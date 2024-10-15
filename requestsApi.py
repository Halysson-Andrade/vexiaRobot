from os import getenv
from dotenv import load_dotenv 
import requests
load_dotenv()  
def login(attempts=0, MAX_RETRIES=5):
    # Capturar dados para processamento
    portalUrl = getenv('LOGIN')
    userPortal = getenv('USER')
    passwordPortal = getenv('PASSWORD')
    
    # Preparar payload para login na API
    payload = {
        "email": userPortal,
        "password": passwordPortal
    }
    
    # Fazer a requisição POST para login
    response = requests.post(portalUrl, json=payload)
    
    # Verificar o status da resposta
    if response.status_code == 200:
        print("Login bem-sucedido.")
        response = response.json()  
        data_field = response.get("data")     
        token = data_field.get("token")  
        return token
    
    else:
        print(f"Erro ao tentar logar. Tentativa {attempts + 1} de {MAX_RETRIES}.")
        
        # Verifica se ainda há tentativas restantes
        if attempts < MAX_RETRIES - 1:
            return login(attempts + 1, MAX_RETRIES)
        else:
            print("Número máximo de tentativas atingido. Login falhou.")
            return None  # Ou levante uma exceção, caso prefira

def registerRobot(token, aut_id, proc_id, bot_status, bot_sucess_message, bot_error_message):
    # Exemplo de uso
    # token = "seu_token_aqui"
    # response = registerRobot(token, aut_id="123", proc_id="123", bot_status="completed", bot_sucess_message="Processo finalizado", bot_error_message="")
    # if response:
    #     print(response.json())
    #     
    print("Registrando execução da automação")    
    if token:
        register_robot_url = getenv('ROBOTS')
        headers = {
            "Authorization": f"Bearer {token}",
            "UserId": "1"
        }
        
        # Preparar payload para o registro do robô na API
        payload = {
            "aut_id": aut_id,
            "proc_id": proc_id,
            "bot_status": bot_status,
            "bot_sucess_message": bot_sucess_message,
            "bot_error_message": bot_error_message
        }
        
        # Enviar requisição POST para o endpoint
        response = requests.post(register_robot_url, json=payload, headers=headers)
        
        # Verificar o status da resposta
        if response.status_code == 200:
            print("Registro realizado com sucesso")
        else:
            print("Erro ao registrar o Robot")
        
        return response
    else:
        print("Token está vazio. Não é possível registrar a automação.")
        return None
    
def updateFolderId(token, proc_id, folderNameComp):     
    print("Registrando execução da automação")    
    if token:
        url = getenv('PROCESSAUTOMATIONS')
        headers = {
            "Authorization": f"Bearer {token}",
            "UserId": "1"
        }
        
        # Preparar payload para o registro do robô na API
        payload = {
            "proc_id": proc_id,
            "proc_state": 1,
            "proc_msg": "Gerando documentos na estrutura de pasta confomr Proc_Comp_Ref",
            "proc_msg_error": "",
            "proc_comp_ref": folderNameComp
        }        
        # Enviar requisição POST para o endpoint
        response = requests.put(url, json=payload, headers=headers)        
        # Verificar o status da resposta
        if response.status_code == 200:
            print("Registro realizado com sucesso")
        else:
            print("Erro ao registrar o Robot")
        
        return response
    else:
        print("Token está vazio. Não é possível registrar a automação.")
        return None

def updateEmployeesStatusTrue(token, ali_id, brc_id, brr_id):     
    print("Registrando execução da automação")    
    if token:
        url = getenv('UPDATEEMPLOYEES')
        headers = {
            "Authorization": f"Bearer {token}",
            "UserId": "1"
        }
        
        # Preparar payload para o registro do robô na API
        payload = {
            "ali_id": ali_id,
            "brc_id": brc_id,
            "brr_id": brr_id,
        }        
        # Enviar requisição POST para o endpoint
        response = requests.put(url, json=payload, headers=headers)        
        # Verificar o status da resposta
        if response.status_code == 200:
            print("Registro realizado com sucesso")
        else:
            print("Erro ao registrar o Robot")
        
        return response
    else:
        print("Token está vazio. Não é possível registrar a automação.")
        return None


            




