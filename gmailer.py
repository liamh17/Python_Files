import smtplib

fromaddr = '17lheisler@fatherjudgestudent.com'
toaddrs = '17lheisler@fatherjudgestudent.com'
msg = 'There was a terrible error that occured and I wanted you to know!'


# Credentials (if needed)
username = '17lheisler@fatherjudgestudent.com'
password = 'yohihey123'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()