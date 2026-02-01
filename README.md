# mlops-hw
MLOps HW: separation of concerns
This project demonstrates separation of concerns in an MLOps setting.

## Files
- `api.py`: FastAPI layer (API endpoints)
- `scoring.py`: Scoring / prediction logic

## Run
```bash
pip install -r requirements.txt
uvicorn api:app --reload

## Run locally (Docker)
docker build -t mlops-hw .
docker run -p 8000:8000 mlops-hw
# Swagger UI: http://localhost:8000/docs

## Kubernetes manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
