import u12
import smtplib
import datetime
from time import sleep
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587) #second argument is port number
    server.ehlo() #prior to login, establish server connection
    server.starttls()
    server.ehlo()
    server.login("egs.alert@gmail.com", "1Egsgroup!")
    msg=MIMEMultipart()
    msg['From']="egs.alert@gmail.com"
    msg['To']="davidollodart@gmail.com"
    msg['Subject']="Alert"
    with open('log','r') as read_file:
        msg.attach(MIMEText(read_file.read(),'plain'))
    text=msg.as_string()
    server.sendmail("egs.alert@gmail.com", "davidollodart@gmail.com", text)

now=datetime.datetime.now()
dCont=u12.U12(serialNumber=100054654)
while True:
    rough_pressure=-1.*(dCont.eAnalogIn(channel=9,gain=20)['voltage']) # gain specification is only for pre-digitizing the input, which is then divided out. At very low pressures and thus low signal voltages from the unity gain thermocouple pressure transducer controller, where 8 millitorr -> 0.008 V, this will improve the reading, though the sensitivity is still limited
    print(rough_pressure)
    if rough_pressure > 0.1:  #greater than 100 millitorr
        with open('log','a') as append_file:
            append_file.write('p='+str(rough_pressure) + ' torr at time ' + str(now))
            send_email()
    sleep(15)
