MLOps Telco Customer Churn Project

Pipeline:
1. Data Validation: "Great Expectations" ensures data quality and schema consistency.
2. Modeling
3. Containerization: Docker packages the application for consistent deployment.
4. ML Tracking: MLflow logs experiments, metrics, and artifacts.
5. Serving: FastAPi procides REST endpoints and Gradio offers a web UI.
6. Deployment: AWS ECS hosts containerized application.



Setup project from scratch using the following command:
mkdir -p data/raw data/processed data/external notebooks src/{data,features,models,utils} app configs scripts tests .github/workflows docker great_expectations mlruns artifacts

scripts:
- Data and preprocessign scripts: Data loading, quality checks, preprocessing
- Feature engineering script
- Model training script
- Pipeline orchestration script: ties everything together in a reproducible training flow (load->validate->preprocess->feature engineering)
- Experiment tracking (MLFlow): logging everything
- 