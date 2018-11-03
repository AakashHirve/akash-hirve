# Send emails via Gmail SMTP server

from smtplib import SMTP
from smtplib import SMTPAuthenticationError
from smtplib import SMTPException

try:
  server = SMTP('smtp.gmail.com', 587)
  server.set_debuglevel(True)
  message = "Hello World!"

  server.ehlo()                   # Determines if server supports TLS encryption
  if server.has_extn('STARTTLS'): # Check the results of ehlo(), if server supports service extension TLS 
        server.starttls()         # Puts the connection to TLS mode
        server.ehlo()
  server.login('sender@email.com', 'sender_password')

  response = server.sendmail("sender_email", "recepient_email", message)
  print("This is response "+str(response))
except SMTPException as ex:
  print("SMTP Exception: \n",str(ex))
finally:
  server.quit()
