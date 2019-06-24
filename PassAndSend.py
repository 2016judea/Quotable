"""
Author: Aidan Jude
Date: 06/23/2019
Description:
    -This file passes the pseudo random author to the get_random_quote module
    -After this, we send SMS messages to the listed recipients
"""

from QuoteFetch import *
import smtplib
from email.mime.text import MIMEText
from time import sleep

#utilize a gmail account to send the desired text messages
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(GmailAccount, Password)
end_users = ['9999999999@vtext.com', '9999999999@txt.att.net']

favorite_authors = ['F Scott Fitzgerald', 'Thomas Wolfe', 'Cormac McCarthy', 'John Keats',
                        'T S Eliot', 'John Steinbeck', 'W B Yeats', 'Ernest Hemingway',
                        'Rupert Brooke', 'John Milton', 'C S Lewis', 'Friedrich Nietzsche']

y = random.choice(range(0, 12, 1))
to_send = get_random_quote(favorite_authors[y]) + ' - ' + favorite_authors[y]
#MIMEText seems to cut off messages over 120 characters, so to be safe we slice large ones in half and send two messages
if len(to_send) > 110:
    length_string = len(to_send)
    first_length = round(length_string / 2)
    first_half = to_send[0:first_length]
    second_half = to_send[first_length:]
    message_1 = MIMEText(first_half, 'html')
    message_2 = MIMEText(second_half, 'html')
    for user in end_users:
        server.sendmail('Quotable', user, message_1.as_string())
        sleep(2.0)
        server.sendmail('Quotable', user, message_2.as_string())
else:
    message = MIMEText(to_send, 'html')
    message['Subject'] = 'Quotable'
    for user in end_users:
        server.sendmail('Quotable', user, message.as_string())

server.quit()
