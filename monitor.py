import requests
import json
import csv
import os
import argparse
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("HIBP_API_KEY")

BASE_URL = "https://haveibeenpwned.com/api/v3"
HEADERS = {
    "User-Agent": "MonitorVazamento-Estudo/1.0",
    "hibp-api-key": API_KEY
}

def validar_configuracao():
    if not API_KEY:
        print("API Key não encontrada! Verifique o arquivo .env")
        exit(1)
    print("Configuração validada.")

def verificar_email(email):
    print(f"\n Consultando: {email}")
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
            return vazamentos

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

def gerar_relatorio(email, vazamentos):
    if not vazamentos:
        print("Nenhum dado para salvar.")
        return 

    
    timestamp = datetime.now().strftime("%Y/%m/%d _%H%M%S")
    nome_arquivo = f"relatorio_{timestamp}.csv"

    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Email", "Serviço", "Data do Vazamento", "Total Afetados", "Descrição"])

        for item in vazamentos:
            writer.writerow([
                email,
                item["Title"],
                item["BreachDate"],
                item["PwnCount"],
                item["Description"][:100]
            ])

    print(f"\nRelatório salvo: {nome_arquivo}")

def main ():
    parser = argparse.ArgumentParser(
        description= "Monitor de Vazamento de Dados"
    )
    
    parser.add_argument(
        "emails",
        nargs = '+',
        help = "Um ou mais e-mail para consultar"
    )
    args = parser.parse_args()

    validar_configuracao()

    resultados = {}

    for email in args.emails:
        vazamentos = verificar_email(email)
        if vazamentos:
            resultados[email] = vazamentos


    for email, vazamentos in resultados.items():
        gerar_relatorio(email, vazamentos)


if __name__ == "__main__":
    main()
