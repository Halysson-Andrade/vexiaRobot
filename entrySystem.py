import executeRDP
import pyautogui
import time
from pyautogui import ImageNotFoundException
import json

executeRDP.main()

MAX_RETRIES = 5

def launch_rdp():
    time.sleep(60)

    fill_username()

    pyautogui.write("SF172023")
    pyautogui.keyDown("tab")
    pyautogui.write("vexia2029")

    time.sleep(0.7)
    click_with_retries("assets/logonrdp/okcheck.png")

    # time.sleep(1)
    # if not alreadyLooged("assets/logonrdp/isAlreadyLogged.png", "assets/logonrdp/yesAlreadyLogged.png"):
    #     pass

    time.sleep(3.7)
    click_with_retries("assets/logonrdp/payroll.png")

    time.sleep(7)
    click_with_retries("assets/payroll/reports.png")

    time.sleep(0.7)
    click_with_retries("assets/payroll/sendReports.png")

    time.sleep(1)
    click_with_retries("assets/payroll/maximizepayroll.png")

    time.sleep(2)
    click_with_retries("assets/payroll/monthly.png")

    time.sleep(0.6)
    click_with_retries("assets/payroll/bycentercost.png")

    time.sleep(0.6)
    click_with_retries("assets/payroll/monthlyreport.png")

    time.sleep(0.6)
    click_with_retries("assets/payroll/enterprise.png")

    time.sleep(0.6)
    click_with_retries("assets/payroll/enterpriseClick.png")

    time.sleep(0.6)
    click_with_retries("assets/payroll/date_time.png")

    time.sleep(0.6)
    click_daily_report()

    time.sleep(0.6)
    click_with_retries("assets/print/preview_print.png")

    time.sleep(6)
    click_with_retries("assets/print/contract.png")

    time.sleep(1)
    handle_contract_form()

def fill_username():
    try:
        if not pyautogui.locateOnScreen("assets/logonrdp/userfilled.png", confidence=0.8, grayscale=True):
            pyautogui.write("3911")
            pyautogui.keyDown("tab")
        else:
            print("Campo '3911' já preenchido, pulando...")
    except ImageNotFoundException:
        pyautogui.write("3911")
        pyautogui.keyDown("tab")

def click_daily_report():
    try:
        if not pyautogui.locateOnScreen("assets/payroll/daily.png", confidence=0.8, grayscale=True):
            pyautogui.click(pyautogui.locateOnScreen("assets/payroll/dailygrayscale.png", confidence=0.8, grayscale=True))
        else:
            pyautogui.click(pyautogui.locateOnScreen("assets/payroll/daily.png", confidence=0.8, grayscale=True))
    except ImageNotFoundException as e:
        print(f"Erro: {e}, tentando novamente...")

def click_with_retries(image_path):
    for attempt in range(MAX_RETRIES):
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8, grayscale=True)
            if location:
                pyautogui.doubleClick(location)
                return
            else:
                raise ImageNotFoundException(f"Imagem não encontrada: {image_path}")
        except (ImageNotFoundException, Exception) as e:
            print(f"Erro: {e}, tentando novamente... ({attempt + 1}/{MAX_RETRIES})")
            time.sleep(1)
    print(f"Falha ao encontrar e clicar na imagem {image_path} após {MAX_RETRIES} tentativas.")
    launch_rdp()

def alreadyLooged(image_path, button):
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.8, grayscale=True)
        if location:
            pyautogui.click(pyautogui.locateOnScreen(button, confidence=0.8, grayscale=True))
            return
        else:
            raise ImageNotFoundException(f"Imagem não encontrada: {image_path}")
            pass
    except (ImageNotFoundException, Exception) as e:
        print(f"Erro, tentando novamente...")
        alreadyLooged("assets/logonrdp/isAlreadyLogged.png", "assets/logonrdp/yesAlreadyLogged.png")


def handle_contract_form():
    try:
        contract_form = pyautogui.locateOnScreen("assets/print/contract_form.png", confidence=0.8, grayscale=True)
        if contract_form:
            x, y = pyautogui.locateCenterOnScreen("assets/print/locale_contract.png", confidence=0.8, grayscale=True)
            if x is not None and y is not None:
                pyautogui.click(x, y)
                print('1st true')

                with open('json.example.json', 'r') as json_file:
                    data = json.load(json_file)
                    type_employee_names(get_employee_names(data))

                return True
            else:
                print('2nd false')
                return False
        else:
            print('3rd false')
            return False
    except (AttributeError, TypeError, FileNotFoundError, ImageNotFoundException, Exception) as e:
        print(f"Erro: {e}, tentando novamente...")
        handle_contract_form()

def get_employee_names(data):
    employees = []
    for branch_id, branch_info in data['data'].items():
        print(branch_id)
        # borrowers = branch_info.get('borrowers', {})
        # for borrower_id, borrower_info in borrowers.items():
        #     employee_list = borrower_info.get('employees', [])
        #     for employee in employee_list:
        #         employees.append(employee['empl_name'])
    return employees

def type_employee_names(employee_names):
    for name in employee_names:
        pyautogui.write(name)
        pyautogui.press('enter')
        time.sleep(1)

def main():
    launch_rdp()

main()
