# Rossmann Store Sales Forecasting

## 1. Project Overview

This project focuses on forecasting daily sales for Rossmann retail stores using historical sales data, store information, promotions, and calendar-related features. The goal is to build a reliable forecasting solution that helps analyze store performance, understand sales patterns, and predict future sales.

## 2. Project Objectives

- Explore and understand historical retail sales data.
- Perform data cleaning and exploratory data analysis (EDA).
- Engineer features for sales forecasting.
- Develop and evaluate forecasting models.
- Compare model performance using RMSPE.
- Forecast customer visits.
- Build an interactive Streamlit dashboard to explore forecasts.

## 3. Dataset

The project uses the Rossmann Store Sales dataset.

Main data files:

- `train.csv` - Historical training sales data.
- `test.csv` - Data for which sales predictions are required.
- `store.csv` - Store-related information.
- `sample_submission.csv` - Expected submission format.

**Data management:** Dataset files are managed using DVC. The repository contains the `Data.dvc` tracking file.

## 4. Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- CatBoost
- TensorFlow / Keras
- MLflow
- DVC
- Streamlit
- Jupyter Notebook
- Git and GitHub

## 5. Project Structure

```text
P6/
|-- .dvc/
|-- Notebooks/
|   |-- 01_data_exploration.ipynb
|   |-- 02_sales_modelling.ipynb
|   |-- 03_lstm_forecasting.ipynb
|   |-- 04_customer_forecasting.ipynb
|   |-- README.md
|-- Reports/
|   |-- figures/
|   |-- tables/
|-- Data.dvc
|-- app.py
|-- log_model_artifacts.py
|-- track_experiments.py
|-- Project 6.pdf
|-- .gitignore
|-- .dvcignore
```

## 6. Model Development

The project explores multiple forecasting approaches:

- Historical median baseline.
- Store and weekday-based baseline.
- CatBoost forecasting model.
- LSTM forecasting model.
- Baseline and CatBoost blending approach.

The selected baseline and CatBoost blend achieved a validation RMSPE of approximately **12.68%** in the recorded evaluation.

The customer forecasting analysis also compares store-level and store-weekday-promotion baselines.

## 7. Experiment Tracking

MLflow is used to track model experiments, evaluation metrics, and model artifacts.

DVC is used to manage dataset and trained model versioning.

## 8. Interactive Dashboard

A Streamlit dashboard is included to explore forecast results.

Dashboard features:

- Store selection.
- Date range filtering.
- Forecast sales KPI.
- Forecast customer visits KPI.
- Daily sales and customer forecast charts.
- Top-performing store comparison.
- Store performance table.
- CSV and Excel report downloads.

## 9. Running the Dashboard

Install the required Python packages in your project environment, then run:

```bash
streamlit run app.py
```

## 10. Current Project Scope

This project includes a retail sales forecasting workflow covering data analysis, model development, evaluation, experiment tracking, and dashboard development.

### Completed Components

- Data cleaning and exploratory data analysis (EDA).
- Feature engineering and statistical analysis.
- Sales forecasting using baseline, Ridge Regression, Random Forest, and CatBoost models.
- LSTM-based forecasting experiments.
- Sales prediction using a 50–50 baseline and CatBoost blend.
- Customer forecasting using store, weekday, and promotion-based information.
- Model evaluation using MAE, RMSE, and RMSPE.
- Interactive Streamlit dashboard for sales and customer forecasts.
- MLflow experiment tracking and model artifact logging.
- DVC-based dataset and trained model versioning.

### Data and Model Management

- Dataset files are tracked using DVC and stored on DagsHub.
- Trained model files are tracked using DVC and stored on DagsHub.
- GitHub stores the project source code, documentation, and DVC tracking files.
- Python dependencies are documented in `requirements.txt`.

### Remaining Tasks

- Prepare the final project report.
- Prepare the project presentation.
- Complete final testing and submission verification.

## 11. Author

**Mahima Thorecha**

Data Science & AI

GitHub: [mahimathorecha](https://github.com/mahimathorecha)