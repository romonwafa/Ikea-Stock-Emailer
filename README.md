# Ikea Stock Emailer
Furniture kept going out of stock at Ikea during the Coronavirus pandemic so I wrote this script to send automated emails on product availability.

Emails can only be sent <b>from</b> emails using Outlook SMTP settings (@outlook and @hotmail), but can be sent <b>to</b> any email address.


This tool is desgined for Ikea locations in Canada.

# Requirements

<= Python 3.7

Outlook or Hotmail email

# Usage
python ikeastock.py 

# Additional Notes
Ikea item IDs can be found in the url of the item on the ikea website. It will be the digits at the end of the url. Omit any letters or other characters such as slashes. You will need to enter this when prompted by the program.
Emails will stop sending when the program is closed.
