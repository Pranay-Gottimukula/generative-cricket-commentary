import sys
import os
import pytesseract
import cv2

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.picture_utils import process_for_ocr

output = process_for_ocr('data/test_pictures/scorecard.png')

img = cv2.imread('data/test_pictures/scorecard.png')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img_rgb, config=config)

print("Extracted Text:\n", text)