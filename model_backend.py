import fastapi
import joblib
from model_utils import load_model, make_prediction

app = fastapi.FastAPI()
model = load_model()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.get("/predict")
def predict(size: float, nb_rooms: float, garden: float):
    return {"prediction": make_prediction(size, nb_rooms, garden, model)[0]}
