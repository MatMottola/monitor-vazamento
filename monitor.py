import requests
import json
import csv

base_url = "https://haveibeenpwned.com/api/v3"
Headers = {"User-Agent": "MonitorVazamento-Estudo/1.0"}

def verificar_email(email):
    print(f"\n Consultando {email}")

    url = f'{base_url}/breachedaccount/{email}'


    try:
        resposta = requests.get(url, headers=Headers)
        print(f" Status da resposta: {resposta.status_code}")
        print(f" Conteúdo bruto: {resposta.text}")
    except Exception as e:
        print(f" Erro: {e}")

email_teste = "test@example.com"
verificar_email(email_teste) 

