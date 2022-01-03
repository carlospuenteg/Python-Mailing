import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#------------WITH FILE------------
from email.mime.base import MIMEBase
from email import encoders
import os

# https://techexpert.tips/es/python-es/python-enviar-correo-electronico-usando-gmail/

################################################################

def info():
    print("\nIf you don't trues this process, you can use a secondary google account")
    print("\n1.1. If your google account doesn't have 2 step verification, get if here: https://myaccount.google.com/u/2/signinoptions/two-step-verification/enroll-welcome")
    print("\n1.2. If it does, go to 'https://myaccount.google.com/u/4/apppasswords' and create a new app password for mail and for any device. Then COPY IT AND SAVE IT ")
    print("\n2. Go to https://accounts.google.com/DisplayUnlockCaptcha and allow external access to your google account")
    print("\n3. ALL DONE!\n")
    menu()

################################################################

def sendMail():
    while True:
        username = input("Your adress (E.g. sender@gmail.com): ").strip()
        if ("@gmail.com" in username): 
            smtpHost = "smtp.gmail.com".strip
            break
        elif ("@outlook.com" in username): 
            smtpHost = "smtp.office365.com" #https://support.microsoft.com/es-es/office/configuraci%C3%B3n-pop-imap-y-smtp-8361e398-8af4-4e97-b147-6c6c4ac95353
            break
        else:
            print("Invalid adress")

    while True:
        password = input("Your app password (E.g. xacdhdbnmadsiags): ").strip()
        if (len(password) == 16): 
            smtpHost = "smtp.gmail.com"
            break
    while True:
        mail_from = input("From (E.g. sender@gmail.com): ").strip() 
        if (mail_from != ""):
            break

    while True:
        mail_to = input("To (E.g. receiver@gmail.com): ").strip()
        if (mail_from != ""):
            break

    while True:
        mail_subject = input("Subject (E.g. TEST SUBJECT): ").strip()
        if (mail_from != ""):
            break

    while True:
        mail_body = input("Body (E.g. This is a test body): ").strip()
        if (mail_from != ""):
            break

    while True:
        fileChoice = input("Do you want to attach the file in the 'attachment' folder? (Y/n): ").lower()
        if (fileChoice=="y"): 
            if (os.listdir("attachment")):
                wFile = True
                mail_attachment="attachment/"+"".join(x for x in os.listdir("attachment") if x!="example.png")
                mail_attachment_name="profile.jpeg"
                break
            else:
                print("There is no attached file. Put it in the 'attachment' folder")
        elif(fileChoice=="n"): 
            wFile = False
            break
        else:
            print("Invalid option")

    try:
        mimemsg = MIMEMultipart()
        mimemsg['From']=mail_from
        mimemsg['To']=mail_to
        mimemsg['Subject']=mail_subject
        mimemsg.attach(MIMEText(mail_body, 'plain'))

        if (wFile):
            with open(mail_attachment, "rb") as attachment:
                mimefile = MIMEBase('application', 'octet-stream')
                mimefile.set_payload((attachment).read())
                encoders.encode_base64(mimefile)
                mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
                mimemsg.attach(mimefile)
            
        connection = smtplib.SMTP(host=smtpHost, port=587)
        connection.starttls()
        connection.login(username,password)
        connection.send_message(mimemsg)
        connection.quit()
    except:
        print("Unable to send the message")

################################################################

def menu():
    print("\n0. Get Started")
    print("1. Send an email")
    op = input("\nOption: ")

    if (op == "0"):
        info()
    elif (op == "1"):
        sendMail()
    else:
        print("Invalid option")

################################################################

menu()