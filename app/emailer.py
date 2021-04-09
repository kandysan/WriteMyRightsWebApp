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

    def __init__(self, to_addr: str = "letters@writemyrights.com", file_name: str = "email1.docx"):
        self.from_addr = "letters@writemyrights.com"
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
               " letter is attached. Keep fighting the good fight. " \
               "Like what you see? Get 10% off your next premium letter by using the promo code 10OFF."

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        main_dir = os.path.dirname(__file__)
        print(main_dir)
        rel_path = "temporary_emails/" + self.file_name
        abs_file_path = os.path.join(main_dir, rel_path)
        print(abs_file_path)
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
        s = smtplib.SMTP('smtp.hostinger.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(self.from_addr, "Totempole85%")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(self.from_addr, self.to_addr, text)

        # terminating the session
        s.quit()

        #delete temporary email
        attachment.close()
        os.remove(abs_file_path)
