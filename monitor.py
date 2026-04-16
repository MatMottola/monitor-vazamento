import requests
import json
import csv
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("HIBP_API_KEY")

BASE_URL = "https://haveibeenpwned.com/api/v3"
HEADERS = {
    "User-Agent": "MonitorVazamento-Estudo/1.0",
    "hibp-api-key": API_KEY
}


def verificar_email(email):
    print(f"\n🔍 Consultando: {email}")
    print("-" * 40)

    url = f"{BASE_URL}/breachedaccount/{email}?truncateResponse=false"

    try:
        resposta = requests.get(url, headers=HEADERS)

        if resposta.status_code == 200:
            vazamentos = resposta.json()
            print(f"{len(vazamentos)} vazamento(s) encontrado(s):\n")

            for item in vazamentos:
                print(f" {item['Title']}")
                print(f" Data   : {item['BreachDate']}")
                print(f" Afetados: {item['PwnCount']:,}")
                print(f" Descrição: {item['Description'][:80]}...")
                print()

        elif resposta.status_code == 404:
            print("Nenhum vazamento encontrado para este e-mail!")

        elif resposta.status_code == 401:
            print("API Key inválida. Verifique o arquivo .env")

        elif resposta.status_code == 429:
            print("Muitas requisições. Aguarde um momento e tente novamente.")

        else:
            print(f"Resposta inesperada: {resposta.status_code}")

    except Exception as e:
        print(f"Erro de conexão: {e}")

email_teste = input("Digite o e-mail para consultar: ")
verificar_email(email_teste)