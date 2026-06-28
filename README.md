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

FastAPI:
- FastAPI provides API to run the model from anywhere.
- We will put the model in a docker container and add it to either docker hub or ECR.
- Then, deploy it to AWS.
- FastAPI turns model into an API that can receive data and return predictions.
- Gradio Web UI.
- root is to health check the API endpoint for monitoring and load balancing checks.
- CustomerData class is created to define a structure of how the customer data should look.
- app.post("/predict") is used to make predictions
- Main components: app (initialising the FastAPI app), root (app.get, for health check), customerdata pydantic model, get_prediction (app.post) 


containerization and CI/CD:
- dockerfile: set a python version to use -> set the working directory -> copy the requirements.txt file -> run upgrade pip and install requirements.txt -> copy the entire project -> copy the ML models -> 



