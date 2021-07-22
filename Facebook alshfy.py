#!/usr/bin/python3
import base64
import time
import os
import sys
try:
    import requests
    
except ImportError:
    print("Error to import 'requests' Library\ntodo : python3 -m pip install requests")
    exit()

banner ="""
 "\033[32m"  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
"\033[31m"     ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||=======>✪kareemalshfy✪  <=========|||||||||||||||||
 "\033[33m"    ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
     WhatsApp>  +201068960354              
   "\033[35m"    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  

  
    """

print(banner)

p = input("Enter a id the user facebook : > ")
m = input("Enter the How many times does he try the code?  : > ")
resp = requests.post('https://raw.githubusercontent.com/kareem68960/kareemalshfy-pin/main/kareemalshfy.txt/text', {
        'phone': (p),
        'message': (m), 
        'key': 'textbelt',      
})

try:
    int(p) 
    print("\n\t\t[ + ] plase wait ..... ")
    time.sleep( 5 )
    print(resp.json())
    

except:
    print("\n\t[!] Error Danger danger please escape")
    print("\t[!] Please try again and enter the id  \n ")











