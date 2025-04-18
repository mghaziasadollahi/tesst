# Optical Character Recognition (OCR) with Tesseract
# Overview

This project implements Optical Character Recognition (OCR) using Python with Tesseract (pytesseract) and OpenCV. It extracts text from images with support for French language characters and visualizes the recognition results with bounding boxes.
# Features

    Text extraction from images using Tesseract OCR

    Support for French language characters (including accented letters)

    Image preprocessing with OpenCV:

        Grayscale conversion

        Gaussian blur

        Thresholding

    Visualization of recognized text with bounding boxes

    Confidence-based filtering of OCR results

# Output

The script provides:

    Raw OCR text output

    Processed OCR text after image preprocessing

    Visual output showing:

        Bounding boxes around recognized text

        Recognized text labels

        Confidence-filtered results (only >80% confidence)

# Image Processing Pipeline

    Original image loading

    Grayscale conversion

    Gaussian blur (5x5 kernel)

    Binary thresholding (inverted)

    OCR on both original and processed images

# Customization

To adapt for different use cases:

    Change input filename in PIL.Image.open() and cv2.imread()

    Modify configuration string for different languages or character sets

    Adjust confidence threshold (currently 80)

    Change image preprocessing parameters as needed

# Notes

    Performance may vary based on image quality

    For best results, use clear images with good contrast

    The current version is optimized for French text but can be adapted for other languages
