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
- Quarto (1.4.553) (Included in the Docker image)

## Project Structure & Scripts

The analysis pipeline is organized into modular Python scripts stored in the `scripts/` directory. Each script uses `click` to support command-line arguments.

- `data_generator.py`: Downloads the raw dataset from a specified URL.
- `data_processor.py`: Cleans, processes, and transforms the raw data.
- `boxplot_generator.py`: Creates the exploratory data analysis visualization.
- `confusion_matrix_generator.py`: Trains the classification model and generates model evaluation output.

## Running the Analysis

This project uses Docker to containerize the computational environment and GNU Make to automate the data analysis pipeline.

### 1. Start the Docker Container

First, clone this repository and navigate to its root directory in your terminal. Then, use the command appropriate for your operating system to launch the container and mount the volume.

#### For Mac/Linux (or Git Bash on Windows)

docker run --rm -p 8888:8888 -v "$(pwd):/home/jovyan/work" oscarcheng77/dsci-310-group-11:latest

#### For Windows (PowerShell)

docker run --rm -p 8888:8888 -v "${PWD}:/home/jovyan/work" oscarcheng77/dsci-310-group-11:latest

#### For Windows (Command Prompt)

docker run --rm -p 8888:8888 -v "%cd%:/home/jovyan/work" oscarcheng77/dsci-310-group-11:latest

### 2. Run the Automated Pipeline

Once the container is running, copy the generated URL (e.g., http://127.0.0.1:8888/lab?token=...) from the terminal and paste it into your browser to open JupyterLab.

Inside JupyterLab, open a terminal:

File -> New -> Terminal

To run the full pipeline:

make all

### 3. Clean the Environment

To remove all generated files:

make clean

This will allow the project to be accessed from the browser at `localhost:8888`. It will ask for a token for access. The token can be found in the terminal output in a URL containing `?token=`.

## Pipeline Overview

The `Makefile` automates the workflow through the following dependency structure:

`data_generator.py` (raw CSV) → `data_processor.py` (processed CSV) → EDA and modeling scripts (plots) → Quarto (final HTML report)

## Licensing

- **Code:** MIT License
- **Project Report:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)

See the `LICENSE.md` file for the full license texts.
