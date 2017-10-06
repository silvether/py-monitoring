#***************************************************************#
#This script is going to run a daily test on all ip addresses to#
#see if they are still open                                     #
#                                                               #
#                                                               #
#                                                               #
#                                           -Nicholas Keels 2017#
#***************************************************************#

import smtplib
import socket

def Email(content):
    content
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('emailaddress@fqdm.com','password')
    mail.sendmail('emailaddress@fqdm.com', 'recievingemail@whatever.com', content)
    mail.close 

ip = ['10.25.128.225', '10.25.128.223', '10.25.128.224', '10.25.128.241']
err = []

for address in ip:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((address, 9999))
    if result != 0:
        err.append(address)
        
if err != None:
    Email("There is an error with the {} address(es)! Please check as soon as possible!!".format(err))
else:
    quit()




