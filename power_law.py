import cv2 # To read the image that will be used
import numpy as np

def power_law_transform(image, gamma):
    # Normalize pixel intensities to the range [0, 1]
    image_normalized = image / 255.0
    # Perform power law transformation
    image_transformed = np.power(image_normalized, gamma)
    # Revert normalization to return to the range [0, 255]
    image_transformed = np.uint8(image_transformed * 255)
    return image_transformed

# Read the image
image = cv2.imread('test/raw.jpg',cv2.IMREAD_GRAYSCALE)
# Set the gamma value as needed
gamma = 0.5
# Apply power law transformation
transformed_image = power_law_transform(image, gamma)
# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()