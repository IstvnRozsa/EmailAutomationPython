import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json


with open('config/config.json') as json_file:
    data = json.load(json_file)
    
PORT = data["sender"]["port"]
HOST = data["sender"]["host"]
EMAIL_ADDRESS = data["sender"]["email_address"]
PASSWORD = data["sender"]["password"]
    
    
class Receiver:
    def __init__(self, name, email, subject, body, sign):
        self.name = name
        self.email = email
        self.subject = subject
        self.body = body
        self.sign = sign
    
    def send_email(self):
        with smtplib.SMTP(host=HOST, port=PORT) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS, PASSWORD)
            html = '''\
                <html>
                <body>
                    <p>Kedves {name}!</p>
                    <p>
                    {body}
                    </p>
                    <p>
                    {sign}
                    </p>
                </body>
                </html>
                '''.format(name = self.name, body=self.body, sign=self.sign)
            message = MIMEMultipart("alternative")
            message["Subject"] = self.subject
    
            part2 = MIMEText(html, "html")
            message.attach(part2)
            smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message.as_string())
        
        


r = Receiver("Pityu", "pisti.rzsa@gmail.com", "Haligali", "Haligali body", "Üdv.: Pityu")
r.send_email()
