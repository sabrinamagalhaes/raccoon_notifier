# coding=utf-8

import logging
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender(object):

    def __init__(self, name, user, pwd):
        self.debug = False
        self.gmail_pwd = pwd
        self.gmail_user = user
        self.from_addr = name
        self.header = '<html><body>'
        self.footer = '<hr><font size="2" color="gray">Essa é uma mensagem automática de <a href="http://raccoon.ag">Raccoon Marketing Digital</a>.<br>Por favor, não responda este e-mail.</font></body></html>'
        self.attachment = []
        self.server = None

    def add_attachment(self, attach):
        self.attachment.append(attach)

    def send(self, toaddrs, subject, body, footer=True):
        try:
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
        except socket.gaierror, e:
            logging.error(e)
        self.server.ehlo()
        self.server.starttls()
        try:
            self.server.login(self.gmail_user, self.gmail_pwd)
        except smtplib.SMTPAuthenticationError:
            logging.error('Authentication Error: email or password incorrect')

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.from_addr

        if footer:
            header = MIMEText(self.header, 'html')
            msg.attach(header)

        try:
            msg1 = MIMEText(body, 'plain', 'utf-8')
            msg.attach(msg1)
        except UnicodeEncodeError:
            logging.error('Unicode error sending email')

        if footer:
            html_msg = MIMEText(self.footer, 'html')
            msg.attach(html_msg)

        for attachment_file in self.attachment:
            try:
                file_path = file(attachment_file)
                attachment = MIMEText(file_path.read())
                attachment.add_header('Content-Disposition', 'attachment', filename=attachment_file.split('/')[-1])
                msg.attach(attachment)
            except IOError, e:
                logging.error("Couldn't send file. " + str(e))
        self.attachment = []

        if self.debug:
            logging.debug('DEBUG MODE: Email: {0}'.format(msg))
        else:
            try:
                response = self.server.sendmail(msg['From'], toaddrs, msg.as_string())
                logging.important('Sent email to: {0}.'.format(toaddrs))
            except smtplib.SMTPException:
                logging.error('Unable to send email to %s' % toaddrs)

        self.close()

    def close(self):
        self.server.close()
