from django.shortcuts import render, redirect
# Create your views here.
import time
import serial
from datetime import datetime
from QRcodes.models import  Donkethon, DonTrichLucHoTich, DonChungNhanHonNhan, Donkhaitu, DonKhaiSinh
from django.http import HttpResponse
from django.template.loader import get_template

from django.template import Context
from django.template.loader import render_to_string
from QRCODE.settings import MEDIA_ROOT
from django.views.decorators.csrf import csrf_exempt
from mailmerge import MailMerge
import pandas as pd
from QRCODE import settings
import os
from num2words import num2words



soluong=''



def index(request):
    return render(request, 'QRcodes/index.html')


serial_data = ''

def chon_don_1 (request):
    return render(request, 'QRcodes/chon.html')


def chon_don_2(request):
    return render(request, 'QRcodes/chon_don_2.html')

def don_1_nguoi(request):
    
    hovaten_string=''
    so_cccd = ''
    so_cccd_cu =''
    ngay_cap_chuan=''
    gioi_tinh=''
    ngay_sinh_chuan=''
    gioi_tinh=''

    data_json_1=''

    if request.method == 'POST' and 'scan_data_1' in request.POST:
       
        ser = serial.Serial(
            port = '/dev/ttyAMA0',
            baudrate = 9600,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1
        )    
        time.sleep(10)
        qr_code = ser.readline()
        ser.close()

        if qr_code:
            data = qr_code.decode("latin-1")	
            data1 = data.rstrip()
            # cut "\r\n" at last of string
            data=data.replace('|'," ")
            outputString = data1.encode('utf-8').hex()
            print(outputString)
            b = outputString.replace("7c", ",")
            # print(b)
            c=b.split(',')
            
            
        
            hovaten_hex=c[2].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5').replace('0110','0ac490')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â±    
        
            tach_hovaten= ' '.join([hovaten_hex[i:i+2] for i in range(0, len(hovaten_hex), 2)])
            #-------------------------------------------------------------------------------------------------------------------------------------#
            
            
            diachi_hex = c[5].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').replace('0110','0ac490').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â± 
            dia_chi = ' '.join([diachi_hex[i:i+2] for i in range(0, len(diachi_hex), 2)])
            
        
            ngaysinh = c[3]
            ngaysinh = bytes.fromhex(ngaysinh).decode('utf-8')
            birthday = datetime.strptime(ngaysinh, "%d%m%Y")
            so_cccd = c[0]
            so_cccd = bytes.fromhex(so_cccd).decode('utf-8')
            so_cccd_cu = c[1]
            so_cccd_cu = bytes.fromhex(so_cccd_cu).decode('utf-8')
            hovaten_string= bytes.fromhex(tach_hovaten).decode('utf-8')
            ngay_sinh_chuan = datetime.strftime(birthday, "%d/%m/%Y")
            gioi_tinh = c[4].replace('1ec3af','e1bbaf')
            gioi_tinh = bytes.fromhex(gioi_tinh).decode('utf-8')
            dia_chi= bytes.fromhex(dia_chi).decode('utf-8')
            ngaycap = str(c[6])
            ngaycap = bytes.fromhex(ngaycap).decode('utf-8')
            ngay_cap_1 = datetime.strptime(ngaycap, "%d%m%Y")
            ngay_cap_chuan =ngay_cap_1.strftime('%d/%m/%Y')
            thanh_pho = dia_chi.replace('\x00','').split(',')
            thanh_pho_chuan=thanh_pho[-1]
            data_json_1 = {
            'so_cccd': so_cccd.replace('\x00',''),
            'so_cmnd_cu' : so_cccd_cu.replace('\x00',''),
            'ho_va_ten':hovaten_string.replace('\x00',''),
            'ngay_sinh':ngay_sinh_chuan.replace('\x00',''),
            'gioi_tinh':gioi_tinh.replace('\x00',''),
            'dia_chi': dia_chi.replace('\x00',''),
            'ngay_cap':ngay_cap_chuan.replace('\x00',''),
            'thanh_pho': thanh_pho_chuan.replace('\x00','')
            
        }
            request.session['scan_data_1'] = data_json_1
            request.session['scan_data_2'] = data_json_1
            
    return render(request, 'QRcodes/don_1_nguoi.html', {'data_1':data_json_1})
    



@csrf_exempt

