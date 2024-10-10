import executeRDP
import pyautogui
import time
import json
import sys
import pyperclip
from datetime import datetime
from pyautogui import ImageNotFoundException 

paramsExecution = executeRDP.getParams()  # Capturando valores da Fila
executeRDP.main()
MAX_RETRIES = 5
def launch_rdp():
    wating = 'assets/while/login_metadados.png'
    payroll = 'assets/flow/step01.png'
    step02 = 'assets/flow/step02.png'
    step03 = 'assets/flow/step03.png'
    step04 = 'assets/flow/step04.png'
    step06 = 'assets/flow/step06.png'
    # Validação da abertura do sistema
    while True:
        try:
            # Tenta localizar a imagem na tela
            location = pyautogui.locateOnScreen(wating, confidence=0.8, grayscale=True)
            if location:
                print("Imagem encontrada.")
                break               
            else:
                print("Aguardando abertura do Metadados")
                time.sleep(1)  # Espera 1 segundo antes de tentar novamente 
        except Exception as e:
            # Exibe o erro exato que está ocorrendo
            time.sleep(1)  # Espera 1 segundo antes de tentar novamente 
            print(f"Erro ao localizar a imagem: {e}")
            launch_rdp()
            break   

    fill_username()

    pyautogui.write("SF178583")
    pyautogui.keyDown("tab")
    pyautogui.write("12345")

    time.sleep(0.7)
    click_with_retries(wating)
    validationHide(wating)
    click(payroll,0)
    validationHide(payroll)
    validationShow(step02)
    click(step02,0)
    validationShow(step03)
    click(step03,0)
    validationShow(step04)
    
    # Execução das automações
    folhaAnalitica('1100',step06)
    
    

    #click_with_retries(payroll)

    time.sleep(3.7)
    

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
        if not pyautogui.locateOnScreen("assets/logonrdp/haly/userfilled.png", confidence=0.8, grayscale=True):
            pyautogui.write("3911")
            pyautogui.keyDown("tab")
        else:
            print("Campo '3911' já preenchido, pulando...")
    except ImageNotFoundException:
        pyautogui.write("3911")
        pyautogui.keyDown("tab")

def click(imgRef,exeptionControl):
    try:
        if pyautogui.locateOnScreen(imgRef, confidence=0.8, grayscale=True):
            click_with_retries(imgRef)
        else:
            print("Erro ao localizar a imagem", imgRef )
            sys.exit() 
    except (ImageNotFoundException, Exception) as e:
            
            print("Erro ao localizar a imagem", imgRef )
            if imgRef == "assets/flow/createNewFolder.png"and exeptionControl == 2:
                print("teste")
                wait_for_it ='assets/flow/wait_for_it.png'
                start_folde_create_flow ='assets/flow/start_folde_create_flow.png'
                save ='assets/flow/save.png'
                create_folder ='assets/flow/create_folder.png'
                currentFolder ='assets/flow/currentFolder.png'
                firstClickToCreateFolderArquiteture ='assets/flow/firstClickToCreateFolderArquiteture.png'
                click(start_folde_create_flow,0)
                validationHide(start_folde_create_flow)
                validationShow(wait_for_it)
                validationShow(save)
                click(save,0)
                validationShow(create_folder)
                validationShow(currentFolder)
                click(firstClickToCreateFolderArquiteture,0)
                time.sleep(0.5)
                pyautogui.press("down")
                pyautogui.write("Automações_Yupa")
                pyautogui.press('enter')
            else:
                sys.exit() 
            #Implementar o reprocessamento da automação

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
                pyautogui.click(location)
                return
            else:
                raise ImageNotFoundException(f"Imagem não encontrada: {image_path}")
        except (ImageNotFoundException, Exception) as e:
            print(f"Erro: {e}, tentando novamente... ({attempt + 1}/{MAX_RETRIES})")
            time.sleep(1)
    print(f"Falha ao encontrar e clicar na imagem {image_path} após {MAX_RETRIES} tentativas.")
    launch_rdp()

def validationHide(imgRef):
    while True:
        try:
            # Tenta localizar a imagem na tela
            location = pyautogui.locateOnScreen(imgRef, confidence=0.8, grayscale=True)
            if location:
                print("Aguarndando sumir a imagem", imgRef)
                time.sleep(0.2)  # Espera 1 segundo antes de tentar novamente               
            else:
                 print("Próxima etapa avançada", imgRef)
                 break 
                
        except Exception as e:
            print(f"Estapa executada com sucesso",imgRef)
            break  
