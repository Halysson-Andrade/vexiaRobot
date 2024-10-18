from os import getenv, path
import subprocess
import platform
import pyautogui
import getExe
import time
from dotenv import load_dotenv
load_dotenv()

rdp_path = getenv('RDP_PATH')
def getParams():
    return getExe.getParams()

if (path.exists(rdp_path) == False):
    getExe.processar()

def launch_rdp():
    ok_button_path = 'assets/init/OkWinGuard.png'
    ok_button_path_win12 = 'assets/init/Confirm.png'
    msg_except = 'assets/init/remote_msg_detail.png'
    time.sleep(2)
    try:
        if pyautogui.locateOnScreen(msg_except, confidence=0.8, grayscale=True):
            pyautogui.click(pyautogui.locateOnScreen(msg_except, confidence=0.8, grayscale=True))
            time.sleep(0.5)
            pyautogui.write(getenv('LOGIN_PASS'))
            time.sleep(0.5)
            if pyautogui.locateOnScreen(ok_button_path_win12, confidence=0.8, grayscale=True):
                pyautogui.click(pyautogui.locateOnScreen(ok_button_path_win12, confidence=0.8, grayscale=True))
            else:
                if pyautogui.locateOnScreen(ok_button_path, confidence=0.8, grayscale=True):
                    pyautogui.click(pyautogui.locateOnScreen(ok_button_path, confidence=0.8, grayscale=True))
                else:
                    print("Erro ao localizar botão de Ok para conectar a sessão remota")
                    exit()
        else:
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
        getExe.processar()


def open_downloads_folder():
    system_name = platform.system()
    open_rdp_file(rdp_path)

def main():
    open_downloads_folder()
    launch_rdp()