def don_2_nguoi(request):
    hovaten_string_2=''
    so_cccd_2 = ''
    so_cccd_cu_2 =''
    ngay_cap_chuan_2=''
    gioi_tinh_2=''
    dia_chi=''
    ngay_sinh_chuan_2=''
    gioi_tinh_2,
    
    hovaten_string=''
    so_cccd = ''
    so_cccd_cu =''
    ngay_cap_chuan=''
    gioi_tinh=''
    dia_chi_2=''
    ngay_sinh_chuan=''
    gioi_tinh=''
    data_json_2=''
    data_json_1=''

    if request.method == 'POST' and 'scan_data_1' in request.POST:
       
        ser = serial.Serial(
            port = '/dev/ttyAMA0',
            baudrate = 9600,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1
        )    
        time.sleep(10)
        qr_code = ser.readline()
        print(qr_code)
        ser.close()

        if qr_code:
            data = qr_code.decode("latin-1")	
            print(data)
            print(len(data))# decode s
    
            data1 = data.rstrip()
            # cut "\r\n" at last of string
            data=data.replace('|'," ")
            outputString = data1.encode('utf-8').hex()
            print(outputString)
            b = outputString.replace("7c", ",")
            # print(b)
            c=b.split(',')
            
            
        
            hovaten_hex=c[2].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5').replace('0110','0ac490')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â±    
        
            tach_hovaten= ' '.join([hovaten_hex[i:i+2] for i in range(0, len(hovaten_hex), 2)])
            #-------------------------------------------------------------------------------------------------------------------------------------#
            
            
            diachi_hex = c[5].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').replace('0110','0ac490').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â± 
            dia_chi = ' '.join([diachi_hex[i:i+2] for i in range(0, len(diachi_hex), 2)])
            
        
            ngaysinh = c[3]
            ngaysinh = bytes.fromhex(ngaysinh).decode('utf-8')
            birthday = datetime.strptime(ngaysinh, "%d%m%Y")
            so_cccd = c[0]
            so_cccd = bytes.fromhex(so_cccd).decode('utf-8')
            so_cccd_cu = c[1]
            so_cccd_cu = bytes.fromhex(so_cccd_cu).decode('utf-8')
            hovaten_string= bytes.fromhex(tach_hovaten).decode('utf-8')
            ngay_sinh_chuan = datetime.strftime(birthday, "%d/%m/%Y")
            gioi_tinh = c[4].replace('1ec3af','e1bbaf')
            gioi_tinh = bytes.fromhex(gioi_tinh).decode('utf-8')
            dia_chi= bytes.fromhex(dia_chi).decode('utf-8')
            ngay_cap = c[6]
            ngay_cap = bytes.fromhex(ngay_cap).decode('utf-8')
            ngay_cap_1 = datetime.strptime(ngay_cap, "%d%m%Y")
            ngay_cap_chuan = datetime.strftime(ngay_cap_1, "%d/%m/%Y")
            thanh_pho = dia_chi.replace('\x00','').split(',')
            thanh_pho_chuan=thanh_pho[-1]
            data_json_1 = {
            'so_cccd': so_cccd,
            'so_cmnd_cu' : so_cccd_cu,
            'ho_va_ten':hovaten_string,
            'ngay_sinh':ngay_sinh_chuan.replace('\x00',''),
            'gioi_tinh':gioi_tinh,
            'dia_chi': dia_chi.replace('\x00',''),
            'ngay_cap':ngay_cap_chuan,
            'thanh_pho': thanh_pho_chuan
            
        }
            print(data_json_1['dia_chi'])
            print(data_json_1)
            request.session['scan_data_1'] = data_json_1
            print(data_json_1)
        
           
    if request.method == 'POST' and 'scan_data_2' in request.POST:
        ser = serial.Serial(
            port = '/dev/ttyAMA0',
            baudrate = 9600,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1
        )
            
        time.sleep(10)
        qr_code_2 = ser.readline()

        ser.close()

        if qr_code_2:
            data_2 = qr_code_2.decode("latin-1")	
            
    
            data1_2 = data_2.rstrip()
            # cut "\r\n" at last of string
            data_2=data_2.replace('|'," ")
            outputString = data1_2.encode('utf-8').hex()
            b = outputString.replace("7c", ",")
            # print(b)
            c=b.split(',')
            
            
        
            hovaten_hex_2=c[2].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5').replace('0110','0ac490')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â±    
        
            tach_hovaten_2= ' '.join([hovaten_hex_2[i:i+2] for i in range(0, len(hovaten_hex_2), 2)])
            #-------------------------------------------------------------------------------------------------------------------------------------#
            
            
            diachi_hex_2 = c[5].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').replace('0110','0ac490').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â± 
            print(diachi_hex_2)
            dia_chi_2 = ' '.join([diachi_hex_2[i:i+2] for i in range(0, len(diachi_hex_2), 2)])
            print(dia_chi_2)
            
        
            ngaysinh_2 = c[3]
            ngaysinh_2 = bytes.fromhex(ngaysinh_2).decode('utf-8')
            birthday_2 = datetime.strptime(ngaysinh_2, "%d%m%Y")
            so_cccd_2 = c[0]
            so_cccd_2 = bytes.fromhex(so_cccd_2).decode('utf-8')
            so_cccd_cu_2 = c[1]
            so_cccd_cu_2 = bytes.fromhex(so_cccd_cu_2).decode('utf-8')
            hovaten_string_2= bytes.fromhex(tach_hovaten_2).decode('utf-8')
            ngay_sinh_chuan_2 = datetime.strftime(birthday_2, "%d/%m/%Y")
            gioi_tinh_2 = c[4].replace('1ec3af','e1bbaf')
            gioi_tinh_2 = bytes.fromhex(gioi_tinh_2).decode('utf-8')
            dia_chi_2= bytes.fromhex(dia_chi_2).decode('utf-8')
            thanh_pho_2 = dia_chi_2.replace('\x00','').split(',')
            thanh_pho_chuan_2=thanh_pho_2[-1]
    
            ngay_cap_2 = c[6]
            ngay_cap_2 = bytes.fromhex(ngay_cap_2).decode('utf-8')
            ngay_cap_2 = datetime.strptime(ngay_cap_2, "%d%m%Y")
            ngay_cap_chuan_2 = datetime.strftime(ngay_cap_2, "%d/%m/%Y")
            # ngay_cap_2 = bytes.fromhex(ngay_cap_2).decode('utf-8')
            # ngay_cap_dinh_dang_2 = datetime.strptime(ngay_cap_2, "%d/%m/%Y")
            # ngay_cap_chuan_2 = datetime.strftime(ngay_cap_dinh_dang_2, "%d/%m/%Y")
            
            data_json_2 = {
            'so_cccd_2': so_cccd_2,
            'so_cmnd_cu_2' : so_cccd_cu_2,
            'ho_va_ten_2':hovaten_string_2.replace('\x00',''),
            'ngay_sinh_2':ngay_sinh_chuan_2,
            'gioi_tinh_2':gioi_tinh_2,
            'dia_chi_2':dia_chi_2.replace('\x00',''),
            'ngay_cap_2':ngay_cap_chuan_2,
            'thanh_pho_2' : thanh_pho_chuan_2
        }
            print(data_json_2)
            request.session['scan_data_2'] = data_json_2
            
         
        
    
 

    return render(request,'QRcodes/don_2_nguoi.html', {'data_1':data_json_1,
                                                    'data_2': data_json_2})

