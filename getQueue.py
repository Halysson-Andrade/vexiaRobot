from os import getenv
from dotenv import load_dotenv 
import requests
import sys
load_dotenv()

def processar():
    # Capturando dados para processamento
    #########################################
    portalUrl = getenv('LOGIN')
    userPortal= getenv('USER')
    passwordPortal= getenv('PASSWORD')
    # Login na API
    #########################################
    payload = {
        "email": userPortal,
        "password": passwordPortal
    }
    response = requests.post(portalUrl, json=payload)

    if response.status_code == 200:
        # Capturando token
        #########################################
        print("Logando para buscar Fila")
        response_data = response.json()  
        data_field = response_data.get("data")     
        token = data_field.get("token")  
        if token != '':
            # Login executado com sucesso
            #########################################
            print("Capturando Fila")
            getQueue = getenv('GETQUEUE')
            headers = {
            "Authorization": f"Bearer {token}",
            "UserId": "1"
            }
            # EndPoint Validando Fila
            #########################################
            queueResponse = requests.get(getQueue, headers=headers)
            if queueResponse.status_code == 200:
                # Fila para execução
                #########################################
                queue_data = queueResponse.json()  
                data_result = queue_data.get("data")  
                print("Validando resultado da Fila")   
                if len(data_result):
                    # Execução da Fila
                    #########################################
                    for item in data_result:
                    # Execute ações com cada 'item' em data_result
                        ali_id = str(item.get('ali_id', ''))
                        print("Buscando Parâmetros para execução")   
                        getParams = getenv('GETPARAMS')
                        getParams = getParams+ali_id
                        headers = {
                            "Authorization": f"Bearer {token}",
                            "UserId": "1"
                        }
                        paramsResponse = requests.get(getParams, headers=headers)
                        if paramsResponse.status_code == 200:
                            params_data = paramsResponse.json()  
                            params_result = params_data.get("data")  
                            if len(params_result):
                                print("Execução realizada com sucesso!")  
                                return params_result
                            else:
                                return processar()
                        else:
                            return processar() 
                else:
                    return processar()
            else:
                return processar() 
        else:
            return processar()       
    else:
        return processar()  