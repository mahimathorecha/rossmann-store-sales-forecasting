
import mlflow

# Connect to your existing MLflow database
mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Select your existing experiment
mlflow.set_experiment("Rossmann_Sales_Forecasting")

# Validation results from final_model_metadata.json
validation_results = {
    "backtest_1": {
        "period": "2015-05-09 to 2015-06-19",
        "rmspe_pct": 14.18
    },
    "backtest_2": {
        "period": "2015-06-20 to 2015-07-31",
        "rmspe_pct": 13.61
    }
}

# Start an MLflow run
with mlflow.start_run(run_name="Final_Baseline_CatBoost"):

    # Log model information
    mlflow.log_param(
        "model",
        "50-50 Median Baseline + CatBoost"
    )

    mlflow.log_param("baseline_weight", 0.5)
    mlflow.log_param("catboost_weight", 0.5)

    mlflow.log_param(
        "catboost_file",
        "catboost_final.cbm"
    )

    mlflow.log_param(
        "baseline_file",
        "final_baseline_bundle.joblib"
    )

    # Log validation metrics
    mlflow.log_metric(
        "backtest_1_rmspe_pct",
        validation_results["backtest_1"]["rmspe_pct"]
    )

    mlflow.log_metric(
        "backtest_2_rmspe_pct",
        validation_results["backtest_2"]["rmspe_pct"]
    )

    # Add experiment tags
    mlflow.set_tag(
        "project",
        "Rossmann Sales Forecasting"
    )

    mlflow.set_tag(
        "model_status",
        "Final validation model"
    )

print("Successfully logged model results to MLflow!")
