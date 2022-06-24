from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Thank you for subscribing to CreativeArt NewsLetter'
    sender = 'b.odhiambo.bo@gmail.com'

 