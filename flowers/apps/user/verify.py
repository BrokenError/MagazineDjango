import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException, TwilioException

account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'value of sid'
auth_token = os.environ['TWILIO_AUTH_TOKEN'] = '<your Twilio Auth Token here>'
service = os.environ['TWILIO_VERIFY_SERVICE_ID'] = '<your Twilio Verify Service SID here>'

client = Client(account_sid, auth_token)
verify = client.verify.services(service)


def send(phone):
    try:
        verify.verifications.create(to=phone, channel='sms')
    except TwilioException:
        verify.verifications.create(to=phone, channel='call')


def check(phone, code):
    try:
        result = verify.verification_checks.create(to=phone, code=code)
    except TwilioRestException:
        return False
    return result.status == 'approved'
