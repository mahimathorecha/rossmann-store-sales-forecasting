import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Rossmann_Sales_Forecasting")

with mlflow.start_run(run_name="Final_Baseline_CatBoost"):
    mlflow.log_param("model", "50-50 Median Baseline + CatBoost")
    mlflow.log_param("baseline_weight", 0.5)
    mlflow.log_param("catboost_weight", 0.5)
    mlflow.log_param("catboost_file", "catboost_final.cbm")
    mlflow.log_param("baseline_file", "final_baseline_bundle.joblib")

    mlflow.log_metric("backtest_1_rmspe_pct", 14.18)
    mlflow.log_metric("backtest_2_rmspe_pct", 13.61)

    mlflow.set_tag("project", "Rossmann Sales Forecasting")
    mlflow.set_tag("model_status", "Final validation model")

print("Successfully logged model results to MLflow!")
