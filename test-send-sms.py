from zeep import Client
from zeep.plugins import HistoryPlugin
from lxml import etree

history = HistoryPlugin()
mobile_no = '09059242876'
message = 'hello, world!'
client = Client('SendSMS.xml', plugins=[history])

with client.settings(force_https=False):
    service = client.create_service(
        '{http://tempuri.org}SendSMSSoap',
        'https://10.0.32.43:80/SendSMS')

    result = client.service.SendSMS(mobile_no, message)

    your_pretty_xml = etree.tostring(
        history.last_received["envelope"], encoding="unicode", pretty_print=True)

    f = open("myfile.txt", "w")
    f.write(str(your_pretty_xml))
    f.close()
