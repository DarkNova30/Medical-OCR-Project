# Medical OCR Project

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![Pytesseract](https://img.shields.io/badge/Pytesseract-OCR-red.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.65.2-teal.svg)
![Postman](https://img.shields.io/badge/Postman-Testing-orange.svg)
![RegEx](https://img.shields.io/badge/RegEx-Pattern_Matching-yellow.svg)

## Introduction
This project is a Python-based Optical Character Recognition (OCR) application designed to extract essential information from two types of medical documents: prescription details PDFs and patient details PDFs. It utilizes a combination of image processing and text extraction techniques to parse and retrieve specific data, making the information easily accessible for further use.

## Features
- **Two Document Parsers**: Separate parsers for handling prescription and patient details PDFs.
- **Common Extractor Class**: Converts PDFs to images, applies OpenCV thresholding, and uses Pytesseract for text extraction.
- **RegEx-Based Data Extraction**: Utilizes regular expressions to extract critical information such as names, phone numbers, medical conditions, medicines, directions for medication, and refills.
- **Test-Driven Development (TDD)**: Ensures that the expected outcomes match the actual outcomes through rigorous testing.
- **Code Refactoring**: Applied best practices to simplify and optimize the codebase.
- **Deployment**: Deployed using FastAPI to handle requests, with Postman used for verifying outcomes and results.

## Technology Stack
- **Programming Language**: Python
- **Libraries**: OpenCV, Pytesseract, RegEx, FastAPI
- **Tools**: Postman, TDD
- **Image Processing**: OpenCV for thresholding
- **Text Extraction**: Pytesseract for OCR

## Dataset
The project uses PDF files containing patient details and prescription information as input data. These documents are processed to extract relevant details such as patient names, contact information, medical issues, prescribed medications, and instructions.

## Architecture

### Common Extractor Class
This class is responsible for:
- **Converting PDFs to Images**: Utilizes Python libraries to convert each page of a PDF into an image format.
- **Image Preprocessing**: Applies OpenCV thresholding to enhance the text's visibility in the images.
- **Text Extraction**: Uses Pytesseract to extract text from the processed images.

### Prescription Parser
The prescription parser extracts the following information from the document:
- **Patient Name**: Extracted using specific RegEx patterns.
- **Address**: Captures the address field from the prescription.
- **Medicines**: Identifies prescribed medicines, including dosage and frequency.
- **Directions for Medication**: Extracts the instructions for how the medicines should be taken.
- **Refills**: Identifies the number of refills authorized for the prescription.

### Patient Details Parser
The patient details parser focuses on extracting:
- **Name**: Extracted using RegEx based on common name patterns.
- **Phone Number**: Detects phone numbers in various formats.
- **Vaccine Information**: Extracts details about administered vaccines.
- **Medical Conditions**: Identifies and extracts any listed medical problems or conditions.

## Testing
The application was developed using Test-Driven Development (TDD) to ensure that each component works as expected:
- **Unit Tests**: For individual functions and methods to ensure their accuracy.
- **Integration Tests**: Ensuring that the different parts of the application work together seamlessly.

## Results
The application successfully parses and extracts critical information from both prescription and patient details PDFs, providing structured data that can be used for further analysis or storage. The application was rigorously tested and deployed using FastAPI, with the outputs verified via Postman.

## Deployment
The application was deployed using FastAPI to handle incoming requests and return structured data based on the parsed PDFs. Postman was used extensively during testing to ensure the API performed as expected.
