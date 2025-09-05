# register_model

import json
import mlflow
import logging
from src.logger import logging
import os
import warnings

warnings.simplefilter("ignore", UserWarning)
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
load_dotenv()

# Load DagsHub / MLflow credentials
dagshub_token = os.getenv("CAPSTONE_TEST")
if not dagshub_token:
    raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token
mlflow_tracking_uri = os.getenv("MLFLOW_TRACKING_URI")

# Only initialize dagshub locally (skip in CI/CD)
if not os.getenv("GITHUB_ACTIONS"):
    import dagshub
    dagshub_cred_owner = os.getenv("DAGSHUB_CRED_OWNER")
    dagshub_cred_name = os.getenv("DAGSHUB_CRED_NAME")
    if dagshub_cred_owner and dagshub_cred_name:
        dagshub.init(repo_owner=dagshub_cred_owner,
                     repo_name=dagshub_cred_name,
                     mlflow=True)

def load_model_info(file_path: str) -> dict:
    """Load the model info from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            model_info = json.load(file)
        logging.debug('Model info loaded from %s', file_path)
        return model_info
    except FileNotFoundError:
        logging.error('File not found: %s', file_path)
        raise
    except Exception as e:
        logging.error('Unexpected error occurred while loading the model info: %s', e)
        raise

def register_model(model_name: str, model_info: dict):
    """Register the model to the MLflow Model Registry."""
    try:
        model_uri = f"runs:/{model_info['run_id']}/{model_info['model_path']}"
        
        # Register the model
        model_version = mlflow.register_model(model_uri, model_name)
        
        # Transition the model to "Staging" stage
        client = mlflow.tracking.MlflowClient()
        client.transition_model_version_stage(
            name=model_name,
            version=model_version.version,
            stage="Staging"
        )
        
        logging.debug(f'Model {model_name} version {model_version.version} registered and transitioned to Staging.')
    except Exception as e:
        logging.error('Error during model registration: %s', e)
        raise

def main():
    try:
        model_info_path = 'reports/experiment_info.json'
        model_info = load_model_info(model_info_path)
        
        model_name = "my_model"
        register_model(model_name, model_info)
    except Exception as e:
        logging.error('Failed to complete the model registration process: %s', e)
        print(f"Error: {e}")

if __name__ == '__main__':
    main()

#The code which is not working now
# # register model

# import json
# import mlflow
# import logging
# from src.logger import logging
# import os
# import dagshub

# import warnings
# warnings.simplefilter("ignore", UserWarning)
# warnings.filterwarnings("ignore")


# from dotenv import load_dotenv
# load_dotenv()
# dagshub_token = os.getenv("CAPSTONE_TEST")
# if not dagshub_token:
#     raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

# os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
# os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token


# mlflow_tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
# # -------------------------------------------------------------------------------------


# def load_model_info(file_path: str) -> dict:
#     """Load the model info from a JSON file."""
#     try:
#         with open(file_path, 'r') as file:
#             model_info = json.load(file)
#         logging.debug('Model info loaded from %s', file_path)
#         return model_info
#     except FileNotFoundError:
#         logging.error('File not found: %s', file_path)
#         raise
#     except Exception as e:
#         logging.error('Unexpected error occurred while loading the model info: %s', e)
#         raise

# def register_model(model_name: str, model_info: dict):
#     """Register the model to the MLflow Model Registry."""
#     try:
#         model_uri = f"runs:/{model_info['run_id']}/{model_info['model_path']}"
        
#         # Register the model
#         model_version = mlflow.register_model(model_uri, model_name)
        
#         # Transition the model to "Staging" stage
#         client = mlflow.tracking.MlflowClient()
#         client.transition_model_version_stage(
#             name=model_name,
#             version=model_version.version,
#             stage="Staging"
#         )
        
#         logging.debug(f'Model {model_name} version {model_version.version} registered and transitioned to Staging.')
#     except Exception as e:
#         logging.error('Error during model registration: %s', e)
#         raise

# def main():
#     try:
#         model_info_path = 'reports/experiment_info.json'
#         model_info = load_model_info(model_info_path)
        
#         model_name = "my_model"
#         register_model(model_name, model_info)
#     except Exception as e:
#         logging.error('Failed to complete the model registration process: %s', e)
#         print(f"Error: {e}")

# if __name__ == '__main__':
#     main()

