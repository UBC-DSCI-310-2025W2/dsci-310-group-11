FROM quay.io/jupyter/scipy-notebook:2024-02-24

WORKDIR /home/jovyan/work

COPY . .

RUN pip install --no-cache-dir \
    pandas==2.2.0 \
    matplotlib==3.8.3 \
    seaborn==0.13.2 \
    scikit-learn==1.4.2