def ket_hon(request):
    hovaten_string_2=''
    so_cccd_2 = ''
    so_cccd_cu_2 =''
    ngay_cap_chuan_2=''
    gioi_tinh_2=''
    dia_chi=''
    ngay_sinh_chuan_2=''
    gioi_tinh_2,
    
    hovaten_string=''
    so_cccd = ''
    so_cccd_cu =''
    ngay_cap_chuan=''
    gioi_tinh=''
    dia_chi_2=''
    ngay_sinh_chuan=''
    gioi_tinh=''
    data_json_2=''
    data_json_1=''

    if request.method == 'POST' and 'scan_data_1' in request.POST:
       
        ser = serial.Serial(
            port = '/dev/ttyAMA0',
            baudrate = 9600,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1
        )    
        time.sleep(10)
        qr_code = ser.readline()
        print(qr_code)
        ser.close()

        if qr_code:
            data = qr_code.decode("latin-1")	
            print(data)
            print(len(data))# decode s
    
            data1 = data.rstrip()
            # cut "\r\n" at last of string
            data=data.replace('|'," ")
            outputString = data1.encode('utf-8').hex()
            print(outputString)
            b = outputString.replace("7c", ",")
            # print(b)
            c=b.split(',')
            
            
        
            hovaten_hex=c[2].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5').replace('0110','0ac490')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â±    
        
            tach_hovaten= ' '.join([hovaten_hex[i:i+2] for i in range(0, len(hovaten_hex), 2)])
            #-------------------------------------------------------------------------------------------------------------------------------------#
            
            
            diachi_hex = c[5].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').replace('0110','0ac490').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â± 
            dia_chi = ' '.join([diachi_hex[i:i+2] for i in range(0, len(diachi_hex), 2)])
            
        
            ngaysinh = c[3]
            ngaysinh = bytes.fromhex(ngaysinh).decode('utf-8')
            birthday = datetime.strptime(ngaysinh, "%d%m%Y")
            so_cccd = c[0]
            so_cccd = bytes.fromhex(so_cccd).decode('utf-8')
            so_cccd_cu = c[1]
            so_cccd_cu = bytes.fromhex(so_cccd_cu).decode('utf-8')
            hovaten_string= bytes.fromhex(tach_hovaten).decode('utf-8')
            ngay_sinh_chuan = datetime.strftime(birthday, "%d/%m/%Y")
            gioi_tinh = c[4].replace('1ec3af','e1bbaf')
            gioi_tinh = bytes.fromhex(gioi_tinh).decode('utf-8')
            dia_chi= bytes.fromhex(dia_chi).decode('utf-8')
            ngay_cap = c[6]
            ngay_cap = bytes.fromhex(ngay_cap).decode('utf-8')
            ngay_cap_1 = datetime.strptime(ngay_cap, "%d%m%Y")
            ngay_cap_chuan = datetime.strftime(ngay_cap_1, "%d/%m/%Y")
            thanh_pho = dia_chi.replace('\x00','').split(',')
            thanh_pho_chuan=thanh_pho[-1]
            data_json_1 = {
            'so_cccd': so_cccd,
            'so_cmnd_cu' : so_cccd_cu,
            'ho_va_ten':hovaten_string,
            'ngay_sinh':ngay_sinh_chuan.replace('\x00',''),
            'gioi_tinh':gioi_tinh,
            'dia_chi': dia_chi.replace('\x00',''),
            'ngay_cap':ngay_cap_chuan,
            'thanh_pho': thanh_pho_chuan
            
        }
            print(data_json_1['dia_chi'])
            print(data_json_1)
            request.session['scan_data_1'] = data_json_1
            print(data_json_1)
        
           
    if request.method == 'POST' and 'scan_data_2' in request.POST:
        ser = serial.Serial(
            port = '/dev/ttyAMA0',
            baudrate = 9600,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1
        )
            
        time.sleep(10)
        qr_code_2 = ser.readline()

        ser.close()

        if qr_code_2:
            data_2 = qr_code_2.decode("latin-1")	
            
    
            data1_2 = data_2.rstrip()
            # cut "\r\n" at last of string
            data_2=data_2.replace('|'," ")
            outputString = data1_2.encode('utf-8').hex()
            b = outputString.replace("7c", ",")
            # print(b)
            c=b.split(',')
            
            
        
            hovaten_hex_2=c[2].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5').replace('0110','0ac490')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â±    
        
            tach_hovaten_2= ' '.join([hovaten_hex_2[i:i+2] for i in range(0, len(hovaten_hex_2), 2)])
            #-------------------------------------------------------------------------------------------------------------------------------------#
            
            
            diachi_hex_2 = c[5].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').replace('0110','0ac490').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â± 
            print(diachi_hex_2)
            dia_chi_2 = ' '.join([diachi_hex_2[i:i+2] for i in range(0, len(diachi_hex_2), 2)])
            print(dia_chi_2)
            
        
            ngaysinh_2 = c[3]
            ngaysinh_2 = bytes.fromhex(ngaysinh_2).decode('utf-8')
            birthday_2 = datetime.strptime(ngaysinh_2, "%d%m%Y")
            so_cccd_2 = c[0]
            so_cccd_2 = bytes.fromhex(so_cccd_2).decode('utf-8')
            so_cccd_cu_2 = c[1]
            so_cccd_cu_2 = bytes.fromhex(so_cccd_cu_2).decode('utf-8')
            hovaten_string_2= bytes.fromhex(tach_hovaten_2).decode('utf-8')
            ngay_sinh_chuan_2 = datetime.strftime(birthday_2, "%d/%m/%Y")
            gioi_tinh_2 = c[4].replace('1ec3af','e1bbaf')
            gioi_tinh_2 = bytes.fromhex(gioi_tinh_2).decode('utf-8')
            dia_chi_2= bytes.fromhex(dia_chi_2).decode('utf-8')
            thanh_pho_2 = dia_chi_2.replace('\x00','').split(',')
            thanh_pho_chuan_2=thanh_pho_2[-1]
    
            ngay_cap_2 = c[6]
            ngay_cap_2 = bytes.fromhex(ngay_cap_2).decode('utf-8')
            ngay_cap_2 = datetime.strptime(ngay_cap_2, "%d%m%Y")
            ngay_cap_chuan_2 = datetime.strftime(ngay_cap_2, "%d/%m/%Y")
            # ngay_cap_2 = bytes.fromhex(ngay_cap_2).decode('utf-8')
            # ngay_cap_dinh_dang_2 = datetime.strptime(ngay_cap_2, "%d/%m/%Y")
            # ngay_cap_chuan_2 = datetime.strftime(ngay_cap_dinh_dang_2, "%d/%m/%Y")
            
            data_json_2 = {
            'so_cccd_2': so_cccd_2,
            'so_cmnd_cu_2' : so_cccd_cu_2,
            'ho_va_ten_2':hovaten_string_2.replace('\x00',''),
            'ngay_sinh_2':ngay_sinh_chuan_2,
            'gioi_tinh_2':gioi_tinh_2,
            'dia_chi_2':dia_chi_2.replace('\x00',''),
            'ngay_cap_2':ngay_cap_chuan_2,
            'thanh_pho_2' : thanh_pho_chuan_2
        }
            print(data_json_2)
            request.session['scan_data_2'] = data_json_2
            
         
        
    
 

    return render(request,'QRcodes/dien_ket_hon.html', {'data_1':data_json_1,
                                                    'data_2': data_json_2})



