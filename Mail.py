import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


fromaddress = "systatict1611@gmail.com"
toaddress = "systatict1611@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddress

msg['To'] = toaddress

msg['Subject'] = " TEST EXECUTION REPORT OF R1BACKOFFICE"

body = "Respected Sir/Madam    \n\nPlease find Attachment Test Execution Report Of R1BACKOFFICE.   \n\nThanks and Regards \nRitika Kamboj  "

msg.attach(MIMEText(body,'plain'))

filename = "BlastResults1.xls"
attachment = open("BlastResults1.xls","rb")


part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename = %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddress,"Username@1611")
text = msg.as_string()
server.sendmail(fromaddress, toaddress, text)
server.quit()











