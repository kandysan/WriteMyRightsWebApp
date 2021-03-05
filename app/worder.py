import docx
import os

class WordDoc:
    def __init__(self, input_dict: dict):
        self.input_dict = input_dict

    def create(self):
        mydoc = docx.Document()
        for key in self.input_dict:
            mydoc.add_paragraph(self.input_dict[key])
        main_dir = os.path.dirname(__file__)
        rel_path = "temporary_emails/" + self.input_dict['name']
        abs_file_path = os.path.join(main_dir, rel_path)
        mydoc.save(abs_file_path + ".docx")
