import argparse
import pywhatkit
import time
import pyautogui
from datetime import datetime

pyautogui.FAILSAFE = True

# Add .csv file to send messages in bulk in future

def send_messages(contact, messages, wait_time):
    pywhatkit.sendwhatmsg_instantly(
        contact,
        messages[0],
        wait_time=wait_time,
        tab_close=False
    )

    time.sleep(2)
    pyautogui.press("enter")

    for msg in messages[1:]:
        time.sleep(1)
        pyautogui.write(msg, interval=0.04)
        pyautogui.press("enter")


def log(contact, messages):
    with open("whatsapp_log.txt", "a") as f:
        f.write(
            f"[{datetime.now()}] Sent {len(messages)} messages to {contact}\n"
        )


def main():
    parser = argparse.ArgumentParser(
        description="CLI-based WhatsApp Automation Tool"
    )

    parser.add_argument(
        "--contacts",
        nargs="+",
        required=True,
        help="Phone numbers with country code"
    )

    parser.add_argument(
        "--messages",
        nargs="+",
        required=True,
        help="Messages to send "
    )

    parser.add_argument(
        "--wait",
        type=int,
        default=20,
        help="Wait time for WhatsApp Web load"
    )

    args = parser.parse_args()

    for contact in args.contacts:
        send_messages(contact, args.messages, args.wait)
        log(contact, args.messages)
        time.sleep(3)

    print("All messages sent successfully!")


if __name__ == "__main__":
    main()
