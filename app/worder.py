# creating letter template in a form of a word document
import docx
import os


class WordDoc:
    def __init__(self, input_str: str, input_dict: dict):
        self.input_dict = input_dict
        self.input_str = input_str

    def create(self):
        mydoc = docx.Document()
        mydoc.add_paragraph(self.input_str)
        main_dir = os.path.dirname(__file__)
        rel_path = "temporary_emails/" + self.input_dict['name']
        abs_file_path = os.path.join(main_dir, rel_path)
        print(abs_file_path)
        mydoc.save("%s%s" %(abs_file_path, ".docx"))