def validationShow(imgRef):
    while True:
        try:
            # Tenta localizar a imagem na tela
            location = pyautogui.locateOnScreen(imgRef, confidence=0.8, grayscale=True)
            if location:
                print("Clique realizado com sucesso", imgRef)
                break 
            else:
                print("Aguarndando sumir a imagem", imgRef)
                time.sleep(0.2)  # Espera 1 segundo antes de tentar novamente
                
        except Exception as e:
            if imgRef =='assets/flow/currentFolder.png':
                backPage ="assets/flow/backPage.png"
                click(backPage,0)
            print(f"Aguardando imagem de referencia",imgRef)
            time.sleep(0.2)
            validationShow(imgRef)
            break  

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
################################### Automações específicas ################################
def folhaAnalitica(cod, imgRef):
    try:
        ########################################
        #paramsExecution = executeRDP.getParams()  # Capturando valores da Fila
        step = 0
        for flow in paramsExecution:
            if step == 0:
                configToInsert = paramsExecution.get(flow)
                compDataToInsert = configToInsert.get('ali_comp')                
                getnow = datetime.now().strftime("%Y%m%d_%H%M%S")
                folderNameComp = compDataToInsert+'_'+getnow
                folderNameComp = folderNameComp.replace('/', '')
                step = 1
            else:
                companyToProcess = paramsExecution.get(flow)
                companyData =companyToProcess.get('companyDetails')
                ########################################
                #Selecionando relatório
                pyautogui.press("tab")
                pyautogui.write(cod)
                pyautogui.press("tab")
                pyautogui.press("enter")
                validationShow(imgRef) #Validando se o relatório foi selecionado
                #Clicando em copetencia
                competenciaIsFound = 'assets/flow/competenciaIsFound.png'
                validationShow(competenciaIsFound)
                click(competenciaIsFound,0)
                pyautogui.press("tab")
                pyautogui.keyDown("shift")
                pyautogui.press("end")
                pyautogui.press("delete")
                pyautogui.keyUp("shift")
                pyautogui.write(compDataToInsert)
                company_click = 'assets/flow/company_click.png'
                click(company_click,0)
                isCompanySelected = 'assets/flow/isCompanySelected.png'
                validationShow(isCompanySelected)
                if companyData.get('cmp_system_code') == '1001':
                    companyToSelect = 'assets/flow/companyToSelect.png'
                    companySelected = 'assets/flow/companySelected.png'
                    print = 'assets/flow/print.png'
                    printSelected = 'assets/flow/printSelected.png'
                    filter = 'assets/flow/filter.png'
                    filterSelected = 'assets/flow/filterSelected.png'
                    click(companyToSelect,0)
                    validationShow(companySelected)
                    click(print,0)
                    validationShow(printSelected)
                    click(filter,0)
                    validationShow(filterSelected)
                    pyautogui.press("tab")
                    branches =companyToProcess.get('branches')
                    for flow in branches:
                        brancheToProcess = branches.get(flow)
                        bracheDetails = brancheToProcess.get('branchDetails')
                        bracheSystemCode = bracheDetails.get('brc_system_code')
                        pyautogui.write(bracheSystemCode)
                        pyautogui.press("tab")
                        bracheName = bracheDetails.get('brc_name')
                        brancheBorrowers = brancheToProcess.get('borrowers')
                        for key in brancheBorrowers:
                            borrowToprocess = brancheBorrowers.get(key)
                            borrowerDetails = borrowToprocess.get('borrowerDetails')
                            borrowName = borrowerDetails.get('brr_name')
                            borrowEmployees = borrowToprocess.get('employees')
                            for empKey in borrowEmployees:                                
                                employeeRegister = empKey.get('empl_matricula')
                                pyautogui.write(employeeRegister)
                                pyautogui.press("enter")
                            start_folde_create_flow ='assets/flow/start_folde_create_flow.png'
                            save ='assets/flow/save.png'
                            create_folder ='assets/flow/create_folder.png'
                            currentFolder ='assets/flow/currentFolder.png'
                            firstClickToCreateFolderArquiteture ='assets/flow/firstClickToCreateFolderArquiteture.png'
                            wait_for_it ='assets/flow/wait_for_it.png'
                            click(start_folde_create_flow,0)
                            validationHide(start_folde_create_flow)
                            validationShow(wait_for_it)
                            validationShow(save)
                            click(save,0)
                            validationShow(create_folder)
                            validationShow(currentFolder)
                            click(firstClickToCreateFolderArquiteture,0)
                            time.sleep(0.5)
                            pyautogui.press("down")
                            time.sleep(0.2)
                            pyautogui.write("Automações_Yupa")
                            time.sleep(0.2)
                            pyautogui.press('enter')
                            time.sleep(0.2)
                            isFolderExist= 'assets/flow/isFolderExist.png'
                            noFouders = 'assets/flow/noFouders.png'
                            checkFolders(folderNameComp,noFouders,0)
                            checkFolders(bracheName,noFouders,0)
                            checkFolders(borrowName,noFouders,1)
                            checkFolders('Emissão de folha Analítica',noFouders,0)
                            pyautogui.press('tab')
                            pyautogui.press('tab')
                            time.sleep(0.1)
                            pyautogui.write('impressão_dos_funcionários_alocados')
                            save_click ='assets/flow/save_click.png'
                            click(save_click,0)
                            validationHide(save_click)
                            validationShow(wait_for_it)
                            pyautogui.press('esc')
                            time.sleep(0.2)
                            validationShow(filterSelected)
                            removeAll ='assets/flow/removeAll.png'
                            click(removeAll,0)
                            afterRemoveAll ='assets/flow/afterRemoveAll.png'
                            validationShow(afterRemoveAll)
                            pyautogui.press("tab")
                            time.sleep(0.1)
                            pyautogui.press("tab")
                            time.sleep(0.1)
                            pyautogui.press("tab")
                            time.sleep(0.1)
                            pyautogui.press("tab")
                            time.sleep(0.1)
                            pyautogui.press("tab")
                            time.sleep(0.1)
                            pyautogui.press("tab")
                            time.sleep(0.1)
                        print(f"Finalizad   o processamento de {borrowName}.")  # Exemplo de ação ao término do loop

                else:
                    print("Configurar novas empresas")
    except ImageNotFoundException:
        print("Erro seleção do relatório")
        sys.exit() 

