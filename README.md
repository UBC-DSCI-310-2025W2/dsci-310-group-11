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

## Installation
The project uses Docker for dependency management. Ensure you have Docker installed and running. To set up the Docker environment, do the following.

1. Pull the pre-built Docker image from Docker Hub by running the following command in your terminal:

```bash
docker pull oscarcheng77/dsci-310-group-11:latest
```

2. Run the container using the following command in the terminal:
```
docker run --rm -p 8888:8888 -v "$(pwd):/home/jovyan/work" oscarcheng77/dsci-310-group-11:latest
```

This will allow the project to be accessed from the browser at `localhost:8888`. It will ask for a token for access. The token can be found in the terminal output in a URL containing `?token=`.


## Running the Analysis

The analysis can be run from the browser using the previous steps. Open the `predict_wine_quality.ipynb` file, which contains the analysis model. Code blocks can be run sequentially using `Shift + Enter`.

## Licensing
- **Code:** MIT License  
- **Project Report:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)

See the `LICENSE.md` file for the full license texts.
