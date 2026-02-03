import cv2

# Read image
img = cv2.imread("opencv.jpg")

# Check if image was loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Resize
    resized = cv2.resize(img, (400, 300))

    # Convert to grayscale
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blur, 100, 200)

    # Display
    cv2.imshow("Original", img)
    cv2.imshow("Resized", resized)
    cv2.imshow("Gray", gray)
    cv2.imshow("Blur", blur)
    cv2.imshow("Edges", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
