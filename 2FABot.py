import telepot
import pyotp #Importeert de Telegram & 2FA API's
from telepot.loop import MessageLoop
from pprint import pprint #OwO mooie tekst

bot = telepot.Bot("370325529:AAGKGqP-dHRoyKb2FKnPtMyYCdOhcGKLK5Q")
response = bot.getUpdates() #pakt het laatst verzonden bericht aan de bot
response_1 = response[1]
UserID = response_1['message']['chat']['id'] #pakt het ID van de verzender

FietsID = ####Vogel uit hoe je enkel het bericht leest, dit moet overeenkomen met de .csv



def TwoFactor(TFAcode):
    while True:
        if FietsID == :####whatever er in de .csv staat
            TFAcode = ####Hier nog een pyotp Time-based OTP invoeren
            bot.sendMessage(UserID, 'Placeholder voor Pyotp.TOTP')
        else: bot.sendMessage(UserID, 'Dat is niet het ID van je fiets')
        return TFAcode

def UnlockFiets():
    while True:
        if input('Voer hier je TFACode in om je fiets op te kunnen halen: ') == TFACode: ##komt nog wel
            print('Je kan bij je fiets!')
        else: input('Dit klopt niet. Probeer opnieuw: ')

TwoFactor()
UnlockFiets()


####klopt hier het een en ander niet I know, maar komt nog wel