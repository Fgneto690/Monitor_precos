import csv
import os
from thefuzz import fuzz
from serpapi import GoogleSearch


# 1 CONFIG INICIAL
API_KEY = os.getenv("SERAPI_KEY", "SUA CHAVE AQUI")
PRODUTO_ALVO = "RTX 4060"

def buscar_e_comparar(query):
    params = {
        "engine": "google_shopping",
        "q": query,
        "hl": "pt",
        "gl": "br",
        "api_key": API_KEY
    }

    pesquisa = GoogleSearch(params)
    resultado = pesquisa.get_dict()

    #Pegamos a lista de resultado do Google Shopping
    shopping_results = resultado.get("shopping_results", [])

    if not shopping_results:
        print("Nenhum resultado encontrado")
        return
    
    lista_final = []
    
    for item in shopping_results:
        nome = item.get("title")
        preco = item.get("extracted_price"),
        loja = item.get("source")
        rating = item.get("rating", 0) #se não tiver rating assume como sendo 0
        #logica da similaridade do nome
        similaridade = fuzz.partial_ratio(query.lower(), nome.lower())
        #Filtro de similaridade
        if similaridade > 70:
            lista_final.append([nome, preco, loja, rating]) # Salvando como lista para o CSV
    lista_final.sort(key=lambda x: x[1]) #organizando por preço antes de salvar
    
    with open("relatorio_precos.csv", mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Produto', 'Preço', 'Loja', 'Rating'])
        escritor.writerows(lista_final)
    print("Arquivo criado com sucesso")

buscar_e_comparar(PRODUTO_ALVO)