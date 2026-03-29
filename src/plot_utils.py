import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def create_quality_boxplot(
    df, x_col="label", y_col="alcohol", output_path=None
):
    """
    Create a boxplot comparing a numeric variable across wine quality labels.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the data to plot.
    x_col : str, default="label"
        Name of the categorical grouping column.
    y_col : str, default="alcohol"
        Name of the numeric column to plot.
    output_path : str or None, default=None
        Path to save the figure. If None, the figure is not saved.

    Returns
    -------
    matplotlib.axes.Axes
        Axes object containing the boxplot.

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame.
    ValueError
        If x_col or y_col are not columns in df.
    ValueError
        If y_col is not numeric.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    if x_col not in df.columns:
        raise ValueError(f"{x_col} is not a column in df")

    if y_col not in df.columns:
        raise ValueError(f"{y_col} is not a column in df")

    if not pd.api.types.is_numeric_dtype(df[y_col]):
        raise ValueError(f"{y_col} must be numeric")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(
        x=x_col,
        y=y_col,
        data=df,
        palette="Set2",
        hue=x_col,
        legend=False,
        ax=ax,
    )

    ax.set_xlabel("Wine Quality Category", fontsize=12)
    ax.set_ylabel("Alcohol Content (% vol)", fontsize=12)
    ax.set_title("Alcohol Content by Wine Quality Label", fontsize=14)

    plt.tight_layout()

    if output_path is not None:
        fig.savefig(output_path, dpi=300)

    return ax