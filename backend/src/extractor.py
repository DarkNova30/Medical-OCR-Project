from util import preprocess
from pdf2image import convert_from_path
import pytesseract
from parser_prescription import PrescriptionParser
from parser_patient_detaills import PatientDetailsParser

pop_path = '/opt/homebrew/Cellar/poppler/24.04.0/bin'


def extract(file_path, file_format):
    # extract text from pdf files
    pages = convert_from_path(file_path, poppler_path=pop_path)  # converts pdf to image
    document_text = ""
    processed_image = preprocess(pages[0])
    text = pytesseract.image_to_string(processed_image, lang='eng')
    document_text = '\n' + text
    # for page in pages:
    #     processed_image = preprocess(page)
    #     text = pytesseract.image_to_string(processed_image, lang='eng')
    #     document_text = '\n' + text
    # print (document_text)

    # extracting fields from text
    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()

    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
    else :
        raise Exception(f"Invalid document format: {file_format}")
    return extracted_data


if __name__ == '__main__':
    data = extract('../resources/patient_details/pd2.pdf', 'patient_details')

    print(data)
