# 2010 Ilshad Khabibullin <astoon@spacta.com>

from email.MIMEText import MIMEText
from email.Header import Header
from zope.component import getUtility
from zope.sendmail.interfaces import IMailDelivery

from tackle.serve import config

def send_mail(message, subject, recipient,
              from_header=None, to_header=None,
              subtype='plain', sender=None):
    if sender is None:
        sender = config.get('mail', 'default_sender')
    msg = MIMEText(unicode(message), subtype, 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = Header(from_header or sender, 'utf-8')
    msg['To'] = Header(to_header or recipient, 'utf-8')
    mailer = getUtility(IMailDelivery, "tackle")
    mailer.send(sender, [recipient,], msg.as_string())