def checkFolders(folderToFind,isFolderExist,controlBorrow):
    try:
        time.sleep(0.2)
        location = pyautogui.locateOnScreen(isFolderExist, confidence=0.8, grayscale=True)
        if location:
            createNewFolder = 'assets/flow/createNewFolder.png'
            click(createNewFolder,0)
            time.sleep(0.1)
            pyautogui.press("f2")
            time.sleep(0.1)
            pyautogui.write(folderToFind)
            pyautogui.press('enter')
            time.sleep(0.1)
            pyautogui.press('enter')  
    except Exception as e:
        while True:
                if controlBorrow == 1 :
                    createNewFolder = 'assets/flow/createNewFolder.png'
                    click(createNewFolder,0)
                    time.sleep(0.1)
                    pyautogui.press("f2")
                    time.sleep(0.1)
                    pyautogui.write(folderToFind)
                    pyautogui.press('enter')
                    time.sleep(0.1)
                    pyautogui.press('enter') 
                    break
                else:
                    time.sleep(0.2)
                    pyautogui.press("down")
                    time.sleep(0.2)
                    pyautogui.press("f2")
                    time.sleep(0.1)
                    pyautogui.hotkey("ctrl", "c")
                    copied_value = pyperclip.paste()
                    pyautogui.press('esc')                
                    try:
                        print(folderToFind)
                        print(copied_value)
                        if folderToFind == copied_value:
                            pyautogui.press('enter')
                            break               
                        else:
                            print("Check next folder")
                            time.sleep(0.2)
                            pyautogui.press("down")
                            time.sleep(0.2)
                            pyautogui.press("f2")
                            time.sleep(0.1)
                            pyautogui.hotkey("ctrl", "c")
                            pyautogui.press('enter')
                            next_value = pyperclip.paste()
                            if next_value == copied_value:
                                createNewFolder = 'assets/flow/createNewFolder.png'
                                click(createNewFolder,2)
                                print("tratar exceção")                            
                                time.sleep(0.2)
                                pyautogui.press("f2")
                                time.sleep(0.2)
                                pyautogui.write(folderToFind)
                                pyautogui.press('enter')
                                time.sleep(0.1)
                                pyautogui.press('enter')
                                break
                            else:
                                pyautogui.press("up")
                    except Exception as e:
                        print("Erro na criação de estrutura de pasta")
                        break  

def main():
    launch_rdp()


main()
