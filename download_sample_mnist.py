"""
Generate sample MNIST-like images for testing the classifier
"""
import os
from PIL import Image, ImageDraw
import random

output_dir = os.path.join(os.path.dirname(__file__), "sample_images")
os.makedirs(output_dir, exist_ok=True)

print(f"Generating sample MNIST-like images to: {output_dir}")

# Generate synthetic digit images
for digit in range(10):
    filepath = os.path.join(output_dir, f"digit_{digit}.png")
    
    # Create a 28x28 image with white background
    img = Image.new('L', (28, 28), color=255)
    draw = ImageDraw.Draw(img)
    
    # Draw a simple representation of each digit
    if digit == 0:
        draw.ellipse([4, 4, 24, 24], outline=0, width=2)
    elif digit == 1:
        draw.line([10, 4, 10, 24], fill=0, width=2)
    elif digit == 2:
        draw.arc([4, 4, 24, 14], 0, 180, fill=0, width=2)
        draw.line([4, 14, 24, 14], fill=0, width=2)
        draw.arc([4, 14, 24, 24], 180, 360, fill=0, width=2)
    elif digit == 3:
        draw.arc([4, 4, 24, 14], 0, 180, fill=0, width=2)
        draw.line([4, 14, 24, 14], fill=0, width=2)
        draw.arc([4, 14, 24, 24], 180, 360, fill=0, width=2)
        draw.line([24, 4, 24, 24], fill=0, width=2)
    elif digit == 4:
        draw.line([20, 4, 4, 14], fill=0, width=2)
        draw.line([10, 4, 10, 24], fill=0, width=2)
        draw.line([4, 14, 20, 14], fill=0, width=2)
    elif digit == 5:
        draw.line([24, 4, 4, 4], fill=0, width=2)
        draw.line([4, 4, 4, 14], fill=0, width=2)
        draw.arc([4, 14, 24, 24], 180, 360, fill=0, width=2)
        draw.line([24, 14, 24, 14], fill=0, width=2)
    elif digit == 6:
        draw.arc([4, 4, 24, 24], 0, 360, fill=0, width=2)
        draw.line([4, 14, 24, 14], fill=0, width=2)
    elif digit == 7:
        draw.line([4, 4, 24, 4], fill=0, width=2)
        draw.line([20, 4, 8, 24], fill=0, width=2)
    elif digit == 8:
        draw.ellipse([4, 4, 24, 14], outline=0, width=2)
        draw.ellipse([4, 14, 24, 24], outline=0, width=2)
    elif digit == 9:
        draw.arc([4, 4, 24, 24], 0, 360, fill=0, width=2)
        draw.line([20, 4, 20, 24], fill=0, width=2)
    
    img.save(filepath, 'PNG')
    print(f"Generated digit_{digit}.png ✓")

print(f"\nSample images saved to: {output_dir}")
print("You can now upload these images in the frontend for testing!")
