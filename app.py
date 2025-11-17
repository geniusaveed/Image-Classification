from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from torchvision import transforms
from PIL import Image
import torch
import io
from models import SimpleCNN

# --- Load Trained Model ---
import os
model_path = os.path.join(os.path.dirname(__file__), "mnist_cnn.pth")
model = SimpleCNN()
model.load_state_dict(torch.load(model_path, weights_only=False))
model.eval()

# --- Image Preprocessing ---
transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Resize((28, 28)),
    transforms.ToTensor()
])

# --- FastAPI App ---
app = FastAPI()

# Allow frontend to call this API (running on 127.0.0.1:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert('L')  # Convert to grayscale
    img = transform(img)
    with torch.no_grad():
        output = model(img.unsqueeze(0))
        pred = output.argmax(dim=1).item()
    return {"prediction": pred}
