# dsci-310-group-11 - Wine Quality Analysis

## Contributors

- Rudy Ma
- Oscar Cheng
- Tyler Stevenson

## Project Summary

This project analyzes the UCI Machine Learning Wine Quality dataset ([link](https://archive.ics.uci.edu/dataset/186/wine+quality)) to determine whether the quality of red wine samples can be predicted from their physicochemical properties and, if so, which properties are the strongest indicators of wine quality.

The classification model used for the analysis is a Logistic Regression model from Python's `scikit-learn` library.

The analysis suggests that physicochemical properties are robust predictors of the sensory quality of red wine, with alcohol content standing out as a strong predictor. However, the error rate in the analysis shows that chemical features are not the only determinants of wine quality.

Overall, the model shows that it is possible to use the chemical properties of wine to identify lower-quality wines. This could help wineries flag low-quality batches during production.

## Helper Package

Core reusable functions (data labelling, model training, and visualization) have been abstracted into a separate, independently versioned Python package:

**[winequalityutils](https://github.com/UBC-DSCI-310-2025W2/winequalityutility)** (v0.1.0)

This package provides:

- `generate_quality_label`: Binarises the raw quality score into "Good" / "Bad" labels.
- `train_logistic_regression`: Trains and returns a fitted Logistic Regression classifier.
- `create_quality_boxplot`: Generates and saves an EDA boxplot comparing a numeric feature across quality groups.

Tests for these functions reside in the package repository and are run via continuous integration on every push.

## Dependencies

The project has the following dependencies:

| Package          | Version                                |
| ---------------- | -------------------------------------- |
| pandas           | 2.2.0                                  |
| matplotlib       | 3.8.3                                  |
| seaborn          | 0.13.2                                 |
| scikit-learn     | 1.4.2                                  |
| click            | (installed as transitive dependency)   |
| winequalityutils | v0.1.0                                 |
| Quarto           | 1.4.553 (included in the Docker image) |

All Python dependencies are pinned in the `Dockerfile` to guarantee a reproducible environment.

## Data Validation

To ensure the correctness and quality of the analysis, the pipeline applies **10 automated data validation checks** implemented in `src/data_validation.py`. If any check fails, the pipeline raises an error and halts immediately to prevent downstream use of invalid data.

### Raw data checks (applied after download)

1. All 12 expected columns are present.
2. Every column is numeric.
3. No completely empty rows exist.
4. No column exceeds 5% missing values.
5. No duplicate rows exist.
6. No unexpected negative values in any numeric column.
7. Quality scores are within the valid range [0, 10].
8. The quality column contains more than one unique value.

### Processed data checks (applied after wrangling)

9. The `label` column contains only the expected categories ("Good" and "Bad").

### Train/test split check (applied after splitting)

10. There is no index overlap (data leakage) between the training set and the test set.

## Project Structure

```
dsci-310-group-11/
├── data/
│   ├── raw/                           # Downloaded raw CSV
│   └── processed/                     # Cleaned and labelled CSV
├── results/                           # Output figures and metric tables
├── scripts/
│   ├── data_generator.py              # Downloads raw dataset from UCI
│   ├── data_processor.py              # Cleans data and generates quality labels
│   ├── boxplot_generator.py           # Produces EDA boxplot
│   └── confusion_matrix_generator.py  # Trains model and outputs metrics
├── src/
│   └── data_validation.py             # Data validation checks for the pipeline
├── Dockerfile                         # Reproducible computational environment
├── Makefile                           # Automates the full pipeline
├── report.qmd                         # Quarto source for the final HTML report
├── references.bib                     # Bibliography
├── LICENSE.md
├── CODE_OF_CONDUCT.md
└── CONTRIBUTING.md
```

### Execution Scripts (`scripts/`)

- `data_generator.py`: Downloads the raw dataset directly from the UCI ML Repository.
- `data_processor.py`: Applies validation checks, then calls `winequalityutils.generate_quality_label` to create binary class labels.
- `boxplot_generator.py`: Calls `winequalityutils.create_quality_boxplot` to produce the EDA figure.
- `confusion_matrix_generator.py`: Calls `winequalityutils.train_logistic_regression`, evaluates the model, and writes metric CSVs and a confusion matrix figure.

### Validation Module (`src/`)

- `src/data_validation.py`: Contains `validate_raw_data`, `validate_processed_data`, and `validate_split` — called automatically at each stage of the pipeline.

## Running the Analysis

This project uses Docker to containerize the computational environment and GNU Make to automate the data analysis pipeline.

### 1. Clone the Repository

First, clone this repository to your local machine and navigate into the project root directory:

```bash
git clone [https://github.com/UBC-DSCI-310-2025W2/dsci-310-group-11.git](https://github.com/UBC-DSCI-310-2025W2/dsci-310-group-11.git)
cd dsci-310-group-11
```

### 2. Start the Docker Container

Use the command appropriate for your operating system to launch the container and mount the volume:

#### Mac/Linux (or Git Bash on Windows)

```bash
docker run --rm -p 8888:8888 -v "$(pwd):/home/jovyan/work" oscarcheng77/dsci-310-group-11:latest
```

#### Windows (PowerShell)

```powershell
docker run --rm -p 8888:8888 -v "${PWD}:/home/jovyan/work" oscarcheng77/dsci-310-group-11:latest
```

#### Windows (Command Prompt)

```cmd
docker run --rm -p 8888:8888 -v "%cd%:/home/jovyan/work" oscarcheng77/dsci-310-group-11:latest
```

### 3. Access the Environment

Once the container is running, copy the generated URL (e.g., `http://127.0.0.1:8888/lab?token=...`) from the terminal and paste it into your browser to open JupyterLab.

### 4. Run the Automated Pipeline

Inside JupyterLab, open a terminal via:
**File** -> **New** -> **Terminal**

The `Makefile` automates the workflow through the following dependency structure:

`data_generator.py` (raw CSV) → `data_processor.py` (processed CSV) → EDA and modeling scripts (plots) → Quarto (final HTML report)

To run the full pipeline (download data, preprocess, generate plots, and render report), execute:

```bash
make all
```

### 5. Clean the Environment

To remove all generated files and reset the project state:

```bash
make clean
```

## Licensing

- **Code:** MIT License
- **Project Report:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)

See the `LICENSE.md` file for the full license texts.
