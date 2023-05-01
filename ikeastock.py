import requests
import re
import time
import smtplib, ssl
from getpass import getpass
from email.message import EmailMessage
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print("("+current_time+") Enter item ID: ")
itemID = input()
url = "https://api.ingka.ikea.com/cia/availabilities/ru/ca?itemNos="+(itemID)

headers = {
    "Connection": "keep-alive",
    "x-client-id": "b6c117e5-ae61-4ef5-b4cc-e0b1e37f0631"
}

msg = EmailMessage()
msg["Subject"] = "Ikea Stock Alert"
print("Enter your email address: ")
msg["From"] = input()
print("Enter your email password: ")
password = getpass()
print("Enter the recipient email: ")
msg["To"] = input()
print("How often would you like to receive an email update on your item's stock? \n(type a digit in minutes): ")
minutes = int(input())
mins = minutes*60
print("Sending updates to "+msg["To"]+" every "+str(minutes)+" minutes...\n")

while 1 == 1:
    req = requests.get(url, headers=headers)

    resp = req.text

    stock = resp.replace('"216"', "Calgary")
    stock = stock.replace('"349"', "Edmonton")
    stock = stock.replace('"313"', "Coquitlam")
    stock = stock.replace('"003"', "Richmond")
    stock = stock.replace('"249"', "Winnipeg")
    stock = stock.replace('"529"', "Dartmouth")
    stock = stock.replace('"040"', "Burlington")
    stock = stock.replace('"256"', "Etobicoke")
    stock = stock.replace('"149"', "NorthYork")
    stock = stock.replace('"004"', "Ottawa")
    stock = stock.replace('"372"', "Vaughan")
    stock = stock.replace('"414"', "Boucherville")
    stock = stock.replace('"039"', "Montreal")
    stock = stock.replace('"559"', "QuebecCity")

        
    x = re.findall('Calgary|Edmonton|Coquitlam|Richmond|Winnipeg|Dartmouth|Burlington|Etobicoke|NorthYork|Ottawa|Vaughan|Boucherville|Montreal|QuebecCity|LOW_IN_STOCK|HIGH_IN_STOCK|OUT_OF_STOCK', stock)

    final = str(x).replace("'OUT", "\n'OUT")
    final = final.replace("'LOW", "\n'LOW")
    final = final.replace("'HIGH", "\n'HIGH")
    print(final)

    #Send email
    

    msg.set_content(final)
    context=ssl.create_default_context()

    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as smtp:
        smtp.starttls(context=context)
        smtp.login(msg["From"], password)
        smtp.send_message(msg)
        smtp.quit()
    time.sleep(mins)
