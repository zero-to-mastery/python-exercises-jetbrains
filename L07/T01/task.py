import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

# Read the HTML template from a file
html = Template(Path('template.html').read_text())
email = EmailMessage()

email['from'] = 'Andrei Neagoie'
email['to'] = '<to email address>'
email['subject'] = 'You won 1,000,000 dollars!'

# Call a method on the `email` object to set the HTML body of the email
# and use substitute() to set name to 'TinTin' in the HTML template
email.set_content(html.substitute({'name': 'TinTin'}), 'html')

# Connect to 'smtp.gmail.com' using port 587
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  # Connect to the server by calling a method on the smtp object
  smtp.ehlo()

  # Start a secure connection by calling a method on the smtp object
  smtp.starttls()

  smtp.login('<your email address>', '<your password>')
  smtp.send_message(email)
  print('all good boss!')