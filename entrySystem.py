import requestsApi
import executeRDP
from os import getenv
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
    robotExecution('1100',step06)
    robotExecution('1180',step06)
    

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
                pyautogui.press('esc')
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
def robotExecution(cod, imgRef):
    try:
        step = 0
        ########################################
        #paramsExecution = executeRDP.getParams()  # Capturando valores da Fila
        for flow in paramsExecution:
            if step == 0:
                configToInsert = paramsExecution.get(flow)
                proc_id = configToInsert.get('proc_id')  
                proc_comp_ref = configToInsert.get('proc_comp_ref') 
                compDataToInsert = configToInsert.get('ali_comp')
                ali_id = configToInsert.get('ali_id')                  
                getnow = datetime.now().strftime("%Y%m%d_%H%M%S")
                folderNameComp = compDataToInsert+'_'+getnow
                folderNameComp = folderNameComp.replace('/', '')
                if proc_comp_ref !="":
                    folderNameComp = proc_comp_ref
                step = 1
                aut_id = 6
                ## Registro do processamento:
                token = requestsApi.login()
                if token is None:
                    print("Falha no registro da execução do Robô Folha Analíca - Step Login API")
                else:
                    updateFolderId = requestsApi.updateFolderId(token, proc_id, folderNameComp)
                    if updateFolderId.status_code == 200:
                        print("Armazenado ID da estrutura de pasta")
                    else:
                        print("Não foi armazenado o ID da Pasta, erro de comunicação com banco de dados")
                    response = requestsApi.registerRobot(token, aut_id, proc_id, step, bot_sucess_message="Iniciando a execução da Automação", bot_error_message="")
                    if response.status_code == 200:
                        print("Registro da execução do robo criada com sucesso!")
                    else:
                        print("Erro no Registro da execução do robo")
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
                    print_image = 'assets/flow/print.png'
                    printSelected = 'assets/flow/printSelected.png'
                    filter = 'assets/flow/filter.png'
                    filterSelected = 'assets/flow/filterSelected.png'
                    click(companyToSelect,0)
                    validationShow(companySelected)
                    click(print_image,0)
                    validationShow(printSelected)
                    click(filter,0)
                    validationShow(filterSelected)
                    pyautogui.press("tab")
                    branches =companyToProcess.get('branches')
                    for flow in branches:
                        brancheToProcess = branches.get(flow)
                        bracheDetails = brancheToProcess.get('branchDetails')
                        bracheSystemCode = bracheDetails.get('brc_system_code')
                        brc_id = bracheDetails.get('brc_id')
                        pyautogui.write(bracheSystemCode)
                        pyautogui.press("tab")
                        bracheName = bracheDetails.get('brc_name')
                        brancheBorrowers = brancheToProcess.get('borrowers')
                        for key in brancheBorrowers:
                            borrowToprocess = brancheBorrowers.get(key)
                            borrowerDetails = borrowToprocess.get('borrowerDetails')
                            borrowName = borrowerDetails.get('brr_name')
                            brr_id = borrowerDetails.get('brr_id')
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
                            time.sleep(0.1)
                            checkFolders(bracheName,noFouders,0)
                            time.sleep(0.1)
                            checkFolders(borrowName,noFouders,1)
                            time.sleep(0.1)
                            checkFolders('Emissao de folha Analitica',noFouders,0)
                            time.sleep(0.2)
                            pyautogui.press('tab')
                            time.sleep(0.2)
                            pyautogui.press('tab')
                            time.sleep(0.2)
                            pyautogui.write('impressao_dos_funcionarios_alocados')
                            save_click ='assets/flow/save_click.png'
                            time.sleep(0.2)
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
                            employeesToUpdate = requestsApi.updateEmployeesStatusTrue(token, ali_id, brc_id, brr_id)
                            if employeesToUpdate.status_code == 200:
                                print("Armazenado ID da estrutura de pasta")
                            else:
                                print("Não foi armazenado o ID da Pasta, erro de comunicação com banco de dados")
                        print(f"Finalizad   o processamento de {borrowName}.")  # Exemplo de ação ao término do loop
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
                else:
                    print("Configurar novas empresas")
    except ImageNotFoundException:
        print("Erro seleção do relatório")
        sys.exit() 

