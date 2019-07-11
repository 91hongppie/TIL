import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD : ')

msg = EmailMessage()
msg['subject'] = '요기요 이벤트'
msg['From'] = 'marioz9@naver.com'
msg['To'] = '91hongppie@gmail.com', 'toohong5@gmail.com', '91hongpy@gmail.com'
msg.set_content('치킨 반값')

ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
ssafy.login('marioz9', password)
ssafy.send_message(msg)

print('이메일 전송 완료!')

to_email_list = ['91hongppie@gmail.com', '91hongpy@gmail.com', 'marioz9@naver.com']
for email in to_email_list:
    msg = EmailMessage()
    msg['subject'] = '요기요 이벤트'
    msg['From'] = 'marioz9@naver.com'
    msg['To'] = email
    msg.set_content('치킨 반값')

    ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
    ssafy.login('marioz9', password)
    ssafy.send_message(msg)

    print('이메일 전송 완료!')
