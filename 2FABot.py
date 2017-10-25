import telepot
import pyotp #Importeert de Telegram & 2FA API's
from telepot.loop import MessageLoop
import csv
from pprint import pprint #OwO mooie tekst
from Fietsenstalling import csvread

####2FA- & Botgedeelte
bot = telepot.Bot("370325529:AAGKGqP-dHRoyKb2FKnPtMyYCdOhcGKLK5Q") #Hash voor de bot
response = bot.getUpdates() #pakt het laatst verzonden bericht aan de bot
response_1 = response[-1]
UserID = response_1['message']['chat']['id'] #pakt het ID van de verzender
UserBericht = response_1['message']['text']

def TFACode():
    print("bla")
def BotBericht():
    gebruiker_gegevens = csvread("gebruikers.csv")
    print("Stuur een bericht met je Fietsnummer naar https://t.me/BevFietsBot")
    for gebruiker_gegeven in gebruiker_gegevens:
        while True:
            if UserBericht == gebruiker_gegeven["fietsnummer"]:
                bot.sendMessage(UserID, 'Placeholder voor Pyotp.TOTP')
                break
            else: bot.sendMessage(UserID, "Dit is niet je fietscode, probeer opnieuw.")

BotBericht()