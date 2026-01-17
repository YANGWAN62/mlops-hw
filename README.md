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
