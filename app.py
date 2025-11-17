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
# Note: MNIST mean=0.1307, std=0.3081 (from standard MNIST dataset)
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    # Normalize using MNIST statistics for better accuracy
    transforms.Normalize(mean=(0.1307,), std=(0.3081,))
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
    try:
        contents = await file.read()
        # Open image and ensure it's in RGB mode first, then convert to grayscale
        img = Image.open(io.BytesIO(contents)).convert('RGB')
        # Convert RGB to grayscale (this ensures consistent conversion)
        img = img.convert('L')
        # Apply transforms
        img_tensor = transform(img)
        # Predict
        with torch.no_grad():
            output = model(img_tensor.unsqueeze(0))
            pred = output.argmax(dim=1).item()
            # Get confidence score
            confidence = torch.softmax(output, dim=1)[0][pred].item()
        return {
            "prediction": pred,
            "confidence": round(confidence, 4)
        }
    except Exception as e:
        return {
            "error": str(e),
            "prediction": None
        }