def don_khai_tu(request):
    hovaten_string_2=''
    so_cccd_2 = ''
    so_cccd_cu_2 =''
    ngay_cap_chuan_2=''
    gioi_tinh_2=''
    dia_chi=''
    ngay_sinh_chuan_2=''
    gioi_tinh_2,
    
    hovaten_string=''
    so_cccd = ''
    so_cccd_cu =''
    ngay_cap_chuan=''
    gioi_tinh=''
    dia_chi_2=''
    ngay_sinh_chuan=''
    gioi_tinh=''
    data_json_2=''
    data_json_1=''

    if request.method == 'POST' and 'scan_data_1' in request.POST:
       
        ser = serial.Serial(
            port = '/dev/ttyAMA0',
            baudrate = 9600,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1
        )    
        time.sleep(10)
        qr_code = ser.readline()
        ser.close()

        if qr_code:
            data = qr_code.decode("latin-1")	
            print(len(data))# decode s
    
            data1 = data.rstrip()
            # cut "\r\n" at last of string
            data=data.replace('|'," ")
            outputString = data1.encode('utf-8').hex()
            print(outputString)
            b = outputString.replace("7c", ",")
            # print(b)
            c=b.split(',')
            
            
        
            hovaten_hex=c[2].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5').replace('0110','0ac490')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â±    
        
            tach_hovaten= ' '.join([hovaten_hex[i:i+2] for i in range(0, len(hovaten_hex), 2)])
            #-------------------------------------------------------------------------------------------------------------------------------------#
            
            
            diachi_hex = c[5].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').replace('0110','0ac490').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â± 
            dia_chi = ' '.join([diachi_hex[i:i+2] for i in range(0, len(diachi_hex), 2)])
            
        
            ngaysinh = c[3]
            ngaysinh = bytes.fromhex(ngaysinh).decode('utf-8')
            birthday = datetime.strptime(ngaysinh, "%d%m%Y")
            so_cccd = c[0]
            so_cccd = bytes.fromhex(so_cccd).decode('utf-8')
            so_cccd_cu = c[1]
            so_cccd_cu = bytes.fromhex(so_cccd_cu).decode('utf-8')
            hovaten_string= bytes.fromhex(tach_hovaten).decode('utf-8')
            ngay_sinh_chuan = datetime.strftime(birthday, "%d/%m/%Y")
            gioi_tinh = c[4].replace('1ec3af','e1bbaf')
            gioi_tinh = bytes.fromhex(gioi_tinh).decode('utf-8')
            dia_chi= bytes.fromhex(dia_chi).decode('utf-8')
            ngay_cap = c[6]
            ngay_cap = bytes.fromhex(ngay_cap).decode('utf-8')
            ngay_cap_1 = datetime.strptime(ngay_cap, "%d%m%Y")
            ngay_cap_chuan = datetime.strftime(ngay_cap_1, "%d/%m/%Y")
            thanh_pho = dia_chi.replace('\x00','').split(',')
            thanh_pho_chuan=thanh_pho[-1]
            data_json_1 = {
            'so_cccd': so_cccd,
            'so_cmnd_cu' : so_cccd_cu,
            'ho_va_ten':hovaten_string,
            'ngay_sinh':ngay_sinh_chuan.replace('\x00',''),
            'gioi_tinh':gioi_tinh,
            'dia_chi': dia_chi.replace('\x00',''),
            'ngay_cap':ngay_cap_chuan,
            'thanh_pho': thanh_pho_chuan
            
        }
            print(data_json_1['dia_chi'])
            print(data_json_1)
            request.session['scan_data_1'] = data_json_1
            print(data_json_1)
        
           
    if request.method == 'POST' and 'scan_data_2' in request.POST:
        ser = serial.Serial(
            port = '/dev/ttyAMA0',
            baudrate = 9600,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1
        )
            
        time.sleep(10)
        qr_code_2 = ser.readline()

        ser.close()

        if qr_code_2:
            data_2 = qr_code_2.decode("latin-1")	
            
    
            data1_2 = data_2.rstrip()
            # cut "\r\n" at last of string
            data_2=data_2.replace('|'," ")
            outputString = data1_2.encode('utf-8').hex()
            b = outputString.replace("7c", ",")
            # print(b)
            c=b.split(',')
            
            
        
            hovaten_hex_2=c[2].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5').replace('0110','0ac490')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â±    
        
            tach_hovaten_2= ' '.join([hovaten_hex_2[i:i+2] for i in range(0, len(hovaten_hex_2), 2)])
            #-------------------------------------------------------------------------------------------------------------------------------------#
            
            
            diachi_hex_2 = c[5].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').replace('0110','0ac490').strip() # thay thĂ¡ÂºÂ¿ kÄ‚Â­ tĂ¡Â»Â± 
            print(diachi_hex_2)
            dia_chi_2 = ' '.join([diachi_hex_2[i:i+2] for i in range(0, len(diachi_hex_2), 2)])
            print(dia_chi_2)
            
        
            ngaysinh_2 = c[3]
            ngaysinh_2 = bytes.fromhex(ngaysinh_2).decode('utf-8')
            birthday_2 = datetime.strptime(ngaysinh_2, "%d%m%Y")
            so_cccd_2 = c[0]
            so_cccd_2 = bytes.fromhex(so_cccd_2).decode('utf-8')
            so_cccd_cu_2 = c[1]
            so_cccd_cu_2 = bytes.fromhex(so_cccd_cu_2).decode('utf-8')
            hovaten_string_2= bytes.fromhex(tach_hovaten_2).decode('utf-8')
            ngay_sinh_chuan_2 = datetime.strftime(birthday_2, "%d/%m/%Y")
            gioi_tinh_2 = c[4].replace('1ec3af','e1bbaf')
            gioi_tinh_2 = bytes.fromhex(gioi_tinh_2).decode('utf-8')
            dia_chi_2= bytes.fromhex(dia_chi_2).decode('utf-8')
            thanh_pho_2 = dia_chi_2.replace('\x00','').split(',')
            thanh_pho_chuan_2=thanh_pho_2[-1]
    
            ngay_cap_2 = c[6]
            ngay_cap_2 = bytes.fromhex(ngay_cap_2).decode('utf-8')
            ngay_cap_2 = datetime.strptime(ngay_cap_2, "%d%m%Y")
            ngay_cap_chuan_2 = datetime.strftime(ngay_cap_2, "%d/%m/%Y")
            # ngay_cap_2 = bytes.fromhex(ngay_cap_2).decode('utf-8')
            # ngay_cap_dinh_dang_2 = datetime.strptime(ngay_cap_2, "%d/%m/%Y")
            # ngay_cap_chuan_2 = datetime.strftime(ngay_cap_dinh_dang_2, "%d/%m/%Y")
            
            data_json_2 = {
            'so_cccd_2': so_cccd_2,
            'so_cmnd_cu_2' : so_cccd_cu_2,
            'ho_va_ten_2':hovaten_string_2.replace('\x00',''),
            'ngay_sinh_2':ngay_sinh_chuan_2,
            'gioi_tinh_2':gioi_tinh_2,
            'dia_chi_2':dia_chi_2.replace('\x00',''),
            'ngay_cap_2':ngay_cap_chuan_2,
            'thanh_pho_2' : thanh_pho_chuan_2
        }
            print(data_json_2)
            request.session['scan_data_2'] = data_json_2
            
         
        
    
 

    return render(request,'QRcodes/khai_tu.html', {'data_1':data_json_1,
                                                    'data_2': data_json_2})



