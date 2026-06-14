# =============================================================
# NIDS - Model Training Module
# Author: Sunishka Singh
# Description: Trains Random Forest and SVM on NSL-KDD dataset
# =============================================================

import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from preprocess import load_data, preprocess


def train_random_forest(X_train, y_train):
    """Train Random Forest classifier."""
    print("\n[*] Training Random Forest...")
    rf = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    rf.fit(X_train, y_train)
    print("[+] Random Forest training complete.")
    return rf


def train_svm(X_train, y_train):
    """Train SVM classifier."""
    print("\n[*] Training SVM...")
    print("    (This may take a few minutes...)")
    svm = SVC(
        kernel='rbf',
        C=1.0,
        gamma='scale',
        random_state=42
    )
    svm.fit(X_train, y_train)
    print("[+] SVM training complete.")
    return svm


def evaluate_model(model, X_test, y_test, model_name):
    """Evaluate model and print results."""
    print(f"\n{'='*55}")
    print(f"  {model_name} - Evaluation Results")
    print(f"{'='*55}")
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"  Accuracy : {acc * 100:.2f}%")
    classification_report(y_test, y_pred, zero_division=0)
    return acc


def save_model(model, filename):
    """Save trained model to models/ directory."""
    os.makedirs('models', exist_ok=True)
    path = f'models/{filename}'
    joblib.dump(model, path)
    print(f"    Model saved to {path}")


if __name__ == '__main__':
    # Load and preprocess data
    train, test = load_data()
    X_train, X_test, y_train, y_test = preprocess(train, test)

    # Train Random Forest
    rf_model = train_random_forest(X_train, y_train)
    rf_acc = evaluate_model(rf_model, X_test, y_test, "Random Forest")
    save_model(rf_model, 'random_forest.pkl')

    # Train SVM
    svm_model = train_svm(X_train, y_train)
    svm_acc = evaluate_model(svm_model, X_test, y_test, "SVM")
    save_model(svm_model, 'svm.pkl')

    # Summary
    print(f"\n{'='*55}")
    print(f"  TRAINING SUMMARY")
    print(f"{'='*55}")
    print(f"  Random Forest Accuracy : {rf_acc * 100:.2f}%")
    print(f"  SVM Accuracy           : {svm_acc * 100:.2f}%")
    winner = "Random Forest" if rf_acc > svm_acc else "SVM"
    print(f"  Best Model             : {winner}")
    print(f"{'='*55}")