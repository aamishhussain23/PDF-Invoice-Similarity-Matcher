# PDF Invoice Similarity Matcher

This project is a Python program that compares PDF invoices and finds the most similar one from a database. This is useful for automatically categorizing and matching incoming invoices.

## Requirements

- Python 3.x
- PyPDF2
- scikit-learn
- numpy
- pdf2image
- pillow
- scikit-image

## Installation

First, make sure you have Python installed on your system. Then, install the required libraries using pip:

```bash
pip install PyPDF2 scikit-learn numpy pdf2image pillow scikit-image
```

## Additional Setup
To convert PDF files to images, you need to have the ```poppler library``` installed on your system.

## On Windows:
- Download poppler for Windows [Download](https://github.com/oschwartz10612/poppler-windows/releases/download/v24.07.0-0/Release-24.07.0-0.zip).
- Extract the downloaded zip file.
- Add the path to the ```bin``` directory ```(e.g., C:\path\to\poppler-xx\bin)``` to your system's PATH environment variable.

## On macOS:
- Install poppler using Homebrew:
```bash
    brew install poppler
```

## How to Run
- Place your PDF invoices ```(invoice1.pdf, invoice2.pdf, etc.)``` in the pdfs directory.
- Modify the ```input_invoice``` variable in the main function to point to the invoice you want to compare.

## Run the script using the following command:
```bash
    python main.py
```

## Conclusion
This program is designed to efficiently compare PDF invoices and identify the most similar one from a database.

- Contributions to the project are welcome.
- Feel free to use this code as a foundation for developing your own invoice matching system.
