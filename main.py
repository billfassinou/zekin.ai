from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from catboost import CatBoostClassifier

# Charger le modèle CatBoostClassifier sauvegardé
model = CatBoostClassifier()
model.load_model("CatBoostClassifier.cb")

# Définir une classe Pydantic pour valider les données d'entrée
class InputData(BaseModel):
    process: str
    amount: int
    phoneNumber: str
    canal: str
    country: str
    event: str
    browser: str
    ip: str
    agregator: str
    # Ajoutez d'autres caractéristiques selon votre modèle

# Initialiser FastAPI
app = FastAPI()

# Définir une route pour effectuer des prédictions avec POST
@app.post("/predict")
async def predict_post(data: InputData):
    try:
        # Convertir les données d'entrée en DataFrame
        input_df = pd.DataFrame([data.model_dump()])
        
        # Faire une prédiction avec le modèle CatBoostClassifier
        prediction = model.predict(input_df)
        
        # Renvoyer la prédiction
        return str(prediction[0][0])
    except Exception as e:
        # En cas d'erreur, renvoyer un message d'erreur
        return {"error": str(e)}

# Définir une route pour effectuer des prédictions avec GET
@app.get("/predict/{data_id}")
async def predict_get(data_id: int):
    # Ici, vous devez implémenter la logique pour récupérer 
    # les données correspondantes à data_id et les transformer en DataFrame
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
