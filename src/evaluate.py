# =============================================================
# NIDS - Model Evaluation Module
# Author: Sunishka Singh
# Description: Loads trained models and generates evaluation
#              reports with confusion matrix and metrics
# =============================================================

import os
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    classification_report, accuracy_score,
    precision_score, recall_score, f1_score,
    confusion_matrix
)
from preprocess import load_data, preprocess


def load_model(filename):
    """Load a trained model from models/ directory."""
    path = f'models/{filename}'
    model = joblib.load(path)
    print(f"[+] Loaded model: {path}")
    return model


def get_metrics(model, X_test, y_test):
    """Calculate evaluation metrics."""
    y_pred = model.predict(X_test)
    metrics = {
        'accuracy':  accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted', zero_division=0),
        'recall':    recall_score(y_test, y_pred, average='weighted', zero_division=0),
        'f1':        f1_score(y_test, y_pred, average='weighted', zero_division=0),
    }
    return y_pred, metrics


def print_report(model_name, y_test, y_pred, metrics):
    """Print formatted evaluation report."""
    print(f"\n{'='*55}")
    print(f"  {model_name} - Full Evaluation Report")
    print(f"{'='*55}")
    print(f"  Accuracy  : {metrics['accuracy']*100:.2f}%")
    print(f"  Precision : {metrics['precision']*100:.2f}%")
    print(f"  Recall    : {metrics['recall']*100:.2f}%")
    print(f"  F1-Score  : {metrics['f1']*100:.2f}%")
    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))


def plot_confusion_matrix(y_test, y_pred, model_name, filename):
    """Plot and save confusion matrix."""
    os.makedirs('results', exist_ok=True)
    labels = sorted(set(y_test))
    cm = confusion_matrix(y_test, y_pred, labels=labels)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=labels, yticklabels=labels)
    plt.title(f'Confusion Matrix - {model_name}')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.tight_layout()
    path = f'results/{filename}'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"[+] Confusion matrix saved to {path}")


def save_results(rf_metrics, svm_metrics):
    """Save evaluation summary to results folder."""
    os.makedirs('results', exist_ok=True)
    path = 'results/evaluation_report.txt'
    with open(path, 'w') as f:
        f.write("NIDS - Model Evaluation Report\n")
        f.write("="*55 + "\n\n")
        for name, m in [("Random Forest", rf_metrics), ("SVM", svm_metrics)]:
            f.write(f"{name}:\n")
            f.write(f"  Accuracy  : {m['accuracy']*100:.2f}%\n")
            f.write(f"  Precision : {m['precision']*100:.2f}%\n")
            f.write(f"  Recall    : {m['recall']*100:.2f}%\n")
            f.write(f"  F1-Score  : {m['f1']*100:.2f}%\n\n")
        winner = "Random Forest" if rf_metrics['f1'] > svm_metrics['f1'] else "SVM"
        f.write(f"Best Model (by F1): {winner}\n")
    print(f"[+] Evaluation report saved to {path}")


if __name__ == '__main__':
    # Load and preprocess data
    train, test = load_data()
    X_train, X_test, y_train, y_test = preprocess(train, test)

    # Load trained models
    rf_model  = load_model('random_forest.pkl')
    svm_model = load_model('svm.pkl')

    # Evaluate Random Forest
    rf_pred, rf_metrics = get_metrics(rf_model, X_test, y_test)
    print_report("Random Forest", y_test, rf_pred, rf_metrics)
    plot_confusion_matrix(y_test, rf_pred, "Random Forest", "cm_random_forest.png")

    # Evaluate SVM
    svm_pred, svm_metrics = get_metrics(svm_model, X_test, y_test)
    print_report("SVM", y_test, svm_pred, svm_metrics)
    plot_confusion_matrix(y_test, svm_pred, "SVM", "cm_svm.png")

    # Save results
    save_results(rf_metrics, svm_metrics)

    # Final summary
    print(f"\n{'='*55}")
    print(f"  FINAL COMPARISON")
    print(f"{'='*55}")
    print(f"  {'Model':<20} {'Accuracy':>10} {'F1-Score':>10}")
    print(f"  {'-'*40}")
    print(f"  {'Random Forest':<20} {rf_metrics['accuracy']*100:>9.2f}% {rf_metrics['f1']*100:>9.2f}%")
    print(f"  {'SVM':<20} {svm_metrics['accuracy']*100:>9.2f}% {svm_metrics['f1']*100:>9.2f}%")
    print(f"{'='*55}")