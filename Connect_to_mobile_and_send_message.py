import os

def send_sms_from_mobile(number, message):
    os.system(f'adb shell am start -a android.intent.action.SENDTO -d sms:{number} --es sms_body "{message}"')
