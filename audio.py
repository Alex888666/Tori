from email.mime import audio
import requests
from requests.auth import HTTPDigestAuth

url_audio= ['http://169.254.170.200/axis-cgi/playclip.cgi?location=Apertura.mp3&repeat=0&volume=40',
'http://169.254.170.200/axis-cgi/playclip.cgi?location=Pre%20cierre.mp3&repeat=0&volume=40',
'http://169.254.170.200/axis-cgi/playclip.cgi?location=Cierre.mp3&repeat=0&volume=40']
user = input("Ingresa tu usuario: ")
password = input("Ingresa tu contraseña: ")

audio = int(input("Ingresa el número del audio: "))
x=0
while x != 'No':
    requests.get(url_audio[audio], auth=HTTPDigestAuth(user, password))
    x = input('¿Quiere responder otro audio?: ')
    if x == 'Si':
        audio = int(input("Ingresa el número del audio: "))
        requests.get(url_audio[audio], auth=HTTPDigestAuth(user, password))