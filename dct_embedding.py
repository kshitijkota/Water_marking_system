import numpy as np
from PIL import Image
import cv2

def embed_watermark_dct(image_path, watermark, output_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    h, w = image.shape

    # Ensure the watermark is the same size as the image
    watermark = cv2.resize(watermark, (w, h))
    
    # Divide image into 8x8 blocks and apply DCT
    dct_blocks = np.zeros_like(image, dtype=np.float32)
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            block = image[i:i+8, j:j+8]
            dct_block = cv2.dct(np.float32(block))
            dct_blocks[i:i+8, j:j+8] = dct_block

    # Embed the watermark into the DCT coefficients
    alpha = 0.1  # watermark strength
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            dct_blocks[i:i+8, j:j+8] += alpha * watermark[i:i+8, j:j+8]

    # Apply inverse DCT to get the watermarked image
    watermarked_image = np.zeros_like(image, dtype=np.float32)
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            block = dct_blocks[i:i+8, j:j+8]
            idct_block = cv2.idct(block)
            watermarked_image[i:i+8, j:j+8] = idct_block

    # Clip values to range [0, 255] and convert to uint8
    watermarked_image = np.clip(watermarked_image, 0, 255).astype(np.uint8)

    # Save the watermarked image
    cv2.imwrite(output_path, watermarked_image)

# Load or create a watermark
watermark = np.random.rand(512, 512) * 255

# Embed the watermark into an image
embed_watermark_dct('input.jpg', watermark, 'watermarked_output.jpg')


def extract_watermark_dct(watermarked_image_path, original_image_path):
    # Load the original and watermarked images
    original_image = cv2.imread(original_image_path, cv2.IMREAD_GRAYSCALE)
    watermarked_image = cv2.imread(watermarked_image_path, cv2.IMREAD_GRAYSCALE)
    h, w = original_image.shape
    
    # Calculate the DCT of both images
    original_dct_blocks = np.zeros_like(original_image, dtype=np.float32)
    watermarked_dct_blocks = np.zeros_like(watermarked_image, dtype=np.float32)
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            original_block = original_image[i:i+8, j:j+8]
            watermarked_block = watermarked_image[i:i+8, j:j+8]
            original_dct_blocks[i:i+8, j:j+8] = cv2.dct(np.float32(original_block))
            watermarked_dct_blocks[i:i+8, j:j+8] = cv2.dct(np.float32(watermarked_block))
    
    # Extract the watermark
    alpha = 0.1
    extracted_watermark = (watermarked_dct_blocks - original_dct_blocks) / alpha
    
    # Clip values to range [0, 255] and convert to uint8
    extracted_watermark = np.clip(extracted_watermark, 0, 255).astype(np.uint8)
    
    return extracted_watermark

# Extract the watermark from the screenshot
extracted_watermark = extract_watermark_dct('screenshot.jpg', 'input.jpg')
cv2.imwrite('extracted_watermark.jpg', extracted_watermark)
