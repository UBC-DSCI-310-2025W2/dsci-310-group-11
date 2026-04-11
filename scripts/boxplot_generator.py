import sys
import os
import pandas as pd
import click
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from winequalityutils import create_quality_boxplot


@click.command()
@click.option('--input_file', type=str, help="Path (including filename) of where to read data")
@click.option('--output_file', type=str, help="Path (including filename) of where to write plot png")
def main(input_file, output_file):
    data_df = pd.read_csv(input_file, sep=',')

    create_quality_boxplot(
        df=data_df,
        x_col='label',
        y_col='alcohol',
        output_path=output_file
    )


if __name__ == "__main__":
    main()