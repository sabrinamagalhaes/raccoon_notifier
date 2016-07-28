# Notifier

## USAGE

### Include repository

#### virtualenv
Include at ```requirements.txt```:
```python
git+https://github.com/devraccoon/raccoon_notifier
```
#### setup.py

```python
setup(
...
install_requires=[
...
  'raccoon-notifier',
...
],
...
dependency_links=['https://github.com/devraccoon/raccoon_notifier/tarball/master#egg=raccoon-notifier'],
...
)
```

## Email Sender

* Module to easily send email using **smtplib**
* Unify email model
* Possible to send attachment

**IMPORTANT:** Email sender uses Gmail as default.

### Send email
```python
from raccoon_email.email_sender import EmailSender

sender = EmailSender('Software Name', 'example@gmail.com', 'password')
sender.add_attachment(file_name) # Optional
sender.send('to@gmail.com', 'Example', 'Body')
```

#### Arguments

> EmailSender(name, email, password)
* **name**: Sender's name
* **email**: Sender's email
* **password**: Sender's password

> EmailSender.add_attachment(attach)

* **attach**: File name and path

> EmailSender.send(toaddrs, subject, body)
* **toaddrs**: _list_ of recipients emails
* **subject**: email subject
* **body**: message to be sent


## SMS Sender

  * Module to easily send SMS using **Plivo**
  * Unify SMS model

### Send SMS

```python
from raccoon_email.sms_sender import SMSSender

sender = EmailSender('Software Name', 'example@gmail.com', 'password')
sender.add_attachment(file_name) # Optional
sender.send('to@gmail.com', 'Example', 'Body')
```
