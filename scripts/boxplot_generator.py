import pandas as pd
import click
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

import click

@click.command
@click.option('--input_file', type=str, help = "Path (including filename) of where to read data")
@click.option('--output_file', type=str, help = "Path (including filename) of where to write plot png")


def main(input_file, output_file):
    # Ensure a directory exists for our figures

    data_df = pd.read_csv(input_file, sep=',')


    plt.figure(figsize=(8, 5))
    # Use box plots to compare the alcohol content distribution of good and bad wines.
    sns.boxplot(x='label', y='alcohol', data= data_df, palette='Set2', hue = 'label', legend = False)

    plt.xlabel("Wine Quality Category", fontsize=12)
    plt.ylabel("Alcohol Content (% vol)", fontsize=12)
    plt.title("Alcohol Content by Wine Quality Label", fontsize=14)
    plt.tight_layout()
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_file)

if __name__ == "__main__":
    main()