import cv2
import os

def detect_cracks(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur to reduce noise
    # Edge detection
    edges = cv2.Canny(blur, 50, 150)

    # Thresholding
    _, thresh = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY)

    return thresh

input_folder = "sample_images"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    path = os.path.join(input_folder, file)
    result = detect_cracks(path)

    output_path = os.path.join(output_folder, file)
    cv2.imwrite(output_path, result)

print("Processing complete. Check output folder.")