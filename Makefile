# DSCI 310 Group 11 - Data Analysis Pipeline Makefile
# Usage:
# make all   : Run the entire pipeline (download -> process -> eda -> model -> report)
# make clean : Remove all generated data, figures, and reports

# ---------------------------------------------------------
# 0. ALL TARGET (The Master Switch)
# ---------------------------------------------------------
all: report.html

# ---------------------------------------------------------
# 1. DOWNLOAD DATA
# ---------------------------------------------------------
data/raw/winequality-red.csv: scripts/data_generator.py
	python scripts/data_generator.py --input_file "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv" --output_file "data/raw/winequality-red.csv"

# ---------------------------------------------------------
# 2. PROCESS DATA
# ---------------------------------------------------------
data/processed/winequality-red-wrangled.csv: scripts/data_processor.py data/raw/winequality-red.csv
	python scripts/data_processor.py --input_file "data/raw/winequality-red.csv" --output_file "data/processed/winequality-red-wrangled.csv"

# ---------------------------------------------------------
# 3. EDA BOXPLOT
# ---------------------------------------------------------
results/eda_boxplot.png: scripts/boxplot_generator.py data/processed/winequality-red-wrangled.csv
	python scripts/boxplot_generator.py --input_file "data/processed/winequality-red-wrangled.csv" --output_file "results/eda_boxplot.png"

# ---------------------------------------------------------
# 4. MODEL CONFUSION MATRIX
# ---------------------------------------------------------
results/confusion_matrix.png: scripts/confusion_matrix_generator.py data/processed/winequality-red-wrangled.csv
	python scripts/confusion_matrix_generator.py --input_file "data/processed/winequality-red-wrangled.csv" --output_file "results/confusion_matrix.png"

# ---------------------------------------------------------
# 5. QUARTO REPORT
# ---------------------------------------------------------
report.html: report.qmd results/eda_boxplot.png results/confusion_matrix.png
	quarto render report.qmd --to html

# ---------------------------------------------------------
# 6. CLEAN TARGET (The Undo Button)
# ---------------------------------------------------------
clean:
	rm -f data/raw/*.csv
	rm -f data/processed/*.csv
	rm -f results/*.png
	rm -f report.html
	rm -rf *_files/

.PHONY: all clean