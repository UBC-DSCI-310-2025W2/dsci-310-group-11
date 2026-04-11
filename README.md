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

## Dependencies

The project has the following dependencies:

- pandas (2.2.0)
- matplotlib (3.8.3)
- seaborn (0.13.2)
- scikit-learn (1.4.2)
- pytest (8.1.1)
- Quarto (1.4.553) (Included in the Docker image)
- click
- pytest

## Project Structure & Scripts

The project is structured modularly. Core analytical functions are abstracted into the `src/` directory, while execution scripts (using `click` for command-line arguments) reside in `scripts/`:

### Source Modules (`src/`)

- `data_wrangling.py`: Contains abstracted functions for data cleaning and transformation.
- `model_utils.py`: Contains abstracted functions for robust model training.
- `plot_utils.py`: Contains abstracted functions for generating EDA visualizations.

### Execution Scripts (`scripts/`)

- `data_generator.py`: Downloads the raw dataset from a specified URL.
- `data_processor.py`: Cleans, processes, and transforms the raw data using `data_wrangling.py`.
- `boxplot_generator.py`: Creates the exploratory data analysis visualization using `plot_utils.py`.
- `confusion_matrix_generator.py`: Trains the classification model and generates output using `model_utils.py`.

The project also includes modularized helper functions in the `src/` directory and unit tests in the `test/` directory.

- `src/data_wrangling.py`: reusable data cleaning and transformation functions.
- `src/model_utils.py`: reusable model training functions.
- `src/plot_utils.py`: reusable plotting functions.
- `test/test_data_wrangling.py`: tests for data wrangling functions.
- `test/test_model_utils.py`: tests for model utility functions.
- `test/test_plot_utils.py`: tests for plotting functions.

## Running the Analysis

This project uses Docker to containerize the computational environment and GNU Make to automate the data analysis pipeline.

### 1: Clone the Repository

First, clone this repository to your local machine and navigate into the project root directory:

```bash
git clone [https://github.com/UBC-DSCI-310-2025W2/dsci-310-group-11.git](https://github.com/UBC-DSCI-310-2025W2/dsci-310-group-11.git)
cd dsci-310-group-11
```

### 2. Start the Docker Container

Use the command appropriate for your operating system to launch the container and mount the volume:

#### For Mac/Linux (or Git Bash on Windows)

```bash
docker run --rm -p 8888:8888 -v "$(pwd):/home/jovyan/work" oscarcheng77/dsci-310-group-11:latest
```

#### For Windows (PowerShell)

```powershell
docker run --rm -p 8888:8888 -v "${PWD}:/home/jovyan/work" oscarcheng77/dsci-310-group-11:latest
```

#### For Windows (Command Prompt)

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

### 5. Testing

Tests are written using `pytest` and stored in the `test/` directory.

To run all tests:

```bash
pytest
```

## Licensing

- **Code:** MIT License
- **Project Report:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)

See the `LICENSE.md` file for the full license texts.
