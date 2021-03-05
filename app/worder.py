import docx

class WordDoc:

    def __init__(self, input_dict: dict):
        self.input_dict = input_dict

    def create(self):
        mydoc = docx.Document()
        for key in self.input_dict:
            mydoc.add_paragraph(key)
        mydoc.save("")

