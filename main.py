from sklearn.model_selection import train_test_split
import cv2
import os
import fastapi
from fastapi import FastAPI,UploadFile, File
import joblib
from tensorflow.keras.models import load_model
import uvicorn

import numpy as np


model = load_model('cancer_detector1.keras')
app = FastAPI()



# Маршрут для загрузки файла и выполнения предсказания
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img_array = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (30, 30))  # Предполагается, что размер изображения 30x30
    img = img / 255.0  # Нормализация
    img = np.expand_dims(img, axis=0)  # Добавление размерности батча
    prediction = model.predict(img)
    return {"prediction": prediction.tolist()}




if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=80)

