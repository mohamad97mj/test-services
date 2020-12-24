from zeep import Client
from enum import Enum
import traceback
from requests import exceptions


class SMSGateway(Enum):
    ADVERTISEMENT = 1,
    PAYMENT = 2,


mobile_no = '09059242876'
message = 'hello, world!'
service_name = "mojahed sms service"

client = Client('http://10.0.32.43/SendSMS.asmx?wsdl')
with client.settings(raw_response=True):
    f = open("myfile3.txt", "w")
    try:
        result = client.service.SendSMS(mobile_no, message, SMSGateway.ADVERTISEMENT, service_name)
        f.write(str(result))
    except Exception as e:
        f.write(str(e))
    except exceptions.ConnectionError as e:
        f.write(str(e))
    finally:
        f.close()

