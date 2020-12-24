from zeep import Client, Settings
from enum import Enum


class SMSGateway(Enum):
    ADVERTISEMENT = 1,
    PAYMENT = 2,


mobile_no = '09059242876'
message = 'hello, world!'
settings = Settings(strict=False, force_https=False, xml_huge_tree=True)
client = Client('test.wsdl', settings=settings)
with client.settings(raw_response=True):
    response = client.service.SendSMS(mobile_no, message, SMSGateway.ADVERTISEMENT, "Mojahed sms service")
    f = open("myfile2.txt", "w")
    f.write(str(result))
    f.close()
