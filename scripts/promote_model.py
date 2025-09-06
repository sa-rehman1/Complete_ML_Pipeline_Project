# promote model

import os
import mlflow

def promote_model():
    # -------------------- Set up DagsHub credentials --------------------
    dagshub_token = os.getenv("CAPSTONE_TEST")
    if not dagshub_token:
        raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

    os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
    os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

    dagshub_url = "https://dagshub.com"
    repo_owner = "sa-rehman1"
    repo_name = "Complete_ML_Pipeline_Project"

    # Set up MLflow tracking URI
    mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')

    client = mlflow.MlflowClient()
    model_name = "my_model"

    # -------------------- Safe fetch latest version --------------------
    stages = ["Staging", "None", "Production"]
    latest_version = None
    for stage in stages:
        versions = client.get_latest_versions(model_name, stages=[stage])
        if versions:
            latest_version = versions[0].version
            break

    if latest_version is None:
        raise ValueError(f"No versions found for model '{model_name}' in any stage")

    # -------------------- Archive current Production model --------------------
    prod_versions = client.get_latest_versions(model_name, stages=["Production"])
    for version in prod_versions:
        client.transition_model_version_stage(
            name=model_name,
            version=version.version,
            stage="Archived"
        )

    # -------------------- Promote the latest version --------------------
    client.transition_model_version_stage(
        name=model_name,
        version=latest_version,
        stage="Production"
    )
    print(f"Model version {latest_version} promoted to Production")


if __name__ == "__main__":
    promote_model()
