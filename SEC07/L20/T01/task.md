# Email Script

## What You'll Learn

Build a Python script that sends emails programmatically using the smtplib module, email templates, and SMTP authentication.

## Concept Overview

Python can automate email sending for notifications, reports, or communication workflows. This involves connecting to an SMTP server (like Gmail's), authenticating with credentials, and sending formatted email messages.

This exercise demonstrates practical scripting: reading files, using templates to customize content, and interacting with external services through standard protocols. These skills are valuable for automation tasks, notifications, and integration with other systems.

## Key Concepts

### SMTP Protocol

SMTP (Simple Mail Transfer Protocol) is the standard for sending emails:

```python
import smtplib

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()        # Identify to server
    smtp.starttls()    # Encrypt connection
    smtp.login(email, password)  # Authenticate
    smtp.send_message(email_obj)
```

### Email Message Construction

Use the email module to create properly formatted messages:

```python
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Sender Name'
email['to'] = 'recipient@example.com'
email['subject'] = 'Subject Line'
email.set_content('Message body', 'html')
```

### Template Substitution

Use string templates to customize email content:

```python
from string import Template
from pathlib import Path

template = Template(Path('template.html').read_text())
personalized = template.substitute({'name': 'John'})
```

### Security Considerations

Never hardcode credentials:
- Use environment variables
- Use app-specific passwords
- Handle credentials securely

## Example

```python
import smtplib
from email.message import EmailMessage

def send_notification(recipient, subject, body):
    email = EmailMessage()
    email['from'] = 'notifications@example.com'
    email['to'] = recipient
    email['subject'] = subject
    email.set_content(body)
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('your_email@gmail.com', 'app_password')
        smtp.send_message(email)
        print(f"Email sent to {recipient}")

# Usage
send_notification(
    'user@example.com',
    'Daily Report',
    'Your daily report is ready.'
)
```

## Your Task

Study how to send emails programmatically using Python's smtplib and email modules. Understand SMTP authentication, email message construction, template usage, and how to securely handle credentials. Learn how Python can automate communication workflows.
