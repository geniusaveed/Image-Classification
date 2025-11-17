# MNIST Digit Classifier

A full-stack web application for classifying handwritten digits using a trained CNN model.

## Features

- 🔢 **Handwritten Digit Recognition**: Upload PNG/JPG images and get instant predictions
- 🎨 **Modern Web Interface**: Beautiful React frontend with drag-and-drop file upload
- ⚡ **Fast Backend**: FastAPI server with CORS support for real-time predictions
- 🧠 **Trained CNN Model**: Pre-trained on MNIST dataset (28x28 grayscale images)
- 📱 **Responsive Design**: Works on desktop and mobile browsers

## Project Structure

```
.
├── app.py                    # FastAPI backend server
├── mnist_cnn.py             # CNN model architecture & training script
├── mnist_cnn.pth            # Pre-trained model weights
├── download_sample_mnist.py # Generate sample test images
├── start_backend.ps1        # PowerShell script to start backend
├── sample_images/           # Sample digit images for testing
├── mnist-frontend/          # React frontend application
│   ├── public/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── App.css
│   │   └── index.tsx
│   └── package.json
└── README.md
```

## Prerequisites

- **Python 3.9+** (Miniconda/Anaconda recommended)
- **Node.js 16+** (for frontend)
- **pip** or **conda** for package management

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Image-Classification.git
cd Image-Classification
```

### 2. Backend Setup

Install Python dependencies:
```bash
# Using pip
pip install torch torchvision fastapi uvicorn python-multipart pillow starlette

# Or using conda
conda install -c pytorch pytorch torchvision
conda install fastapi uvicorn pillow
```

### 3. Frontend Setup

```bash
cd mnist-frontend
npm install
cd ..
```

## Running the Application

### Start Backend (Terminal 1)
```bash
# Using the startup script (Windows)
powershell -ExecutionPolicy Bypass -File start_backend.ps1

# Or manually
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Backend will be available at: `http://127.0.0.1:8000`

### Start Frontend (Terminal 2)
```bash
cd mnist-frontend
npm start
```

Frontend will be available at: `http://127.0.0.1:3000`

## Usage

1. Open `http://127.0.0.1:3000` in your browser
2. Click the file upload area to select an image
3. Supported formats: PNG, JPG, JPEG (recommended: 28x28 grayscale)
4. Click **Predict** to get the model's prediction
5. The model will return a digit (0-9)

### Test with Sample Images

Generate sample images for testing:
```bash
python download_sample_mnist.py
```

This creates 10 sample digit images in the `sample_images/` folder.

## Model Information

- **Architecture**: Convolutional Neural Network (CNN)
- **Input Size**: 28×28 grayscale images
- **Output**: Digit classification (0-9)
- **Training Data**: MNIST dataset
- **Framework**: PyTorch

## API Endpoints

### POST `/predict`
Upload an image and get a prediction.

**Request:**
```bash
curl -X POST -F "file=@digit_image.png" http://127.0.0.1:8000/predict
```

**Response:**
```json
{
  "prediction": 5
}
```

## Troubleshooting

### Backend won't start
- Ensure Python 3.9+ is installed
- Check all dependencies are installed: `pip install torch torchvision fastapi uvicorn`
- Verify `mnist_cnn.pth` model file exists

### Frontend won't load
- Ensure Node.js is installed
- Run `npm install` in `mnist-frontend/` folder
- Check that port 3000 is not in use

### CORS errors
- Backend should be running on `http://127.0.0.1:8000`
- Frontend should access it from `http://127.0.0.1:3000`
- CORS is configured in `app.py` middleware

## Technologies Used

- **Backend**: FastAPI, PyTorch, Python
- **Frontend**: React, TypeScript, CSS3
- **Model**: CNN (Convolutional Neural Network)
- **Server**: Uvicorn

## Future Enhancements

- [ ] Batch prediction support
- [ ] Model accuracy metrics dashboard
- [ ] Support for custom trained models
- [ ] Docker containerization
- [ ] Deploy to cloud (AWS, GCP, Heroku)

## License

MIT License - Feel free to use this project for learning and development.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Author**: Your Name
**Created**: November 2025
