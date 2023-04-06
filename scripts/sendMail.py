import smtplib

def send_mail_to_user(userMail, userName, registration_number, voilationType, amount):
  sender_mail = 'sender@gmail.com'    
  receivers_mail = [userMail]    
  message = """From: From Person %s  
  To:  %s  
  Subject: Sending Mail for Challan.  
  body :
  Hello %s , your vechile with registration number %s
  is detected under %s detection ,
  Kindly pay the requested chalan amount %d
  """%(sender_mail, userMail, userName, registration_number, voilationType, amount)    
  try:    
    password = input('Enter the password');    
    smtpObj = smtplib.SMTP('gmail.com',587)    
    smtpObj.login(sender_mail,password)    
    smtpObj.sendmail(sender_mail, receivers_mail, message)    
    print("Successfully sent email")    
  except Exception:    
    print("Error: unable to send email")    