import os
from pathlib import Path

import joblib
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent
model_path = os.path.join(BASE_DIR, "app", "rfc_model.pkl")
loaded_model = joblib.load(model_path)

app = FastAPI()

num_species = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}


class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/predict/")
async def predict(features: IrisFeatures):
    input_data = [
        [
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width,
        ]
    ]

    pred = loaded_model.predict(input_data)

    return JSONResponse({"species": num_species[pred[0]]})
