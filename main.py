import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from coronastats import CoronaStats


def send_mail(total_cases, new_cases, total_deaths, active_cases, total_recovered, serious_critical, closed_cases):
    message = MIMEMultipart("alternative")
    message["Subject"] = email_subject
    message["From"] = email_from
    message["To"] = email_to

    body = "<html>"
    body += "<head>"
    body += "</head>"
    body += "<body>"
    body += '<center><span style="font-size: 50px;font-weight: bold;">Status of : {}</span><br</br>'.format(country)
    body += "<table width='600px' border='1px solid black' padding='3px' class='col-md-6'>"
    body += "<tr><td colspan=4><center><span style='font-size: 40px;font-weight: bold;'>Total CASES</span></center></td></tr>"
    body += "<tr><td colspan=4><center><span style='font-size: 30px;font-weight: bold;'>{total_cases}</span><br><span style='font-size:13.5px'>Total Cases</span></center></td></tr>".format(
        total_cases=total_cases)
    body += "<tr><td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:#8080FF'>{new_cases}</span><br><span style='font-size:13.5px'>New Case</span></center></td>".format(
        new_cases=new_cases)
    body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:#f5ad42'>{active_cases}</span><br><span style='font-size:13.5px'>Curently Active</span></center></td>".format(
        active_cases=active_cases)
    body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:red '>{serious_critical}</span> <br><span style='font-size:13.5px'>Critical</span></center></td>".format(
        serious_critical=serious_critical)
    body += "</tr>"
    body += "</table>"
    body += "<br>"
    body += "<br>"
    body += "<table  width='600px' border='1px solid black' padding='3px'>"
    body += "<tr><td colspan=3><center><span style='font-size: 40px;font-weight: bold;' >CLOSED CASES</span></center></td></tr>"
    body += "<tr><td colspan=3><center><span style='font-size: 30px;font-weight: bold;'>{closed_cases}</span><br><span style='font-size:13.5px'>Cases which has an outcome</span></center></td></tr>".format(
        closed_cases=closed_cases)
    body += "<tr><td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:#8ACA2B'>{total_recovered}</span><br><span style='font-size:13.5px'>Recovered</span></center></td>".format(
        total_recovered=total_recovered)
    body += "<td width='200px'></td>"
    body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:red '>{total_deaths}</span> <br><span style='font-size:13.5px'>Deaths</span></center></td>".format(
        total_deaths=total_deaths)
    body += "</tr>"
    body += "</table>"
    body += "<br><br>"
    body += "Click the link for more details : https://www.worldometers.info/coronavirus/</center>"
    body += "</body>"
    body += "</html>"

    body = MIMEText(body, "html", 'utf-8')
    message.attach(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email_from, email_password)
        server.sendmail(
            email_from, email_to, message.as_string()
        )
        server.quit()

    print('Email sent successfully.')


if __name__ == '__main__':
    with open('config.json') as file:
        config = json.load(file)

    website = config['website']
    country = input("Enter the Country name : ")
    email_subject = config['email']['subject']
    email_from = config['email']['from']
    email_password = config['email']['password']
    email_to = input("Enter the Email Address to which you want's to send mail: ")

    corona_stats = CoronaStats(country=country, website=website)

    total_cases, new_cases, total_deaths, active_cases, total_recovered, serious_critical, closed_cases = corona_stats.get_data()

    send_mail(total_cases, new_cases, total_deaths, active_cases, total_recovered, serious_critical, closed_cases)
