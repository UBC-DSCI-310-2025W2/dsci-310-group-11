import pandas as pd
from pathlib import Path
import click

@click.command
@click.option('--input_file', type=str, help = "Path (including filename) of where to read data")
@click.option('--output_file', type=str, help = "Path (including filename) of where to write datafile")

def main(input_file, output_file):
    df_wrangled = pd.read_csv(input_file)
    df_wrangled["label"] = df_wrangled["quality"].apply(lambda x: "Good" if x >= 6 else "Bad")

    df_wrangled.to_csv(output_file, index=False)

    print(df_wrangled["label"].value_counts())
    df_wrangled.head()


if __name__ == "__main__":
    main()