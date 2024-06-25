# Water_marking_system
Detecting and flagging AI generated text, images and audio

## Team
Kshitij Koushik Kota - [https://github.com/kshitijkota](https://github.com/kshitijkota) <br/>
Pranav Hemanth - [https://github.com/Pranavh-2004](https://github.com/Pranavh-2004) <br/>
Pranav Rajesh Narayan - [https://github.com/pranav-rn](https://github.com/pranav-rn) <br/>
Roshini Ramesh - [https://github.com/roshr22](https://github.com/roshr22) <br/>
Sampriti Saha - [https://github.com/sampritisaha](https://github.com/Sampriti2803) (Honorary member) <br/>

## Introduction
Track: AI-Media Detection and Flagging <br/>
Topic: Marking AI Generated Images <br/>

In the present-day world of AI-generated media, one of the major problems lies in digital forgery ,deepfakes, copyright and plagiarism, the need for a trusted, immutable source of verifying whether the image is AI generated or not becomes essential. <br/>

## Problem Statement
AI-generated images have become a significant source of misinformation, posing challenges for authenticity verification. Current watermarking methods are inadequate, lacking the ability to effectively mark AI-generated images from their inception. This deficiency allows for the dissemination of altered or misleading content, undermining trust in digital media.


## Objective
Our objective is to develop a robust watermarking system for AI-generated images that can be embedded at the image's inception. This system will enable any individual on the internet to verify if an AI-generated image is unaltered or has been tampered with.

## Scope
The watermarking system will focus on embedding imperceptible yet robust watermarks into AI-generated images. The system will be designed to withstand common image manipulations and will be compatible with a wide range of image formats. Verification of watermarked images will be accessible through a user-friendly online platform, ensuring widespread usability.

## Key Features
Embedding watermarks into AI-generated images at the point of creation.
Watermarks must be imperceptible to the human eye yet robust against tampering.
Compatibility with various image formats and resolutions.
Easy verification process accessible to any internet user.
Scalable and adaptable to future advancements in AI and image processing technologies.

## Beneficiaries
Content creators and artists who want to protect their original work from unauthorized use.
Media organizations and journalists seeking to verify the authenticity of images used in news reporting.
Social media platforms and online communities aiming to curb the spread of misinformation.
General internet users looking to verify the authenticity of images encountered online.

## Outcome
The development of an effective watermarking system for AI-generated images will contribute to combating misinformation, protecting intellectual property rights, and fostering trust in digital media.

## Drawbacks of current watermarking methods
1. **Ease of Removal**: Some watermarking techniques are easily removable by advanced AI algorithms, diminishing their effectiveness in protecting the image's authenticity.
2. **Impact on Image Quality**: Watermarks can degrade the quality of the image, especially if they are large or intrusive, which may be undesirable for certain applications.
3. **Limited Robustness**: Some watermarking methods are not robust enough to withstand common image processing operations such as compression, resizing, or filtering, reducing their effectiveness in protecting the image's integrity.
4. **Detection Complexity**: Verifying the presence and authenticity of watermarks in images can be computationally intensive and may require specialized tools or algorithms, making it challenging to implement at scale.
5. **Limited Compatibility**: Watermarking techniques may not be compatible with all types of images or may require specific software or hardware support, limiting their applicability in certain contexts.
6. **Overhead for Content Creators**: Applying watermarks to images can be time-consuming and may require additional resources, especially for large volumes of images.
7. **User Experience**: Watermarks can interfere with the viewing experience of the image, especially if they are distracting or cover important parts of the image.
8. **Risk of Alteration**: Watermarks themselves can be altered or removed, leading to potential disputes over the ownership or authenticity of the image.

Addressing these drawbacks requires the development of more robust and secure watermarking techniques specifically tailored to AI-generated images, taking into account their unique characteristics and vulnerabilities.

## Solution

**Solution Overview:**
To address the challenge of verifying the authenticity of AI-generated images, we propose a two-step approach leveraging machine learning (ML) and steganography techniques. 

1. **Object Identification and Attention Algorithm:**
   - Utilize a machine learning model to identify different objects in the image, such as dogs, landscapes, humans, etc.
   - Develop an attention algorithm that determines the most critical parts of an image by first identifying the image's category (e.g., dog, landscape) and then segmenting the image into its constituent parts (e.g., legs, body, tail, face).

2. **Steganography Embedding with Hashing:**
   - Generate a unique perceptual hash (phash) for each image using the SHA256 hashing algorithm.
   - Embed the phash into the identified critical parts of the image using bit manipulation techniques, ensuring that the hash is imperceptible to the human eye.
   - The embedded hash serves as a watermark that can be used to verify the authenticity of the image.

**Detailed Steps:**
1. **Object Identification:** Train an ML model to identify objects in images using a dataset of labeled images. Use techniques such as convolutional neural networks (CNNs) for this task.

2. **Attention Algorithm:** Develop an attention algorithm that takes the identified objects and determines the most critical parts of the image. This can be achieved by training a model to recognize important features based on the image category and object segmentation.

3. **Steganography Embedding:** 
   - Generate a unique phash for each image using the SHA256 hashing algorithm.
   - Use the attention algorithm to identify the coordinates of the critical parts of the image.
   - Embed the phash into the identified coordinates using bit manipulation techniques (e.g., LSB embedding).

4. **Verification Process:**
   - Any individual can extract the embedded phash from the image using the same coordinates and bit manipulation techniques. <br/>
   - Compute the phash of the image independently using the SHA256 hashing algorithm. <br/>
   - If the extracted phash and the independently computed phash match, the image is deemed unaltered. <br/>

**Benefits:**
- Provides a robust method for verifying the authenticity of AI-generated images. <br/>
- Ensures that the watermark is imperceptible and resistant to tampering. <br/>
- Enables independent verification by any individual without requiring specialized tools or knowledge. <br/>

**Outcome:**
By implementing this solution, we can enhance trust and transparency in digital media by enabling individuals to verify the authenticity of images, thereby combating misinformation and ensuring the integrity of visual content.

## References and Similar research
https://about.fb.com/news/2024/02/labeling-ai-generated-images-on-facebook-instagram-and-threads/ (Recommended further reading on Meta's Solution - Stable Singnatures) <br/>
https://www.technologyreview.com/2023/08/29/1078620/google-deepmind-has-launched-a-watermarking-tool-for-ai-generated-images/ <br/>
https://www.theverge.com/2024/2/6/24063954/ai-watermarks-dalle3-openai-content-credentials <br/>
