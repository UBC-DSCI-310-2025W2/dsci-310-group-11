import sys
import os
import matplotlib.pyplot as plt
import pandas as pd
import click
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay, classification_report
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.model_utils import train_logistic_regression

@click.command
@click.option('--input_file', type=str, help = "Path (including filename) of where to read data")
@click.option('--output_file', type=str, help = "Path (including filename) of where to write plot png")


def main(input_file, output_file):

# 1. Prepare features and target

    data_df = pd.read_csv(input_file, sep=',')

    x = data_df.drop(columns=["quality", "label"])
    y = data_df["label"]

    # 2. Split data (Stratified ensures Good/Bad ratio remains the same)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=123, stratify=y
    )

    # 3. Train Logistic Regression
    lr_model = lr_model = train_logistic_regression(x_train, y_train, max_iter=2000, random_state=123)

    # 4. Show Classification Report
    y_pred = lr_model.predict(x_test)
    print(classification_report(y_test, y_pred))

    # 5. Plot Confusion Matrix
    disp = ConfusionMatrixDisplay.from_estimator(lr_model, x_test, y_test, cmap=plt.cm.Blues)
    plt.title("Confusion Matrix: Logistic Regression")
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)    
    plt.savefig(output_file, dpi=300)

    
if __name__ == "__main__":
    main()
