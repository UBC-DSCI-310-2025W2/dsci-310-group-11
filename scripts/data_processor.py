import sys
import os
import pandas as pd
from pathlib import Path
import click
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_wrangling import generate_quality_label

@click.command()
@click.option('--input_file', type=str, help = "Path (including filename) of where to read data")
@click.option('--output_file', type=str, help = "Path (including filename) of where to write datafile")

def main(input_file, output_file):
    df = pd.read_csv(input_file)

    split_threshold = 6

    df_wrangled = generate_quality_label(df, split_threshold)

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    df_wrangled.to_csv(output_file, index=False)

    print(df_wrangled["label"].value_counts())
    df_wrangled.head()


if __name__ == "__main__":
    main()