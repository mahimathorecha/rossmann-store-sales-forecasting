from pathlib import Path
import mlflow

PROJECT_DIR = Path(__file__).resolve().parent
MODEL_DIR = PROJECT_DIR / "models"

mlflow.set_tracking_uri(
    "sqlite:///D:/DigiCrome%20Academy/Internship/Nexthikes/P6/mlflow.db"
)
mlflow.set_experiment("Rossmann_Sales_Forecasting")

files = [
    "catboost_final.cbm",
    "final_baseline_bundle.joblib",
    "final_model_metadata.json",
]

for filename in files:
    path = MODEL_DIR / filename
    if not path.is_file():
        raise FileNotFoundError(f"Missing model file: {path}")

with mlflow.start_run(run_name="Final_Baseline_CatBoost_With_Artifacts"):
    mlflow.log_param("model", "50-50 Median Baseline + CatBoost")
    mlflow.log_param("artifact_count", len(files))

    for filename in files:
        mlflow.log_artifact(
            str(MODEL_DIR / filename),
            artifact_path="model_files"
        )
        print(f"Uploaded: {filename}")

print("All model artifacts logged successfully!")
