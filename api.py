# -*- coding: utf-8 -*-
"""API.ipynb
API layer for MLOps HW.
Handles HTTP requests and responses.
"""

# api.py
from fastapi import FastAPI, HTTPException
from scoring import score

app = FastAPI()

@app.post("/score")
def score_endpoint(payload: dict):
    try:
        return score(payload)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing field: {e}")
