Python's [smtplib](https://docs.python.org/3/library/smtplib.html) and [email](https://docs.python.org/3/library/email.html) modules allow you to send emails programmatically. This is useful for automated notifications, reports, or communication systems.

### Creating an Email Message

The `EmailMessage` object stores the email headers and the email body in one place.
Use `EmailMessage()` to create an email object and set headers:

```python
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Sender Name'
email['to'] = 'recipient@example.com'
email['subject'] = 'Hello'
```

Set the email content using `set_content()`:

```python
email.set_content('This is a plain text email')
```

For HTML content, pass `'html'` as the second argument:

```python
email.set_content('<h1>Hello</h1>', 'html')
```

### HTML Templates with Dynamic Values


The `Template` class from the `string` module allows you to create templates with placeholders. In this task, the HTML template is stored in `template.html` in the task folder.

`Path('template.html').read_text()` reads the contents of the HTML file as a string, and `Template(...)` turns that string into a template object.

The `substitute()` method replaces placeholders in the template with actual values. For example, if the template contains `name`, it can be replaced with `'Alice'`.

```python
from string import Template
from pathlib import Path

# Read HTML file
html = Template(Path('template.html').read_text())

# Substitute values into the template
content = html.substitute({'name': 'Alice', 'amount': '1000'})
```

Then set it as the email content:

```python
email.set_content(content, 'html')
```

### Connecting to an SMTP Server

To send an email, your script needs to connect to an SMTP server.

SMTP stands for **Simple Mail Transfer Protocol**. It is the standard protocol used to send emails from a client to a mail server.

In Python, this connection is usually created with `smtplib`, and the result is an `smtp` object. You call methods on this object to communicate with the server and send the email.

Common SMTP actions include:
- connecting to the server with `ehlo()`
- starting a secure connection with `starttls()`
- logging in with your email credentials using `login()`
- sending the prepared email message using `send_message()`

For more complete examples of building and sending messages, see the [email examples documentation](https://docs.python.org/3/library/email.examples.html).

For example, an SMTP connection is created by providing a server address and a port number:

```python
import smtplib

with smtplib.SMTP(host='smtp.example.com', port=587) as smtp:
    pass
```
Here, `smtp` is the connection object. Its methods are used to interact with the mail server.

### Running the script outside the tests

If you run this script yourself, make sure you replace the placeholders in `smtp.login(...)` with real credentials:

```python
smtp.login('your_email@gmail.com', 'your_password')
```

If you leave the email address and password placeholders unchanged, the SMTP server will reject the login and raise `smtplib.SMTPAuthenticationError`.

If you use Gmail, your regular password may not work for SMTP. In that case, you may need to [use an App Password](https://support.google.com/mail/answer/185833) instead.