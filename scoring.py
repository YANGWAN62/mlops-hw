# -*- coding: utf-8 -*-
"""Scoring.ipynb
Scoring logic for MLOps HW.
Pure prediction code without HTTP or framework dependencies.
"""

# scoring.py
from typing import Any, Dict, List

def score(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Pure scoring logic. No HTTP, no framework imports.
    Input: a dict parsed from JSON request body
    Output: a dict that can be JSON-serialized
    """
    features: List[float] = payload["features"]

    y = sum(features)

    return {"prediction": y}
