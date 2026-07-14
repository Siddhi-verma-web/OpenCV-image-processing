import cv2

# Read input image
img = cv2.imread("04_Image_Rotation/input.png")

# Rotate image 90 degrees clockwise
rotate_90_clockwise = cv2.rotate(
    img,
    cv2.ROTATE_90_CLOCKWISE
)

# Save 90 degrees clockwise rotated image
cv2.imwrite(
    "04_Image_Rotation/output_90_clockwise.png",
    rotate_90_clockwise
)


# Rotate image 180 degrees
rotate_180 = cv2.rotate(
    img,
    cv2.ROTATE_180
)

# Save 180 degrees rotated image
cv2.imwrite(
    "04_Image_Rotation/output_180.png",
    rotate_180
)


# Rotate image 90 degrees counterclockwise
rotate_90_counterclockwise = cv2.rotate(
    img,
    cv2.ROTATE_90_COUNTERCLOCKWISE
)

# Save 90 degrees counterclockwise rotated image
cv2.imwrite(
    "04_Image_Rotation/output_90_counterclockwise.png",
    rotate_90_counterclockwise
)


# Display all rotated images
cv2.imshow(
    "90 Degree Clockwise",
    rotate_90_clockwise
)

cv2.imshow(
    "180 Degree Rotation",
    rotate_180
)

cv2.imshow(
    "90 Degree Counterclockwise",
    rotate_90_counterclockwise
)

# Wait until any key is pressed
cv2.waitKey(0)

# Close all image windows
cv2.destroyAllWindows()