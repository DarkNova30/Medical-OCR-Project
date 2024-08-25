from backend.src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_1_maria():
    document_text_1 = '''Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-121-2222

    Name: Marta Sharapova Date: 2/11/2022

    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg
    Lialda 2.4 gram

    Directions:
    Prednisone, Taper 5 mg every 3 days,

    Finish in 2.5 weeks -
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times'''
    return PrescriptionParser(document_text_1)
@pytest.fixture()
def doc_2_virat():
    document_text_2 = '''Dr John Smith, M.D

2 Non-Important street,
New York, Phone (900)-a23- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

| Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times'''
    return PrescriptionParser(document_text_2)


@pytest.fixture()
def doc_3_empty():
    return PrescriptionParser("")


def test_get_name(doc_1_maria,doc_2_virat,doc_3_empty):
    assert doc_1_maria.get_field('patient_name') == 'Marta Sharapova'
    assert doc_2_virat.get_field('patient_name') == 'Virat Kohli'
    assert doc_3_empty.get_field('patient_name') == None


def test_get_add(doc_1_maria,doc_2_virat,doc_3_empty):

    assert doc_1_maria.get_field('patient_address') == '9 tennis court, new Russia, DC'
    assert doc_2_virat.get_field("patient_address") == '2 cricket blvd, New Delhi'
    assert doc_3_empty.get_field("patient_address") == None


def test_parse(doc_1_maria,doc_2_virat,doc_3_empty):
    record_maria = doc_1_maria.parse()
    record_virat = doc_2_virat.parse()
    record_empty = doc_3_empty.parse()
    assert record_maria["patient_name"] == "Marta Sharapova"
    assert record_maria["patient_address"] == "9 tennis court, new Russia, DC"
    assert record_virat == {'patient_name': 'Virat Kohli', 'patient_address': '2 cricket blvd, New Delhi', 'medicines': '| Omeprazole 40 mg', 'directions': 'Use two tablets daily for three months', 'refills': '3'}
    assert record_empty == {'patient_name': None,
                            'patient_address': None,
                            'medicines': None,
                            'directions': None,
                            'refills': None}

document_text_1 = '''Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-121-2222

Name: Marta Sharapova Date: 2/11/2022

Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram

Directions:
Prednisone, Taper 5 mg every 3 days,

Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month

Refill: 2 times'''

document_text_2 = '''Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-121-2222

Name: kirat vohli Date: 2/11/2022

Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram

Directions:
Prednisone, Taper 5 mg every 3 days,

Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month

Refill: 2 times'''