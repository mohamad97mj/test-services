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
client = Client('test.wsdl', plugins=[history])

with client.settings(force_https=False, raw_response=True):

    result = client.service.SendSMS(mobile_no, message, 1, "Mojahed sms service")

    # your_pretty_xml = etree.tostring(
    #     history.last_received["envelope"], encoding="unicode", pretty_print=True)

    f = open("myfile.txt", "w")
    # f.write(str(your_pretty_xml))
    f.write(str(result))
    f.close()
