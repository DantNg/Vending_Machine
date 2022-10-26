import imp
import urllib.request 
import urllib.parse 
from urllib import request
from PIL import Image,ImageQt
from io import BytesIO
import datetime,time
import threading
import json
class MomoPayment:
    def __init__(self,cost):
        self.url = 'https://momosv3.apimienphi.com/api/'
        self.qrCodeParam ={ 
                            "phone": "0366485529", 
                            "amount": cost, 
                            "note": cost 
                            }  
        self.success_payment = False
        self.start_time = datetime.datetime.now()
        self.end_time = self.start_time + datetime.timedelta(seconds=100)
        self.log = []
    #Tạo mã QR thanh toán  
    def requestQRCode(self):
        query_string = urllib.parse.urlencode(self.qrCodeParam )
        self.url = self.url+"QRCode" + "?" + query_string 
        with urllib.request.urlopen( self.url ) as response: 
            response_text = response.read() 
            img = Image.open(BytesIO(response_text) )
            img.save('qr.png')
    #Kiểm tra giao dịch
    def checkPayment(self):
        current_time = datetime.datetime.now()
        # end_time = current_time + datetime.timedelta(seconds=10)
        url = 'https://momosv3.apimienphi.com/api/getTransHistory'
        data= json.load(open('json_file\getTransHistory.json'))
        #print(data)
        data = json.dumps(data)
        data = str(data)
        data = data.encode('utf-8')
        # Post Method 
        req =  request.Request(url, data=data)
        try:
            # Response
            resp = request.urlopen(req)
            myJson = resp.read()
            a = json.loads(myJson)
            self.log = [a['data'][0]["partnerName"] ,a['data'][0]["amount"],a['data'][0]["clientTime"]]
            print (self.log)
            if(a['data'][0]["clientTime"]>= str(self.start_time)  and a['data'][0]["clientTime"] <= str(self.end_time) ):
                print("Thanh toán thành công !")
                self.success_payment = True
                self.log = [a['data'][0]["partnerName"] ,a['data'][0]["amount"],a['data'][0]["clientTime"]] 
        except:
            print("Mất kết nối với Momo!")


        