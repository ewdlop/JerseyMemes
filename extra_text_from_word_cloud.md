from PIL import Image
import pytesseract

# Path to the Tesseract executable (only needed if it's not in your PATH)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    # Open the image using Pillow
    img = Image.open(image_path)
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(img)
    return text

# Example usage
image_path = 'path_to_your_word_cloud_image.png'
extracted_text = extract_text_from_image(image_path)
print(extracted_text)
