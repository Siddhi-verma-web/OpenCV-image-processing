# 📖 Image Reading using OpenCV

## 📌 Overview

This project demonstrates how to read and display an image using OpenCV in Python.

Image reading is the first step in almost every simage processing and computer vision application. OpenCV provides the `cv2.imread()` function to load an image into memory for further processing.

---

## ✨ Features

- Read an image using OpenCV
- Display the image in a window
- Print image type
- Print image dimensions (height, width, channels)

---

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy

---

## 📂 Project Files

- `image_read.py` – Python implementation
- `input.png` – Input image
- `README.md` – Project documentation

---

## ▶️ How to Run

1. Install the required libraries:
   ```bash
   pip install opencv-python numpy
   ```

2. Run the program:
   ```bash
   python image_read.py
   ```

---

## 🖼️ Input Image

![Input Image](input.png)

---

## 📚 Code Explanation

- `cv2.imread()` loads the image from the file.
- `type(img)` displays the image object type.
- `img.shape` returns the image dimensions.
- `cv2.imshow()` displays the image.
- `cv2.waitKey(0)` waits until a key is pressed.
- `cv2.destroyAllWindows()` closes the image window.

---

## 🎯 Learning Outcome

Through this implementation, I learned how OpenCV reads images from storage and prepares them for further image processing tasks. This is one of the most fundamental concepts in Computer Vision.

---

⭐ This project is part of my **OpenCV Image Processing using Python** learning journey.