stored_users = {'jason': 'oeros', 'nicole': 'chance'}
accepted = 'Welcome!'
wrong = 'Wrong username or password'
# Python 2:
import urllib
import smtplib, ssl
import smtplib
import email
from email.mime.multipart import MIMEMultipart
#from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText

# Python 3:
import urllib.parse

def add_user():
    print('Creating user, please choose username and password')
    username = input('Username: ')
    password = input('Password: ')
    if stored_users.get(username):
        print('Username already exiss')
    else:
        stored_users[username] = password

def login():
    print('Logging in')
    username = input('Username: ')
    password = input('Password: ')
    if stored_users.get(username) == password:
        return True
    else:
        print(False)

trials = 0
add_user()
while trials < 3:
    check = login()
    if check:
        print(accepted)
        day_log = str(input("Enter the day:"))
        time_log = float(input("Enter logged number of hours:"))
        getVars = {'var1': str(day_log), 'var2': float(time_log)}
        approval_var = {'var1': str(day_log), 'var2': float(time_log), 'action':'approve'}
        reject_var = {'var1': str(day_log), 'var2': float(time_log), 'action' : 'reject'}
        url = 'https://docs.google.com/forms/d/<form_id>/formResponse'
        # Python 2:
        #print(url + urllib.urlencode(getVars))
        # Python 3:
        subject_link = url + urllib.parse.urlencode(getVars)
        approval_link = '<a href="' + url + urllib.parse.urlencode(approval_var) + '" style="padding: 6px; border-radius:20px; background-color:green" >Approve</a> <br>'
        reject_link = '<a href="' + url + urllib.parse.urlencode(reject_var) + '" style="padding: 6px; border-radius:20px; background-color:red" >reject</a> <br>'
        fromaddr = str(input("Enter your email ID:"))
        toaddr = str(input("Enter recepient's email ID:"))
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Python email"
        body = str(subject_link) + '<br><br>' + approval_link + '<br><br>' + reject_link
        msg.attach(MIMEText(body, 'html'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        usrn=str(input("Enter your Gmail username:"))
        pswr=str(input("Enter password:"))
        server.login(usrn, pswr)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        print('Email Sent!')
        break
     
    else:
        print(wrong)








