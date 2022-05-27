import requests
import configparser
import os
import sys
from .log import *

path = os.path.dirname(os.path.realpath(sys.argv[0]))
cfgfile = os.path.join(path, 'config.ini')

if (os.path.isfile(cfgfile)):
    cfg = configparser.RawConfigParser()
    cfg.read(cfgfile)
else:
    print("O arquivo de configuração config.ini não foi encontrado.")
    quit()

BASE_URL = cfg.get('services', 'base_url')
TOKEN = cfg.get('services', 'token')

my_headers = {
    'Authorization': f"Bearer {TOKEN}",
    'Content-Type': 'application/json'
}

def api_get_all(service):
    try:
        response = requests.get(BASE_URL + service, headers=my_headers)
        if (response.status_code == 200):
            return response.text
    except requests.exceptions.HTTPError as errh:
        send_log_critical("Ocorreu um erro HTTP ao realizar a requisição: " + repr(errh))
        return
    except requests.exceptions.ConnectionError as errc:
        send_log_critical("Ocorreu um erro de conexão ao realizar a requisição: " + repr(errc))
        return
    except requests.exceptions.Timeout as errt:
        send_log_critical("O tempo de conexão foi esgotado: " + repr(errt))
        return
    except requests.exceptions.RequestException as err:
        send_log_critical("Ocorreu um erro desconhecido ao realizar a requisição: " + repr(err))
        return 

def api_get_item(service, id):
    try:
        response = requests.get(BASE_URL + service + f"/{id}", headers=my_headers)
        if (response.status_code == 200):
            return response.text
    except requests.exceptions.HTTPError as errh:
        send_log_critical("Ocorreu um erro HTTP ao realizar a requisição: " + repr(errh))
        return
    except requests.exceptions.ConnectionError as errc:
        send_log_critical("Ocorreu um erro de conexão ao realizar a requisição: " + repr(errc))
        return
    except requests.exceptions.Timeout as errt:
        send_log_critical("O tempo de conexão foi esgotado: " + repr(errt))
        return
    except requests.exceptions.RequestException as err:
        send_log_critical("Ocorreu um erro desconhecido ao realizar a requisição: " + repr(err))
        return 

def api_post(service, content):
    try:
        response = requests.post(BASE_URL + service, json = content, headers = my_headers)
        if (response.status_code != 204):
            return {
                "code": response.status_code,
                "mensagem": response.json()
            }
        elif (response.status_code == 503):
            send_log_critical("O serviço está temporariamente indisponível.")
            return
        else:
            return {
                "code": response.status_code
            }
    except requests.exceptions.HTTPError as errh:
        send_log_critical("Ocorreu um erro HTTP ao realizar a requisição: " + repr(errh))
        return
    except requests.exceptions.ConnectionError as errc:
        send_log_critical("Ocorreu um erro de conexão ao realizar a requisição: " + repr(errc))
        return
    except requests.exceptions.Timeout as errt:
        send_log_critical("O tempo de conexão foi esgotado: " + repr(errt))
        return
    except requests.exceptions.RequestException as err:
        send_log_critical("Ocorreu um erro desconhecido ao realizar a requisição: " + repr(err))
        return 

def api_put(service, id, content):
    try:
        response = requests.post(BASE_URL + service, json = content, headers = my_headers)
        if (response.status_code != 204):
            return {
                "code": response.status_code,
                "mensagem": response.json()
            }
        elif (response.status_code == 503):
            send_log_critical("O serviço está temporariamente indisponível.")
            return
        else:
            return {
                "code": response.status_code
            }
    except requests.exceptions.HTTPError as errh:
        send_log_critical("Ocorreu um erro HTTP ao realizar a requisição: " + repr(errh))
        return
    except requests.exceptions.ConnectionError as errc:
        send_log_critical("Ocorreu um erro de conexão ao realizar a requisição: " + repr(errc))
        return
    except requests.exceptions.Timeout as errt:
        send_log_critical("O tempo de conexão foi esgotado: " + repr(errt))
        return
    except requests.exceptions.RequestException as err:
        send_log_critical("Ocorreu um erro desconhecido ao realizar a requisição: " + repr(err))
        return 

def api_db_delete(service, id):
    try:
        response = requests.db_delete(BASE_URL + service + f"/{id}", headers=my_headers)
        if (response.status_code == 200 or response.status_code == 204):
            return response.text
    except requests.exceptions.HTTPError as errh:
        send_log_critical("Ocorreu um erro HTTP ao realizar a requisição: " + repr(errh))
        return
    except requests.exceptions.ConnectionError as errc:
        send_log_critical("Ocorreu um erro de conexão ao realizar a requisição: " + repr(errc))
        return
    except requests.exceptions.Timeout as errt:
        send_log_critical("O tempo de conexão foi esgotado: " + repr(errt))
        return
    except requests.exceptions.RequestException as err:
        send_log_critical("Ocorreu um erro desconhecido ao realizar a requisição: " + repr(err))
        return 