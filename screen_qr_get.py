import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance
import requests
import pyautogui
import cv2
import time


def screen_spy():
   img = pyautogui.screenshot(region=[0,0,1366,768]) # x,y,w,h
   img.save('jietu.jpg',"JPEG")
   #img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)

def wx_push(message):
    url="http://wxmsg.dingliqc.com/send?msg="+message+"&userIds="  #接入微信推送
    requests.get(url)
    


def qr_scan():

   global b
   image = "jietu.jpg"
   img = Image.open(image)

   #img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度
   #img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化
   img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度
   img = img.convert('L')#灰度化

   barcodes = pyzbar.decode(img)

   for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        print(barcodeData)

   if barcodes:
     a=str(barcodes[0][0])
     if b!=a:
         file_name="签到码"+a[-2:-1]+".jpg"        #特征码，防止一直重复
         print(file_name)
         img.save(file_name,"JPEG")
         img.show()
         b=a
         wx_push(barcodeData)
     if b==a:
         print("已捕获签到二维码，请查看")
         
   if len(barcodes)==0:
         print("暂时没有签到二维码")




b=''               #状态保持量
while(1):
    screen_spy()
    qr_scan()
    time.sleep(2)