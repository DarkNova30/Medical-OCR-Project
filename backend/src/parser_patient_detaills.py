import re

from backend.src.parser_generic import MedicalDocParser


class PatientDetailsParser(MedicalDocParser):

    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_patient_name(),
            'phone_ number': self.get_phone_no(),
            'medical_problems': self.get_med_prob(),
            'hepatitis_b_vaccines': self.get_vaccination(),
        }

    def remove_noise_from_name(self, name):
        name = name.replace("Birth Date", "").strip()
        pattern = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(pattern, name)

        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, "").strip()
        return name

    def get_patient_name(self):
        pattern = "Patient Information(.*?)\(\d{3}\)"

        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            name = self.remove_noise_from_name(matches[0])
        return name

    def get_phone_no(self):
        pattern = "Patient Information.*?(\(\d{3}\) \d{3}-\d{4})"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        matches = matches[0]
        if matches:
            phno = self.remove_noise_from_name(matches)
        return phno

    def get_med_prob(self):
        pattern = "List any Medical Problems .*?:(.*)"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()

    def get_vaccination(self):
        pattern = "Have you had the Hepatitis B vaccination?.*(No|Yes)"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()

if __name__ == "__main__":
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

    pdp_jerry = PatientDetailsParser(doc_text)
    print(pdp_jerry.parse())

    doc_text2 = '''17/12/2020
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
    pdp_kathy = PatientDetailsParser(doc_text2)
    print(pdp_kathy.parse())