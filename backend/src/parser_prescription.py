import re

from backend.src.parser_generic import MedicalDocParser
doc_text = '''Dr John Smith, M.D
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
virat_text = '''Dr John Smith, M.D

2 Non-Important street,
New York, Phone (900)-a23- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

| Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times'''
class PrescriptionParser (MedicalDocParser):

    def __init__(self,text):
        MedicalDocParser.__init__(self, text)
        self.name = None

    def parse(self):
        return {
            'patient_name' : self.get_field('patient_name'),
            'patient_address': self.get_field('patient_address'),
            'medicines' : self.get_field('medicines'),
            'directions' : self.get_field('directions'),
            'refills' : self.get_field('refills')
        }

    def get_field(self, field_name):

        pattern_dict = {
            'patient_name': {'pattern': 'Name: (.*)Date', 'flags': 0},
            'patient_address': {'pattern': 'Address:(.*)\n', 'flags': 0},
            'medicines': {'pattern': 'Address[^\n]*(.*)Directions', 'flags': re.DOTALL},
            'directions': {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
            'refills': {'pattern': 'Refill: (.*)times', 'flags': re.DOTALL},

        }
        pattern_obj = pattern_dict.get(field_name)
        if pattern_obj:
            matches = re.findall(pattern_obj['pattern'], self.text, flags = pattern_obj['flags'])
            if len(matches) > 0:
                return matches[0].strip()

# refactored all code present below:-
 # if field_name == 'patient_name':
#     pattern = "Name:(.*)Date:"
# elif field_name == 'patient_address':
#     pattern = "Address:(.*)\n"
# elif field_name == 'patient_medicine':
#     pattern = "Address:[^\n]*(.*)Directions:"


# matches = re.findall(pattern, self.text)
# if len(matches) > 0 :
#     return matches[0].strip()

    # def get_name(self):
    #     pattern = "Name:(.*)Date:"
    #     matches = re.findall(pattern, self.text)
    #     if len(matches) > 0 :
    #         return matches[0].strip()
    #
    # def get_add(self):
    #     pattern = "Address:(.*)\n"
    #     matches = re.findall(pattern, self.text)
    #     if len(matches) > 0 :
    #         return matches[0].strip()
    #
    # def get_medicine(self):
    #     pattern = "Address:[^\n]*(.*)Directions:"
    #     matches = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(matches) > 0 :
    #         return matches[0].strip()
    #
    # def get_direction(self ):
    #     pattern = "Directions:[\n](.*)Refill:"
    #     matches = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(matches) > 0 :
    #         return matches[0].strip()
    #
    # def get_refill(self):
    #     pattern = "Refill:(.\d)"
    #     matches = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(matches) > 0 :
    #         return matches[0].strip()


if __name__ == '__main__':

    pp = PrescriptionParser(virat_text)
    print(pp.parse())
    # print(pp.get_name())
    # print(pp.get_add())
    # print(pp.get_medicine())
    # print(pp.name)

