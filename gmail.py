from email.message import EmailMessage
import smtplib

def sendEmail(dic, counter):
    user = 'tavaresrenzo@gmail.com'
    password = "tieqdvgnoamjkyps"
    receiver = 'tavaresrenzo@gmail.com'
    subject = f"Daily volatility alerts: {counter} events"
    content = "Hi Renzo, check this news for today:<br><br>"
    index = 0
    for option in dic:
        dic2 = dic[str(index)]
        content += f"{dic2['time']}  -{dic2['currency']} - {dic2['event']}<br>"
        index += 1
    content += "<br>That's all for today, take care!"
    try:
        email = EmailMessage()
        email['From'] = user
        email['To'] = receiver
        email['subject'] = subject
        email.add_header('Content-Type', 'text/html')
        email.set_payload(content)

        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.starttls()
        s.login(email['From'], password)
        s.sendmail(email['From'], [email['To']], email.as_string().encode('utf-8'))

        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
    
