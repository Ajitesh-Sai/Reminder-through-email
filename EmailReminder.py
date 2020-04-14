from datetime import datetime
from datetime import timedelta
import smtplib
from email.message import EmailMessage


email = input("Enter 'from' email id : ")
password = input('Enter password : ')

msg = EmailMessage()
msg['Subject'] = 'Reminder'
msg['From'] = email
msg['To'] = input("Enter 'to' email id : ")

rtime =  int(input('Enter time to be reminded in (in seconds) - '))
print("You will be reminded in {} seconds".format(rtime))


tr = datetime.now()
t = datetime.now()+timedelta(seconds=rtime-1)
while True:
    if datetime.now() == t or datetime.now() > t:
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: #(mail_server, port_number)
            smtp.login(email, password)
            s = str(rtime) + " seconds have passed since " + str(tr) + "\nThe current time is " + str(datetime.now())
            msg.set_content(s)
            smtp.send_message(msg)
            print('Done')
        break







# #while True:
#     #if time.time()==t :
# with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: 
#         # if smtplib.SMTP() is used. Not required if smtplib.SMTP_SSL()
#         # #smtp.ehlo() #sent by client to server to identify itself and initiate SMTP conversation /optional/ 
#         # smtp.starttls() #encrypts traffic / makes connection secure
#         # smtp.ehlo()

#     smtp.login(email, password)
#             #You are now logged in
#     smtp.send_message(msg)
#     #break
    


