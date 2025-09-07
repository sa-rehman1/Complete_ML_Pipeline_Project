```markdown
# 🚀 End-to-End Production Grade MLOps Project  

This repository demonstrates how to take a **simple ML problem (text classification)** and turn it into a **fully automated, production-grade MLOps pipeline**.  
The goal was not just accuracy — but to design the **engineering backbone** required for deploying and monitoring ML models at scale.  

---

## 📌 Project Overview  

- **Problem Statement:** Text Classification (predicting labels from text data)  
- **Objective:** Build an end-to-end ML system with data management, experiment tracking, automation, deployment, and monitoring  
- **Tech Stack:**  
  - **Cloud & Infra:** AWS S3, AWS ECR, AWS EKS  
  - **Experiment Tracking:** Dagshub + MLflow  
  - **Pipeline Orchestration:** DVC  
  - **CI/CD:** GitHub Actions  
  - **Containerization & Deployment:** Docker, Kubernetes  
  - **Monitoring:** Prometheus + Grafana  

---

## ⚙️ Pipeline Architecture  

The project is structured as modular pipelines under the `src/` folder:  

```

src/
│── data\_ingestion.py
│── data\_preprocessing.py
│── feature\_engineering.py
│── model\_building.py
│── model\_evaluation.py
│── register\_model.py

````

Each stage feeds into the next, creating a reproducible workflow.  

- **Data Ingestion:** Loads raw data from AWS S3  
- **Preprocessing & Feature Engineering:** Cleans and transforms data  
- **Model Training:** Trains ML models with tracked hyperparameters  
- **Evaluation:** Compares metrics across runs  
- **Model Registry:** Implements **Challenger vs. Champion strategy** — only better models replace the production one  

---

## 🔄 Workflow Automation  

- **DVC Pipeline:**  
  Defined in `dvc.yaml` for reproducible pipelines. Run the full pipeline with:  
  ```bash
  dvc repro
````

* **CI/CD with GitHub Actions:**
  Ensures code quality and pipeline integrity with automated testing (`.github/workflows/ci.yaml`).

---

## 📦 Deployment

* **Dockerized the pipeline** and pushed images to **AWS ECR**
* Deployed on **Kubernetes (EKS)** for scalability and reliability

---

## 📊 Monitoring

* Integrated **Prometheus + Grafana** to monitor:

  * Model performance metrics
  * System health (CPU, memory, latency)

---

## 📸 Screenshots

* MLflow Dashboard (experiment runs & metrics comparison)
* DVC DAG (pipeline graph)
* GitHub Actions workflow passing ✅
* Grafana dashboard with live metrics

*(Screenshots are available in the `assets/` folder)*

---

## 🛠️ How to Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/<username>/<repo>.git
   cd <repo>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run DVC pipeline:

   ```bash
   dvc repro
   ```

4. Launch MLflow UI for experiment tracking:

   ```bash
   mlflow ui
   ```

---

## 🚀 Key Learnings

* How to move from **notebooks → production pipelines**
* Setting up **experiment tracking, model registry, and versioning**
* Designing **CI/CD for ML workflows**
* Deploying on **cloud-native infrastructure (AWS + Kubernetes)**
* Monitoring with **Prometheus & Grafana**

---

## 📂 Repository Structure

```
.
├── src/                 # Modular pipeline scripts
├── dvc.yaml             # DVC pipeline definition
├── .github/workflows/   # CI/CD workflows
├── Dockerfile           # Containerization
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── assets/              # Screenshots & visuals
```

---

## 📬 Contact

👤 Syed Abdul Rehman

* LinkedIn: linkedin.com/in/sa-rehman1/
* Email: contactsyed135@gmail.com

---

✨ *This project showcases how to productionize ML workflows, making them scalable, reproducible, and deployment-ready.*

```

