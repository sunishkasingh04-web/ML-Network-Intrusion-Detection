# =============================================================
# NIDS - Data Preprocessing Module
# Author: Sunish Kasingh
# Description: Loads and preprocesses the NSL-KDD dataset
# =============================================================

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import joblib
import os

# ── Column names for NSL-KDD dataset ──────────────────────────
COLUMNS = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes',
    'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',
    'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell',
    'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
    'num_access_files', 'num_outbound_cmds', 'is_host_login',
    'is_guest_login', 'count', 'srv_count', 'serror_rate',
    'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
    'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate',
    'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
    'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate', 'label', 'difficulty'
]

# ── Attack category mapping ────────────────────────────────────
ATTACK_MAP = {
    'normal': 'normal',
    'neptune': 'dos', 'back': 'dos', 'land': 'dos', 'pod': 'dos',
    'smurf': 'dos', 'teardrop': 'dos', 'mailbomb': 'dos',
    'apache2': 'dos', 'processtable': 'dos', 'udpstorm': 'dos',
    'ipsweep': 'probe', 'nmap': 'probe', 'portsweep': 'probe',
    'satan': 'probe', 'mscan': 'probe', 'saint': 'probe',
    'ftp_write': 'r2l', 'guess_passwd': 'r2l', 'imap': 'r2l',
    'multihop': 'r2l', 'phf': 'r2l', 'spy': 'r2l',
    'warezclient': 'r2l', 'warezmaster': 'r2l', 'sendmail': 'r2l',
    'named': 'r2l', 'snmpgetattack': 'r2l', 'snmpguess': 'r2l',
    'xlock': 'r2l', 'xsnoop': 'r2l', 'worm': 'r2l',
    'buffer_overflow': 'u2r', 'loadmodule': 'u2r', 'perl': 'u2r',
    'rootkit': 'u2r', 'httptunnel': 'u2r', 'ps': 'u2r',
    'sqlattack': 'u2r', 'xterm': 'u2r'
}


def load_data(train_path='data/KDDTrain+.txt', test_path='data/KDDTest+.txt'):
    """Load NSL-KDD dataset."""
    print("[*] Loading dataset...")
    train = pd.read_csv(train_path, header=None, names=COLUMNS)
    test = pd.read_csv(test_path, header=None, names=COLUMNS)
    print(f"    Train shape: {train.shape}")
    print(f"    Test shape : {test.shape}")
    return train, test


def preprocess(train, test):
    """Encode, map labels, scale features."""
    print("[*] Preprocessing...")

    # Drop difficulty column
    train.drop('difficulty', axis=1, inplace=True)
    test.drop('difficulty', axis=1, inplace=True)

    # Map attack labels to categories
    train['label'] = train['label'].str.strip('.').map(ATTACK_MAP).fillna('unknown')
    test['label'] = test['label'].str.strip('.').map(ATTACK_MAP).fillna('unknown')

    # Encode categorical features
    cat_cols = ['protocol_type', 'service', 'flag']
    le = LabelEncoder()
    for col in cat_cols:
        combined = pd.concat([train[col], test[col]])
        le.fit(combined)
        train[col] = le.transform(train[col])
        test[col] = le.transform(test[col])

    # Separate features and labels
    X_train = train.drop('label', axis=1)
    y_train = train['label']
    X_test = test.drop('label', axis=1)
    y_test = test['label']

    # Scale features
    scaler = MinMaxScaler()
    X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
    X_test = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)

    # Save scaler
    os.makedirs('models', exist_ok=True)
    joblib.dump(scaler, 'models/scaler.pkl')
    print("    Scaler saved to models/scaler.pkl")

    print(f"    Classes: {sorted(y_train.unique())}")
    print("[+] Preprocessing complete.")
    return X_train, X_test, y_train, y_test


if __name__ == '__main__':
    train, test = load_data()
    X_train, X_test, y_train, y_test = preprocess(train, test)
    print("\nLabel distribution (train):")
    print(y_train.value_counts())