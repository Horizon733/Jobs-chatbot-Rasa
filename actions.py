# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
from rasa_sdk.events import SlotSet
import numpy as np
import os
import email
import email.encoders
import smtplib
from smtplib import SMTPConnectError,SMTPException, SMTPAuthenticationError
from datetime import date
from email.mime.multipart import MIMEMultipart


class AppliactionMail(Action):
    def name(self) -> Text:
        return 'send_process_mail'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = []
        user_input = str((tracker.latest_message)['text'])
        user_input = user_input.replace(" ", "")
        messages = "The process is "+"\n1. You will have to send us your resume on careers@diamondgems.in\n2. We will evaluate you and check the eligibility\n3. We will arrange an interview \4. Reach you out about the results"
        try:
            fromadd = '@gmail.com'
            toadd = user_input
            username = '@gmail.com'
            obj = open('password.txt')
            password = obj.read()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromadd, toadd, messages)
            server.quit()
            content = "email sent just check it"
            dispatcher.utter_message(text=content)

        except SMTPAuthenticationError as x:
            print("Your email is wrong ", x)

        except SMTPConnectError as e:
            print("Your connection Error ", e)
        except SMTPException as a:
            print("error: ", a)
            content_text = "Sorry system run into trouble.. Can you please check again?"
            dispatcher.utter_message(text=content_text)
        return []
