from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API opérationnelle 🚀"}

@app.get("/predict")
def predict():
    # Exemple de résultat simulé (à remplacer par ton vrai code plus tard)
    return {
        "direction": "hausse probable",
        "probabilite": 93.4,
        "tp": 1.0750,
        "sl": 1.0680,
        "type": "buy limit"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
