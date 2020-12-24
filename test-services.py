from zeep import Client
from zeep.plugins import HistoryPlugin
from lxml import etree
from enum import Enum


class SMSGateway(Enum):
    ADVERTISEMENT = 1,
    PAYMENT = 2,


history = HistoryPlugin()
mobile_no = '09059242876'
message = 'hello, world!'
client = Client('SendSMS.xml', plugins=[history])

with client.settings(force_https=False, raw_response=True):
    service = client.create_service(
        '{http://tempuri.org/}SendSMSSoap',
        'http://10.0.32.43:80')

    result = service.SendSMS(mobile_no, message, SMSGateway.ADVERTISEMENT, "Mojahed sms service")

    # your_pretty_xml = etree.tostring(
    #     history.last_received["envelope"], encoding="unicode", pretty_print=True)

    f = open("myfile.txt", "w")
    # f.write(str(your_pretty_xml))
    f.write(str(result))
    f.close()
