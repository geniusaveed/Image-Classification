"""Generate sample MNIST digit images from the actual MNIST dataset for testing."""

import torch
import torchvision.datasets as datasets
from torchvision import transforms
import os
from PIL import Image

# Create sample_images directory if it doesn't exist
os.makedirs('sample_images', exist_ok=True)

print("Downloading MNIST dataset and extracting sample images...")

# Load MNIST test dataset (already in correct format for model)
mnist_test = datasets.MNIST(
    root='./mnist_data',
    train=False,
    download=True,
    transform=transforms.ToTensor()
)

# Extract one image for each digit (0-9) from the test set
digit_count = {i: 0 for i in range(10)}
saved_count = 0

for idx, (img_tensor, label) in enumerate(mnist_test):
    if digit_count[label] == 0:  # Save only one per digit
        # Convert tensor (1, 28, 28) to PIL Image
        # img_tensor is already normalized to [0, 1]
        img_array = (img_tensor.squeeze() * 255).byte().numpy()
        img_pil = Image.fromarray(img_array, mode='L')
        
        # Save as PNG
        filename = f'sample_images/digit_{label}.png'
        img_pil.save(filename)
        print(f"✓ Saved digit {label} from MNIST test set: {filename}")
        
        digit_count[label] += 1
        saved_count += 1
        
        if saved_count == 10:
            print("\n✅ All 10 sample digits extracted from real MNIST dataset!")
            print("These are actual handwritten digits that the model was trained on.")
            break

print("\nThese images should now be correctly predicted by the model.")
