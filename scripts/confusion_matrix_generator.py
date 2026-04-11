import sys
import os
import matplotlib.pyplot as plt
import pandas as pd
import click
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay, classification_report
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from winequalityutils import train_logistic_regression

@click.command()
@click.option('--input_file', type=str, help="Path (including filename) of where to read data")
@click.option('--output_file', type=str, help="Path (including filename) of where to write confusion matrix png")
@click.option('--metrics_file', type=str, default="results/model_metrics.csv", help="Path to write per-class metrics CSV")
@click.option('--summary_file', type=str, default="results/report_summary.csv", help="Path to write summary statistics CSV")


def main(input_file, output_file, metrics_file, summary_file):

    # 1. Prepare features and target
    data_df = pd.read_csv(input_file, sep=',')

    x = data_df.drop(columns=["quality", "label"])
    y = data_df["label"]

    # 2. Split data (Stratified ensures Good/Bad ratio remains the same)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=123, stratify=y
    )

    # 3. Train Logistic Regression
    lr_model = train_logistic_regression(x_train, y_train, max_iter=2000, random_state=123)

    # 4. Evaluate and export metrics
    y_pred = lr_model.predict(x_test)
    print(classification_report(y_test, y_pred))

    report_dict = classification_report(y_test, y_pred, output_dict=True)

    metrics_tbl = pd.DataFrame({
        "class": ["Bad", "Good"],
        "precision": [report_dict["Bad"]["precision"], report_dict["Good"]["precision"]],
        "recall": [report_dict["Bad"]["recall"], report_dict["Good"]["recall"]],
        "f1_score": [report_dict["Bad"]["f1-score"], report_dict["Good"]["f1-score"]],
        "support": [int(report_dict["Bad"]["support"]), int(report_dict["Good"]["support"])]
    })
    Path(metrics_file).parent.mkdir(parents=True, exist_ok=True)
    metrics_tbl.to_csv(metrics_file, index=False)

    summary_tbl = pd.DataFrame([{
        "n_rows": int(data_df.shape[0]),
        "good_count": int((data_df["label"] == "Good").sum()),
        "bad_count": int((data_df["label"] == "Bad").sum()),
        "accuracy": float(report_dict["accuracy"]),
        "good_correct": int(((y_test == "Good") & (y_pred == "Good")).sum()),
        "bad_correct": int(((y_test == "Bad") & (y_pred == "Bad")).sum())
    }])
    Path(summary_file).parent.mkdir(parents=True, exist_ok=True)
    summary_tbl.to_csv(summary_file, index=False)

    # 5. Plot and save Confusion Matrix
    disp = ConfusionMatrixDisplay.from_estimator(lr_model, x_test, y_test, cmap=plt.cm.Blues)
    plt.title("Confusion Matrix: Logistic Regression")
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_file, dpi=300)


if __name__ == "__main__":
    main()
