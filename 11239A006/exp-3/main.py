import cv2

# Read image
img = cv2.imread("image.jpg")

# Check if image was loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Display image
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
