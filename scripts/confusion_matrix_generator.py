from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt
import pandas as pd
import click
from pathlib import Path

@click.command
@click.option('--input_file', type=str, help = "Path (including filename) of where to read data")
@click.option('--output_file', type=str, help = "Path (including filename) of where to write plot png")


def main(input_file, output_file):

# 1. Prepare features and target

    data_df = pd.read_csv(input_file, sep=',')

    X = data_df.drop(columns=["quality", "label"])
    y = data_df["label"]

    # 2. Split data (Stratified ensures Good/Bad ratio remains the same)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=123, stratify=y
    )

    # 3. Train Logistic Regression
    lr_model = LogisticRegression(max_iter=2000)
    lr_model.fit(X_train, y_train)

    # 4. Show Classification Report
    y_pred = lr_model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # 5. Plot Confusion Matrix
    disp = ConfusionMatrixDisplay.from_estimator(lr_model, X_test, y_test, cmap=plt.cm.Blues)
    plt.title("Confusion Matrix: Logistic Regression")
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)    
    plt.savefig(output_file, dpi=300)

    
if __name__ == "__main__":
    main()