def checkFolders(folderToFind,isFolderExist,controlBorrow):
    print("Iniciando processo de validação das pastas:")
    print("Pasta para criação", folderToFind)
    try:
        time.sleep(0.2)
        location = pyautogui.locateOnScreen(isFolderExist, confidence=0.8, grayscale=True)
        if location:
            print("Pasta vazia")
            createNewFolder = 'assets/flow/createNewFolder.png'
            click(createNewFolder,0)
            time.sleep(0.2)
            pyautogui.press("f2")
            time.sleep(0.2)
            pyautogui.write(folderToFind)
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.press('enter') 
            print("Pasta criada com sucesso!") 
    except Exception as e:
        while True:
                if controlBorrow == 1 :
                    print("Criação automática pasta de tomadores") 
                    createNewFolder = 'assets/flow/createNewFolder.png'
                    time.sleep(0.1)
                    click(createNewFolder,0)
                    time.sleep(0.2)
                    pyautogui.press("f2")
                    time.sleep(0.2)
                    pyautogui.write(folderToFind)
                    pyautogui.press('enter')
                    try:
                        time.sleep(0.5)
                        duplication = 'assets/flow/duplication.png'
                        isDuplicated = pyautogui.locateOnScreen(duplication, confidence=0.8, grayscale=True)
                        if isDuplicated:
                            print("Pasta duplicada será ")    
                            clickDuplication = 'assets/flow/clickDuplication.png' 
                            validationShow(clickDuplication)
                            click(clickDuplication,0)
                            openCreated = 'assets/flow/openCreated.png' 
                            validationShow(openCreated)
                            time.sleep(1)
                            pyautogui.press('delete')
                            time.sleep(1)
                            deleteFolder = 'assets/flow/deleteFolder.png' 
                            validationShow(deleteFolder)
                            clickDelete = 'assets/flow/clickDelete.png' 
                            click(clickDelete,0)
                            createNewFolder = 'assets/flow/createNewFolder.png'
                            time.sleep(0.1)
                            click(createNewFolder,0)
                            time.sleep(0.2)
                            pyautogui.press("f2")
                            time.sleep(0.2)
                            pyautogui.write(folderToFind)
                            pyautogui.press('enter')
                    except Exception as e:
                        print("Pasta do Tomador é nova - Não é duplicada")   
                    time.sleep(0.2)
                    pyautogui.press('enter') 
                    print("Pasta criada com sucesso!") 
                    break
                else:
                    print("Não está Vazia") 
                    print("Procurando pasta para ou criação ou entrar na pasta") 
                    time.sleep(0.2)
                    pyautogui.press("down")
                    time.sleep(0.2)
                    pyautogui.press("f2")
                    time.sleep(0.1)
                    pyautogui.hotkey("ctrl", "c")
                    copied_value = pyperclip.paste()
                    time.sleep(0.1)
                    pyautogui.press('esc')                
                    try:
                        print("Comparação das pastas") 
                        print(folderToFind)
                        print(copied_value)
                        if folderToFind == copied_value:
                            print("Achou a pasta acessando a pasta") 
                            pyautogui.press('enter')
                            copied_value = ''
                            break               
                        else:
                            print("Pasta não localizadaCheck next folder")
                            time.sleep(0.2)
                            pyautogui.press("down")
                            time.sleep(0.2)
                            pyautogui.press("f2")
                            time.sleep(0.1)
                            pyautogui.hotkey("ctrl", "c")
                            pyautogui.press('enter')
                            next_value = pyperclip.paste()
                            if next_value == copied_value:
                                print("Ultima pasta iniciando a criação da nova pasta")
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
                                print("Pasta criada com sucesso")
                                copied_value = ''
                                break
                            else:
                                print("Varrendo a próxima pasta")
                                copied_value = ''
                                pyautogui.press("up")
                    except Exception as e:
                        print("Erro na criação de estrutura de pasta")
                        copied_value = ''
                        break  

def main():
    launch_rdp()


main()
