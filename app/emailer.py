# Python code to illustrate Sending mail with attachments
# from your Gmail account  

# libraries to be imported 
import smtplib
import os
import docx
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Email:

    def __init__(self, to_addr: str = "anthonyqraymundo@gmail.com", file_name: str = "email1.docx"):
        self.from_addr = "noreply.writemyrights@gmail.com"
        self.to_addr = to_addr
        self.file_name = file_name

    def send(self):
        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = self.from_addr

        # storing the receivers email address
        msg['To'] = self.to_addr

        # storing the subject
        msg['Subject'] = "Here's your letter"

        # string to store the body of the mail
        body = "Thanks for using Write my Rights. Our mission is to help you to " \
               "communicate so you can start solving an everyday legal problem. Your " \
               "(free)(premium) letter is attached. Keep fighting the good fight. " \
               "Like what you see? Get 10% off your next premium letter by using the promo code 10OFF."

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Remove HTML tags from file to be sent
        main_dir = os.path.dirname(__file__)
        doc = docx.Document(main_dir + '\\temporary_emails\\' + self.file_name)
        
        for line in doc.paragraphs:
            str_list = line.text.split("\n")
            line.text = ""
        iterate = 0
        for i in str_list:
            if '<br>' in i:
                print(i)
                str_list.remove(i)
            elif '<p id="blurText">' in i:
                print(i)
                print(str_list.index(i))
                str_list.remove(i)
            elif '</p>'in i:
                print(i)
                str_list.remove(i)
            else:
                iterate += 1

        print(str_list)
        for i in str_list:
            doc.add_paragraph(i)
        doc.save(main_dir + '\\temporary_emails\\' + self.file_name)

        # open the file to be sent
        main_dir = os.path.dirname(__file__)
        rel_path = "temporary_emails/" + self.file_name
        abs_file_path = os.path.join(main_dir, rel_path)
        attachment = open(abs_file_path, "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload(attachment.read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % self.file_name)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(self.from_addr, "writemyrights!")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(self.from_addr, self.to_addr, text)

        # terminating the session
        s.quit()

        #delete temporary email
        attachment.close()
        os.remove(abs_file_path)
