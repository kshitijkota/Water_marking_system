#SHA 256 hash (type 1)

'''import hashlib
from PIL import Image
import numpy as np

def image_to_hash(image_path, hash_func='sha256'):
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        img_data = np.array(img)
        img_bytes = img_data.tobytes()
        
        if hash_func == 'md5':
            hash_object = hashlib.md5(img_bytes)
        elif hash_func == 'sha1':
            hash_object = hashlib.sha1(img_bytes)
        elif hash_func == 'sha256':
            hash_object = hashlib.sha256(img_bytes)
        else:
            raise ValueError("Unsupported hash function")
        
        return hash_object.hexdigest()

hash_value = image_to_hash('Restaurant 365.jpg', 'sha256')
print(hash_value)'''

# using phash(type 2)

'''from PIL import Image
import imagehash

def perceptual_hash(image_path, hash_func='phash'):
    img = Image.open(image_path)
    
    if hash_func == 'ahash':
        hash_value = imagehash.average_hash(img)
    elif hash_func == 'phash':
        hash_value = imagehash.phash(img)
    elif hash_func == 'dhash':
        hash_value = imagehash.dhash(img)
    else:
        raise ValueError("Unsupported perceptual hash function")
    
    return str(hash_value)

hash_value = perceptual_hash('Restaurant 365.jpg', 'phash')
print(hash_value)'''

#histogram watermark (type 3)

'''import cv2
import hashlib
import numpy as np

def histogram_hash(image_path):
    img = cv2.imread(image_path)
    hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    hash_object = hashlib.sha256(hist)
    return hash_object.hexdigest()

hash_value = histogram_hash('Restaurant 365.jpg')
print(hash_value)'''

from PIL import Image
from PIL import JpegImagePlugin

def add_comment_to_jpeg(image_path, comment, output_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Ensure it's a JPEG file
        if img.format != 'JPEG':
            raise ValueError("The image file is not a JPEG")

        # Create a copy of the image info dictionary
        info = img.info.copy()

        # Add or update the 'comment' entry in the info dictionary
        info["comments"] = comment

        # Save the image with the new comment
        img.save(output_path, "JPEG", **info)

# Example usage
add_comment_to_jpeg('Restaurant 365.jpg', 'This is a sample comment', 'Resataurant 365_2.jpg')

