import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("egs.alert@gmail.com", "1Egsgroup!")
msg=MIMEMultipart()
msg['From']="egs.alert@gmail.com"
msg['To']="davidollodart@gmail.com"
msg['Subject']="Alert"
with open('log','r') as read_file:
    msg.attach(MIMEText(read_file.read(),'plain'))
msg.attach(MIMEText(body,'plain'))
text=msg.as_string()
server.sendmail("egs.alert@gmail.com", "davidollodart@gmail.com", text)
