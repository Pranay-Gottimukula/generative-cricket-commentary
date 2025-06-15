import cv2

def process_for_ocr(picture_path: str) -> str:

    image = cv2.imread(picture_path)
    # image = cv2.imread('data/test_pictures/scorecard.png')
    h, w, _ = image.shape
    scorecard = image[int(h * 0.82):h, 0:w]

    gray = cv2.cvtColor(scorecard, cv2.COLOR_BGR2GRAY)

    filtered = cv2.bilateralFilter(gray, 9, 20, 20)
    
    thresh = cv2.adaptiveThreshold(filtered, 255,
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY_INV,
                                            15, 2)

    inverted = cv2.bitwise_not(thresh)

    resized = cv2.resize(inverted, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    output_path = 'data/test_pictures/scorecard_processed.png'
    cv2.imwrite(output_path, resized)

    return output_path

# cv2.waitKey(0)
# cv2.destroyAllWindows()

