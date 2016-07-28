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
from raccoon_notifier.email_sender import EmailSender

sender = EmailSender('Software Name', 'example@gmail.com', 'password')
sender.add_attachment(file_name) # Optional
sender.send(['to@gmail.com'], 'Example', 'Body')
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

  * Module to easily send SMS using **[Plivo API](https://www.plivo.com/)**
  * Unify SMS model

### Send SMS

```python
from raccoon_notifier.sms_sender import SMSSender

sender = SMSSender('Software Name', 'AuthID', 'AuthToken')
sender.send(['5516111111111'], "Hello, it's me")
```

### Arguments

> SMSSender(name, auth_id, auth_token)

* **name**: Software name (appear before message)
* **auth_id**: Plivo AuthID
* **auth_token**: Plivo Auth Token

> SMSSender.send(phones, message)

* **phones**: _list_ of recipients phones
* **message**: message to be sent