def khai_tu_1(request):
    x = datetime.now()
    ngay=x.day
    thang=x.month
    nam=x.year
    data_1 = request.session.get('scan_data_1')
    data_2 = request.session.get('scan_data_2')
    
    
    if data_1 and data_2:
     
        ho_va_ten=data_1['ho_va_ten']
        ngay_sinh=data_1['ngay_sinh']
        so_cccd=data_1['so_cccd']
            
        # 
        ho_va_ten_2=data_2['ho_va_ten_2']
        ngay_sinh_2=data_2['ngay_sinh_2']
        so_cccd_2=data_2['so_cccd_2']
        
     
    
    if request.method == 'POST':
        if request.POST.get('chon'):
            soluong=request.POST.get('chon')
            thanh_tien= int(soluong)* 5000
         
    
            Donkhaitu.objects.create(ho_va_ten=ho_va_ten,so_cccd= so_cccd, ho_va_ten_nguoi_mat=ho_va_ten_2, so_cccd_nguoi_mat=so_cccd_2, thanh_tien=thanh_tien )
    
        return render(request, 'QRcodes/result.html')
    
    # TĂ¡Â»â€°nh/TP
    
    return render(request,'QRcodes/Khai_tu_1.html',{ 
        'data1': data_1,
        'ngay':str(ngay),
        'thang':str(thang),
        'nam':str(nam),})
    
  
  
def ket_hon_1(request):
    x = datetime.now()
    ngay=x.day
    thang=x.month
    nam=x.year
    soluong=''
    
    
    data_1 = request.session.get('scan_data_1')
    data_2 = request.session.get('scan_data_2')

    
    if data_1 and data_2:
     
        ho_va_ten=data_1['ho_va_ten']
        ngay_sinh=data_1['ngay_sinh']
        so_cccd=data_1['so_cccd']
      
        
        # 
        ho_va_ten_2=data_2['ho_va_ten_2']
        ngay_sinh_2=data_2['ngay_sinh_2']
        so_cccd_2=data_2['so_cccd_2']
        
     
    
    if request.method == 'POST':
        if request.POST.get('chon'):
            soluong=request.POST.get('chon')
            thanh_tien= int(soluong)* 5000
         
    
            Donkethon.objects.create(ho_va_ten_nam=ho_va_ten,so_cccd_nam= so_cccd, ho_va_ten_nu=ho_va_ten_2, so_cccd_nu=so_cccd_2, thanh_tien=thanh_tien )
            del request.session['scan_data_1']
            del request.session['scan_data_2']
            
            return render(request, 'QRcodes/result.html')
    
    return render(request,'QRcodes/Ket_hon.html',{
        'ngay':ngay,
        'thang':thang,
        'nam':nam,
        'so_luong' : soluong,
        
    })
    
    
    
    
def trich_luc_ho_tich_1(request):
    x = datetime.now()
    ngay=x.day
    thang=x.month
    nam=x.year
    data_1 = request.session.get('scan_data_1')
    data_2 = data_1

    if data_1 and data_2:
     
        ho_va_ten=data_1['ho_va_ten']
        ngay_sinh=data_1['ngay_sinh']
        so_cccd=data_1['so_cccd']
      
        
        # 
        ho_va_ten_2=data_2['ho_va_ten']
        ngay_sinh_2=data_2['ngay_sinh']
        so_cccd_2=data_2['so_cccd']
        

    
  
    if request.POST.get('in'):
        soluong=request.POST.get('chon')
        loai_don = request.POST.get('chon_1')
       
    
    
        thanh_tien= int(soluong)* 5000
         
    
        DonTrichLucHoTich.objects.create(ho_va_ten_nguoi_yeu_cau=ho_va_ten,so_cccd_nguoi_yeu_cau= so_cccd, loai_don = loai_don , ho_va_ten_nguoi_lam_ho=ho_va_ten_2, so_cccd=so_cccd_2, thanh_tien=thanh_tien )
        del request.session['scan_data_1']
        del request.session['scan_data_2']
        return render(request, 'QRcodes/result.html')
   
    return render(request, 'QRcodes/trich_luc_ho_tich.html',{
        'ngay':ngay,
        'thang':thang,
        'nam':nam,
    })
    
 
    
def trich_luc_ho_tich_2(request):
    x = datetime.now()
    ngay=x.day
    thang=x.month
    nam=x.year
    data_1 = request.session.get('scan_data_1')
    data_2 = request.session.get('scan_data_2')

    if data_1 and data_2:
     
        ho_va_ten=data_1['ho_va_ten']
        ngay_sinh=data_1['ngay_sinh']
        so_cccd=data_1['so_cccd']
      
        
        # 
        ho_va_ten_2=data_2['ho_va_ten_2']
        ngay_sinh_2=data_2['ngay_sinh_2']
        so_cccd_2=data_2['so_cccd_2']
        
  
    if request.POST.get('in'):
        soluong=request.POST.get('chon')
        loai_don = request.POST.get('chon_1')
       
    
    
        thanh_tien= int(soluong)* 5000
         
        DonTrichLucHoTich.objects.create(ho_va_ten_nguoi_yeu_cau=ho_va_ten,so_cccd_nguoi_yeu_cau= so_cccd, loai_don = loai_don , ho_va_ten_nguoi_lam_ho=ho_va_ten_2, so_cccd=so_cccd_2, thanh_tien=thanh_tien )
        del request.session['scan_data_1']
        del request.session['scan_data_2']
        return render(request, 'QRcodes/result.html')    
    return render(request, 'QRcodes/trich_luc_ho_tich_2.html',{
        'ngay':ngay,
        'thang':thang,
        'nam':nam,
    })
    

