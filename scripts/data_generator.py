import pandas as pd
from pathlib import Path
import click

@click.command()
@click.option('--input_file', type=str, help = "Path (including filename) or URL of where to read data")
@click.option('--output_file', type=str, help = "Path (including filename) of where to write datafile")

# our dataset url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

def main(input_file, output_file):
    print(f"Downloading data from {input_file}...")

    df = pd.read_csv(input_file, sep=';')
    print(f"The correct dimensions for red wine data should be: {df.shape}")

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"The data has been successfully downloaded and saved to: {output_file}")


if __name__ == "__main__":
    main()