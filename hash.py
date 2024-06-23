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

import cv2
import hashlib
import numpy as np

def histogram_hash(image_path):
    img = cv2.imread(image_path)
    hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    hash_object = hashlib.sha256(hist)
    return hash_object.hexdigest()

hash_value = histogram_hash('Restaurant 365.jpeg')
print("Hash produced is: ",hash_value)

def add_comment_to_jpeg_com(image_path, comment, output_path):
    with open(image_path, "rb") as f:
        jpeg_data = f.read()

    # Define JPEG markers
    SOI_MARKER = b"\xFF\xD8"  # Start of Image
    EOI_MARKER = b"\xFF\xD9"  # End of Image
    COM_MARKER = b"\xFF\xFE"  # Comment Marker

    if jpeg_data[:2] != SOI_MARKER:
        raise ValueError("The file is not a valid JPEG image.")

    # Find the position to insert the comment
    insert_pos = 2  # Right after the SOI marker

    # Construct the comment segment
    comment_bytes = comment.encode("utf-8")
    comment_length = len(comment_bytes) + 2  # Length includes 2 bytes for length field
    comment_segment = COM_MARKER + comment_length.to_bytes(2, "big") + comment_bytes

    # Insert the comment segment into the JPEG data
    modified_jpeg_data = (
        jpeg_data[:insert_pos] + comment_segment + jpeg_data[insert_pos:]
    )

    with open(output_path, "wb") as f:
        f.write(modified_jpeg_data)


def read_comment_from_jpeg_com(image_path):
    with open(image_path, "rb") as f:
        jpeg_data = f.read()

    # Define JPEG markers
    COM_MARKER = b"\xFF\xFE"

    pos = 0
    while pos < len(jpeg_data):
        marker_start = jpeg_data.find(COM_MARKER, pos)
        if marker_start == -1:
            break

        # Read the length of the comment segment
        comment_length = int.from_bytes(
            jpeg_data[marker_start + 2 : marker_start + 4], "big"
        )
        comment_start = marker_start + 4
        comment_end = comment_start + comment_length - 2

        # Extract the comment
        comment = jpeg_data[comment_start:comment_end]
        return comment.decode("utf-8")

    return None


# Example usage
input_image_path = (
    "Restaurant 365.jpeg"
)
output_image_path = (
    "Output.jpeg"
)
comment_text = str(hash_value)

# Add a comment to the JPEG image
add_comment_to_jpeg_com(input_image_path, comment_text, output_image_path)

# Read the comment from the output JPEG image
comment = read_comment_from_jpeg_com(output_image_path)
if comment:
    print("Comment in JPEG image:", comment)
else:
    print("No comment found in the JPEG image.")

#after taking screenshot of "Output.jpeg"
screen_shot="screenshot.jpg"
comment = read_comment_from_jpeg_com(screen_shot)
if comment:
    print("Comment in JPEG image:", comment)
else:
    print("No comment found in the JPEG image. Thus embedding is lost through screenshots.")