def xac_nhan_hon_nhan(request):
    x = datetime.now()
    ngay=x.day
    thang=x.month
    nam=x.year
    data_1 = request.session.get('scan_data_1')
    data_2 = data_1

    if data_1 and data_2:
     
        ho_va_ten=data_1['ho_va_ten']
        ngay_sinh=data_1['ngay_sinh']
        so_cccd=data_1['so_cccd']
      
        
        # 
        ho_va_ten_2=data_2['ho_va_ten']
        ngay_sinh_2=data_2['ngay_sinh']
        so_cccd_2=data_2['so_cccd']
        thanh_tien=''
        
        if request.POST.get('in'):  
            thanh_tien= 5000
         
    
            DonChungNhanHonNhan.objects.create(ho_va_ten_nguoi_yeu_cau=ho_va_ten,so_cccd_nguoi_yeu_cau= so_cccd,  ho_va_ten=ho_va_ten_2, so_cccd=so_cccd_2, thanh_tien=thanh_tien )
            del request.session['scan_data_1']
            del request.session['scan_data_2']
            return render(request, 'QRcodes/result.html')

    return render(request,'QRcodes/xnhonnhan.html',{
        'ngay':ngay,
        'thang':thang,
        'nam':nam,})
    
    
def xac_nhan_hon_nhan_2(request):
    x = datetime.now()
    ngay=x.day
    thang=x.month
    nam=x.year
    data_1 = request.session.get('scan_data_1')
    data_2 = request.session.get('scan_data_2')

    if data_1 and data_2:
     
        ho_va_ten=data_1['ho_va_ten']
        ngay_sinh=data_1['ngay_sinh']
        so_cccd=data_1['so_cccd']
      
        
        # 
        ho_va_ten_2=data_2['ho_va_ten_2']
        ngay_sinh_2=data_2['ngay_sinh_2']
        so_cccd_2=data_2['so_cccd_2']
        
  
    if request.POST.get('in'):
       
    
        thanh_tien=  5000
        
        DonChungNhanHonNhan.objects.create(ho_va_ten_nguoi_yeu_cau=ho_va_ten,so_cccd_nguoi_yeu_cau= so_cccd,  ho_va_ten=ho_va_ten_2, so_cccd=so_cccd_2, thanh_tien=thanh_tien )
        del request.session['scan_data_1']
        del request.session['scan_data_2']
        return render(request, 'QRcodes/result.html') 
    

    return render(request,'QRcodes/xnhonnhan_2.html',{
        'ngay':ngay,
        'thang':thang,
        'nam':nam,})





#Khai_sinh


