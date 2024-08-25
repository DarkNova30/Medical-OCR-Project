import pytest

from backend.src.parser_patient_detaills import PatientDetailsParser


@pytest.fixture()
def doc_1_kathy():
    doc_text = '''17/12/2020
    Patient Medical Record
    Patient Information Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight’
    9264 Ash Dr 95
    New York City, 10005 ‘
    United States Height:
    190
    In Casc of Emergency
    7 ee
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    General Medical History
    Chicken Pox (Varicella): Measies:
    IMMUNE IMMUNE
    Have you had the Hepatitis B vaccination?
    No
    List any Medical Problems (asthma, seizures, headaches}:
    Migraine CO
    '''
    return PatientDetailsParser(doc_text)


@pytest.fixture()
def doc_2_jerry():
    doc_text = '''17/12/2020
Patient Medical Record
Patient Information
Jerry Lucas
(279) 920-8204
4218 Wheeler Ridge Dr
Buffalo, New York, 14201
United States
Birth Date
May 2 1998
Weight:
57
Height:
170
In Case of Emergency
Joe Lucas
Home phone
4218 Wheeler Ridge Dr
Buffalo, New York, 14201
United States
Work phone
General Medical History
Chicken Pox (Varicella):
IMMUNE
Have you had the Hepatitis B vaccination?
Yes
Measles:
NOT IMMUNE
List any Medical Problems (asthma, seizures, headaches):
N/A CO'''
    return PatientDetailsParser(doc_text)


def test_get_patient_name(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_patient_name() == "Kathy Crawford"
    assert doc_2_jerry.get_patient_name() == "Jerry Lucas"


def test_get_phone_no(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_phone_no() == "(737) 988-0851"
    assert doc_2_jerry.get_phone_no() == "(279) 920-8204"


def test_med_prob(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_med_prob() == "Migraine"
    # assert doc_2_jerry.get_med_prob() == "(279) 920-8204"


def test_vacc(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_vaccination() == "No"
    assert doc_2_jerry.get_vaccination() == "Yes"

def test_parse(doc_1_kathy, doc_2_jerry):
    kathy = doc_1_kathy.parse()
    assert kathy['patient_name'] == "Kathy Crawford"
    assert kathy['phone_ number'] == "(737) 988-0851"
    assert kathy['medical_problems'] == "Migraine"
    assert kathy['hepatitis_b_vaccines'] == "No"


