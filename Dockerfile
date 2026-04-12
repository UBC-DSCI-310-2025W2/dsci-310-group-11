FROM quay.io/jupyter/scipy-notebook:2024-02-24

WORKDIR /home/jovyan/work

RUN mamba install -y -c conda-forge quarto

COPY . .

RUN pip install --no-cache-dir \
    pandas==2.2.0 \
    matplotlib==3.8.3 \
    seaborn==0.13.2 \
    scikit-learn==1.4.2 \
    git+https://github.com/UBC-DSCI-310-2025W2/winequalityutility.git@v0.1.0