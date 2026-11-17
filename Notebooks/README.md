# Corrected P6 notebooks

Back up your existing notebooks, then copy these four notebooks into P6/Notebooks.
Keep data/train.csv, data/test.csv, data/store.csv and data/sample_submission.csv under P6/data. Keep existing models, reports and predictions.

## Changes
- 01: retained EDA and added reproduction guidance.
- 02: removed obsolete feature-importance cell with TypeError; kept the working get_feature_importance calculation; initialized logging before modelling; moved event logging to the relevant stages.
- 03: removed stale NameError and duplicate recovery/empty metadata cells; retained one metadata export after checkpoint loading; locate the project by data rather than requiring a trained CatBoost file; use the explicit data/train.csv path.
- 04: extracted customer forecasting into an independent notebook, added its metric imports and portable project discovery, removed recursive CSV searches, and added a clear missing-sales-file diagnostic before the final merge.

## Running
Existing results remain visible where code was unchanged. These are historical outputs, not a claim that every notebook was rerun. Edited cells have outputs cleared. Run cells in order within each notebook from a fresh kernel. Notebook 02 and 03 Run All will retrain models. You do not need to rerun them merely to adopt these cleanup changes. Notebook 04 is independent until its last cell, which needs predictions/test_predictions_detailed.csv from notebook 02. Notebook 03's matched comparison requires reports/tables/blend_validation_predictions.csv from notebook 02.

## Verification
All four notebooks passed Python syntax checks (excluding notebook installation magics), and contain no stored error outputs. Executed notebook 04's data preparation, both backtests, model save/reload, and customer forecast export against the uploaded data in an isolated directory: 1,017,209 training records and 41,088 forecasts; checks passed. The noninteractive verification replaced display with a no-op. The final merge was not executed because the sales prediction CSV was not provided. CatBoost/LSTM were not retrained, and their saved binaries were not available to verify.

## Remaining scope
Explicit days-before/after-holiday features are not part of the existing 27-feature sales model. Implementing and evaluating them requires a new feature/model version and retraining. This cleanup does not add them to the saved model schema. Dashboard, deployment, experiment tracking and final project documentation remain separate work; this package does not claim those are complete.
