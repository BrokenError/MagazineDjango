import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

account_sid=os.environ['TWILIO_ACCOUNT_SID']='value of sid'
auth_token=os.environ['TWILIO_AUTH_TOKEN']='value of auth token'
service=os.environ['TWILIO_VERIFY_SERVICE_SID']='valu of service'

client = Client(account_sid, auth_token)
verify = client.verify.services(service)


def send():
    verify.verifications.create(to='+79897046544', channel='sms')


def check(phone, code):
    try:
        result = verify.verification_checks.create(to=phone, code=code)
    except TwilioRestException:
        print('no')
        return False
    return result.status == 'approved'