def don_khai_sinh(request):
    hovaten_string_2=''
    so_cccd_2 = ''
    so_cccd_cu_2 =''
    ngay_cap_chuan_2=''
    gioi_tinh_2=''
    dia_chi=''
    ngay_sinh_chuan_2=''
    gioi_tinh_2,
    
    hovaten_string=''
    so_cccd = ''
    so_cccd_cu =''
    ngay_cap_chuan=''
    gioi_tinh=''
    dia_chi_2=''
    ngay_sinh_chuan=''
    gioi_tinh=''
    data_json_2=''
    data_json_1=''
    data_json_3=''

    if request.method == 'POST' and 'scan_data_1' in request.POST:
       
        ser = serial.Serial(
            port = '/dev/ttyAMA0',
            baudrate = 9600,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1
        )    
        time.sleep(10)
        qr_code = ser.readline()
        print(qr_code)
        ser.close()

        if qr_code:
            data = qr_code.decode("latin-1")	
            print(data)
            print(len(data))# decode s
    
            data1 = data.rstrip()
            # cut "\r\n" at last of string
            data=data.replace('|'," ")
            outputString = data1.encode('utf-8').hex()
            print(outputString)
            b = outputString.replace("7c", ",")
            # print(b)
            c=b.split(',')
            
            
        
            hovaten_hex=c[2].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5').replace('0110','0ac490')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').strip() # thay tháº¿ kĂ­ tá»±    
        
            tach_hovaten= ' '.join([hovaten_hex[i:i+2] for i in range(0, len(hovaten_hex), 2)])
            #-------------------------------------------------------------------------------------------------------------------------------------#
            
            
            diachi_hex = c[5].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').replace('0110','0ac490').strip() # thay tháº¿ kĂ­ tá»± 
            dia_chi = ' '.join([diachi_hex[i:i+2] for i in range(0, len(diachi_hex), 2)])
            
        
            ngaysinh = c[3]
            ngaysinh = bytes.fromhex(ngaysinh).decode('utf-8')
            birthday = datetime.strptime(ngaysinh, "%d%m%Y")
            so_cccd = c[0]
            so_cccd = bytes.fromhex(so_cccd).decode('utf-8')
            so_cccd_cu = c[1]
            so_cccd_cu = bytes.fromhex(so_cccd_cu).decode('utf-8')
            hovaten_string= bytes.fromhex(tach_hovaten).decode('utf-8')
            ngay_sinh_chuan = datetime.strftime(birthday, "%d/%m/%Y")
            gioi_tinh = c[4].replace('1ec3af','e1bbaf')
            gioi_tinh = bytes.fromhex(gioi_tinh).decode('utf-8')
            dia_chi= bytes.fromhex(dia_chi).decode('utf-8')
            ngay_cap = c[6]
            ngay_cap = bytes.fromhex(ngay_cap).decode('utf-8')
            ngay_cap_1 = datetime.strptime(ngay_cap, "%d%m%Y")
            ngay_cap_chuan = datetime.strftime(ngay_cap_1, "%d/%m/%Y")
            thanh_pho = dia_chi.replace('\x00','').split(',')
            thanh_pho_chuan=thanh_pho[-1]
            data_json_1 = {
            'so_cccd': so_cccd,
            'so_cmnd_cu' : so_cccd_cu,
            'ho_va_ten':hovaten_string,
            'ngay_sinh':ngay_sinh_chuan.replace('\x00',''),
            'gioi_tinh':gioi_tinh,
            'dia_chi': dia_chi.replace('\x00',''),
            'ngay_cap':ngay_cap_chuan,
            'thanh_pho': thanh_pho_chuan
            
        }
            print(data_json_1['dia_chi'])
            print(data_json_1)
            request.session['scan_data_1'] = data_json_1
            print(data_json_1)
        
           
    if request.method == 'POST' and 'scan_data_2' in request.POST:
        ser = serial.Serial(
            port = '/dev/ttyAMA0',
            baudrate = 9600,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1
        )
            
        time.sleep(10)
        qr_code_2 = ser.readline()

        ser.close()

        if qr_code_2:
            data_2 = qr_code_2.decode("latin-1")	
            
    
            data1_2 = data_2.rstrip()
            # cut "\r\n" at last of string
            data_2=data_2.replace('|'," ")
            outputString = data1_2.encode('utf-8').hex()
            b = outputString.replace("7c", ",")
            # print(b)
            c=b.split(',')
            
            
        
            hovaten_hex_2=c[2].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5').replace('0110','0ac490')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').strip() # thay tháº¿ kĂ­ tá»±    
        
            tach_hovaten_2= ' '.join([hovaten_hex_2[i:i+2] for i in range(0, len(hovaten_hex_2), 2)])
            #-------------------------------------------------------------------------------------------------------------------------------------#
            
            
            diachi_hex_2 = c[5].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').replace('0110','0ac490').strip() # thay tháº¿ kĂ­ tá»± 
            print(diachi_hex_2)
            dia_chi_2 = ' '.join([diachi_hex_2[i:i+2] for i in range(0, len(diachi_hex_2), 2)])
            print(dia_chi_2)
            
        
            ngaysinh_2 = c[3]
            ngaysinh_2 = bytes.fromhex(ngaysinh_2).decode('utf-8')
            birthday_2 = datetime.strptime(ngaysinh_2, "%d%m%Y")
            so_cccd_2 = c[0]
            so_cccd_2 = bytes.fromhex(so_cccd_2).decode('utf-8')
            so_cccd_cu_2 = c[1]
            so_cccd_cu_2 = bytes.fromhex(so_cccd_cu_2).decode('utf-8')
            hovaten_string_2= bytes.fromhex(tach_hovaten_2).decode('utf-8')
            ngay_sinh_chuan_2 = datetime.strftime(birthday_2, "%d/%m/%Y")
            gioi_tinh_2 = c[4].replace('1ec3af','e1bbaf')
            gioi_tinh_2 = bytes.fromhex(gioi_tinh_2).decode('utf-8')
            dia_chi_2= bytes.fromhex(dia_chi_2).decode('utf-8')
            thanh_pho_2 = dia_chi_2.replace('\x00','').split(',')
            thanh_pho_chuan_2=thanh_pho_2[-1]
    
            ngay_cap_2 = c[6]
            ngay_cap_2 = bytes.fromhex(ngay_cap_2).decode('utf-8')
            ngay_cap_2 = datetime.strptime(ngay_cap_2, "%d%m%Y")
            ngay_cap_chuan_2 = datetime.strftime(ngay_cap_2, "%d/%m/%Y")
            # ngay_cap_2 = bytes.fromhex(ngay_cap_2).decode('utf-8')
            # ngay_cap_dinh_dang_2 = datetime.strptime(ngay_cap_2, "%d/%m/%Y")
            # ngay_cap_chuan_2 = datetime.strftime(ngay_cap_dinh_dang_2, "%d/%m/%Y")
            
            data_json_2 = {
            'so_cccd_2': so_cccd_2,
            'so_cmnd_cu_2' : so_cccd_cu_2,
            'ho_va_ten_2':hovaten_string_2.replace('\x00',''),
            'ngay_sinh_2':ngay_sinh_chuan_2,
            'gioi_tinh_2':gioi_tinh_2,
            'dia_chi_2':dia_chi_2.replace('\x00',''),
            'ngay_cap_2':ngay_cap_chuan_2,
            'thanh_pho_2' : thanh_pho_chuan_2
        }
            
            request.session['scan_data_2'] = data_json_2
            
    if request.method == 'POST' and 'scan_data_3' in request.POST:
        ser = serial.Serial(
            port = '/dev/ttyAMA0',
            baudrate = 9600,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1
        )
            
        time.sleep(10)
        qr_code_3 = ser.readline()

        ser.close()

        if qr_code_3:
            data_3 = qr_code_3.decode("latin-1")	
            
    
            data1_3 = data_3.rstrip()
            # cut "\r\n" at last of string
            data_3=data_3.replace('|'," ")
            outputString = data1_3.encode('utf-8').hex()
            b = outputString.replace("7c", ",")
            # print(b)
            c=b.split(',')
            
            
        
            hovaten_hex_3=c[2].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5').replace('0110','0ac490')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').strip() # thay tháº¿ kĂ­ tá»±    
        
            tach_hovaten_3= ' '.join([hovaten_hex_3[i:i+2] for i in range(0, len(hovaten_hex_3), 2)])
            #-------------------------------------------------------------------------------------------------------------------------------------#
            
            
            diachi_hex_3 = c[5].replace('1ec38d','e1bb8d').replace("1ec385","e1bb85").replace('0129','c4a9')\
            .replace('c28c29','c3a1 ').replace('c2813f','c3a0').replace('1ec2a3','e1baa3').replace('00c3a3','c3a3').replace('1ec2a1','e1baa1')\
            .replace('0103','c483').replace('1ec2af','e1baaf').replace('1ec2b1','e1bab1').replace('1ec2b3','e1bab3').replace('1ec2b5','e1bab5').replace('1ec2b7','e1bab7')\
            .replace('00c3a2','c3a2').replace('1ec2a5','e1baa5').replace('1ec2a7','e1baa7').replace('1ec2a9','e1baa9').replace('1ec2ab','e1baab').replace('1ec2ad','e1baad')\
            .replace('0111','c491').replace('00c3a9','c3a9').replace('00c3a8','c3a8').replace('1ec2bb','e1babb').replace('1ec2bd','e1babd').replace('1ec2b9','e1bab9').replace('1ec2b9','e1bab9')\
            .replace('00c3aa','c3aa').replace('1ec2bf','e1babf').replace('1ec381','e1bb81').replace('1ec383','e1bb83').replace('1ec385','e1bb85').replace('1ec387','e1bb87')\
            .replace('00c3b3','c3b3').replace('00c3b2','c3b2').replace('1ec38f','e1bb8f').replace('00c3b5','c3b5').replace('1ec38d','e1bb8d')\
            .replace('00c3b4','c3b4').replace('1ec391','e1bb91').replace('1ec393','e1bb93').replace('1ec395','e1bb95').replace('1ec399','e1bb99').replace('1ec399','e1bb99')\
            .replace('01c2a1','c6a1').replace('1ec39b','e1bb9b').replace('1ec39d','e1bb9d').replace('1ec39f','e1bb9f').replace('1ec3a1','e1bba1').replace('1ec3a3','e1bba3')\
            .replace('00c3ad','c3ad').replace('00c3ac','c3ac').replace('1ec389','e1bb89').replace('0129','c4a9').replace('1ec38b','e1bb8b')\
            .replace('00c3ba','c3ba').replace('00c3b9','c3b9').replace('1ec3a7','e1bba7').replace('0169','c5a9').replace('1ec3a5','e1bba5')\
            .replace('01c2b0','c6b0').replace('1ec3a9','e1bba9').replace('1ec3ab','e1bbab').replace('1ec3ad','e1bbad').replace('1ec3af','e1bbaf').replace('1ec3b1','e1bbb1')\
            .replace('00c3bd','c3bd').replace('1ec3b3','e1bbb3').replace('1ec3b7','e1bbb7').replace('1ec3b9','e1bbb9').replace('1ec3b5','e1bbb5').replace('0110','0ac490').strip() # thay tháº¿ kĂ­ tá»± 
            print(diachi_hex_3)
            dia_chi_3 = ' '.join([diachi_hex_3[i:i+2] for i in range(0, len(diachi_hex_3), 2)])
            print(dia_chi_3)
            
        
            ngaysinh_3 = c[3]
            ngaysinh_3 = bytes.fromhex(ngaysinh_3).decode('utf-8')
            birthday_3 = datetime.strptime(ngaysinh_3, "%d%m%Y")
            so_cccd_3 = c[0]
            so_cccd_3 = bytes.fromhex(so_cccd_3).decode('utf-8')
            so_cccd_cu_3 = c[1]
            so_cccd_cu_3 = bytes.fromhex(so_cccd_cu_3).decode('utf-8')
            hovaten_string_3= bytes.fromhex(tach_hovaten_3).decode('utf-8')
            ngay_sinh_chuan_3 = datetime.strftime(birthday_3, "%d/%m/%Y")
            gioi_tinh_3 = c[4].replace('1ec3af','e1bbaf')
            gioi_tinh_3 = bytes.fromhex(gioi_tinh_3).decode('utf-8')
            dia_chi_3= bytes.fromhex(dia_chi_3).decode('utf-8')
            thanh_pho_3 = dia_chi_3.replace('\x00','').split(',')
            thanh_pho_chuan_3=thanh_pho_3[-1]
    
            ngay_cap_3 = c[6]
            ngay_cap_3 = bytes.fromhex(ngay_cap_3).decode('utf-8')
            ngay_cap_3 = datetime.strptime(ngay_cap_3, "%d%m%Y")
            ngay_cap_chuan_3 = datetime.strftime(ngay_cap_3, "%d/%m/%Y")
            # ngay_cap_2 = bytes.fromhex(ngay_cap_2).decode('utf-8')
            # ngay_cap_dinh_dang_2 = datetime.strptime(ngay_cap_2, "%d/%m/%Y")
            # ngay_cap_chuan_2 = datetime.strftime(ngay_cap_dinh_dang_2, "%d/%m/%Y")
            
            data_json_3 = {
            'so_cccd_3': so_cccd_3,
            'so_cmnd_cu_3' : so_cccd_cu_3,
            'ho_va_ten_3':hovaten_string_3.replace('\x00',''),
            'ngay_sinh_3':ngay_sinh_chuan_3,
            'gioi_tinh_3':gioi_tinh_3,
            'dia_chi_3':dia_chi_3.replace('\x00',''),
            'ngay_cap_3':ngay_cap_chuan_3,
            'thanh_pho_3' : thanh_pho_chuan_3
        }
            
            request.session['scan_data_3'] = data_json_3        
        
    
 

    return render(request,'QRcodes/don_3_nguoi.html', {'data_1':data_json_1,
                                                    'data_2': data_json_2,
                                                      'data_3': data_json_3 } )


