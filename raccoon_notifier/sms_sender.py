import logging

import plivo
import urllib3.contrib.pyopenssl

urllib3.contrib.pyopenssl.inject_into_urllib3()


class SMSSender(object):

    def __init__(self, name, auth_id, auth_token):
        self.auth_id = auth_id
        self.auth_token = auth_token
        self.from_name = name
        self.server = None
        self.source_number = None
        self.ready = False
        self.sender = None
        self.debug = False

    def initialize(self):
        self.sender = plivo.RestAPI(self.auth_id, self.auth_token)
        (status, response) = self.sender.get_numbers()
        if status == 401:
            logging.error(ValueError('Unable to obtain source number from plivo API'))
            return
        self.source_number = response['objects'][0]['number']
        self.ready = True

    def send(self, phones, message):
        if not self.ready:
            self.initialize()

        if len(phones) == 0:
            return
        to = '<'.join(phones)
        params = {
            'src': self.source_number,
            'dst': to,
            'text': self.from_name + ': ' + message,
            'type': 'sms'
        }

        if self.debug:
            print params
        else:
            result = self.sender.send_message(params)
            if result[0] == 400:
                logging.error(result[1]['error'])
            logging.important('Sent SMS to: {0}. Response: {1}.'.format(phones, str(result)))
