from os import getenv, path
import subprocess
import platform
import pyautogui
import time
import getExe
from dotenv import load_dotenv

load_dotenv()

rdp_path = getenv('RDP_PATH')

if (path.exists(rdp_path) == False):
    getExe.download_program()

ok_button_path = 'assets/init/OkWinGuard.png'

def launch_rdp():
    time.sleep(2)
    pyautogui.write(getenv('LOGIN_PASS'))

    time.sleep(0.5)

    try:
        if not pyautogui.locateOnScreen(ok_button_path, confidence=0.8, grayscale=True):
            print("Botão 'Ok' não encontrado, pulando...")
            exit()
        else:
            pyautogui.click(pyautogui.locateOnScreen(ok_button_path, confidence=0.8, grayscale=True))
    except Exception as e:
        print(f"Erro: {e}, tentando novamente...")

    time.sleep(2)

def open_rdp_file(rdp_path):
    if path.exists(rdp_path):
        subprocess.Popen(['start', rdp_path], shell=True)
    else:
        print("Arquivo RDP não encontrado.")


def open_downloads_folder():
    system_name = platform.system()

    open_rdp_file(rdp_path)

def main():
    open_downloads_folder()
    launch_rdp()