# luu--khai_sinb

def khai_sinh_1(request):
    name_string=''
    date_string=''
    date_text=''
    x = datetime.now()
    ngay=x.day
    thang=x.month
    nam=x.year
    print(nam)

    soluong=''
    ho_va_ten=''
    so_cccd=''    # 
    ho_va_ten_me=''
    ngay_sinh_me=''
    
    ho_va_ten_cha=''
    ngay_sinh_cha=''
    

    data_1 = request.session.get('scan_data_1')
    data_2 = request.session.get('scan_data_2')
    data_3 = request.session.get('scan_data_3')

    if request.POST.get('ghi_1'):
        date_string=request.POST.get('ghi_2')
        name_string=request.POST.get('ten_khai_sinh')

        parts = date_string.split('/')
        print(parts)
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
        day_word = num2words(day, to='ordinal', lang='vi')
        month_word = num2words(month, lang='vi')
        year_word = num2words(year, lang='vi')
        date_text = f'''Ghi bằng chữ: Ngày {day_word} tháng {month_word} năm {year_word}'''
        return render(request, 'Qrcodes/khai_sinh.html',{'date_text':date_text,
                                                         'name_string': name_string,
                                                         'date_string':date_string})
        
    elif request.POST.get('in'):
        soluong=request.POST.get('chon')
        print(soluong)
        name_string=request.POST.get('ten_khai_sinh')
        date_string=request.POST.get('ghi_2')
        thanh_tien= int(soluong)* 5000
        print(name_string)

        DonKhaiSinh.objects.create(ho_va_ten_nguoi_yeu_cau=ho_va_ten,
                                    so_cccd= so_cccd, 
                                    ho_va_ten_khai_sinh=name_string,
                                    nam_sinh_khai_sinh=date_string,
                                    ho_va_ten_me=ho_va_ten_me,
                                    nam_sinh_me = ngay_sinh_me,
                                    ho_va_ten_cha = ho_va_ten_cha,
                                    nam_sinh_cha = ngay_sinh_cha,
                                    thanh_tien=thanh_tien )
        return render(request, 'Qrcodes/result.html')
        
        
   
    
    if data_1 and data_2:
     
        ho_va_ten=data_1['ho_va_ten']
        so_cccd=data_1['so_cccd']
      
        
        # 
        ho_va_ten_me=data_2['ho_va_ten_2']
        ngay_sinh_me=data_2['ngay_sinh_2']
        
        ho_va_ten_cha=data_3['ho_va_ten_3']
        ngay_sinh_cha=data_3['ngay_sinh_3']
        
   
    
        
    
    return render(request,'Qrcodes/khai_sinh.html',{
        'ngay':ngay,
        'thang':thang,
        'nam':nam,
        'so_luong' : soluong,
        'date_text': date_text,
        'name_string': name_string,
        'date_string':date_string
        
    })
        

def mobie(request):
    return render(request, 'QRcodes/mau.html')
