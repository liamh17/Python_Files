print("Enter phone number..")
number = int(input())
number = str(number)

print("Enter carrier..")
carrier = str(input())

if carrier == 'verizon':
    sendnum = '' + number + '@vtext.com'

elif carrier == 'tmobile':
    sendnum = '' + number + '@tmomail.com'

elif carrier == 'att':
    sendnum = '' + number + '@txt.att.net'

elif carrier == 'sprint':
    sendnum = '' + number + '@messaging.sprintpcs.com'

elif carrier == 'cricket':
    sendnum = '' + number + '@sms.mycricket.com'

print(sendnum)