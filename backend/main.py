from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load AI model
model = joblib.load('ai-engine/model.pkl')

@app.get("/predict")
async def predict_revenue(month: int):
    next_month = np.array([[month]]).reshape(-1, 1)
    prediction = model.predict(next_month)[0]
    return {"predicted_revenue": f"${prediction:.2f}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
