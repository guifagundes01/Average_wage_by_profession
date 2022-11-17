from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
import pandas as pd
import unidecode
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from pathlib import Path
import json

def cbo_ocupacao(ocupacao, str_ocupacao):
	cbo = ocupacao.loc[lambda ocupacao: ocupacao['TITULO'] == str_ocupacao, 'CODIGO'].values.item()
	return cbo

def string_ocupacao(ocupacao, cbo):
	str_ocup = ocupacao.loc[lambda ocupacao: ocupacao['CODIGO'] == cbo, 'TITULO'].values.item()
	return str_ocup

def media_salarial(ocupacao, str_ocupacao):
	cbo = cbo_ocupacao(ocupacao, str_ocupacao)
	formatted_str_ocupacao = format_str_ocupacao(str_ocupacao)
	media_salario = web_scrapping(formatted_str_ocupacao, cbo)
	return media_salario

def format_str_ocupacao(str_ocupacao):
	formatted_str_ocupacao = str_ocupacao.lower()
	formatted_str_ocupacao = unidecode.unidecode(formatted_str_ocupacao)
	formatted_str_ocupacao = formatted_str_ocupacao.replace(" ", "-")
	formatted_str_ocupacao = formatted_str_ocupacao.replace("(", "")
	formatted_str_ocupacao = formatted_str_ocupacao.replace(")", "")
	return formatted_str_ocupacao	

def web_scrapping(formatted_str_ocupacao, cbo):
	url = "https://www.salario.com.br/profissao/{}-cbo-{}/".format(formatted_str_ocupacao, cbo)
	page = requests.get(url, timeout=10)
	soup = BeautifulSoup(page.text, 'html.parser')
	salario = soup.find_all('td', attrs={'data-label': 'Salário Mensal'})[2]
	return salario.text


@require_http_methods(['GET'])
def cbo_detail(request, cbo):
    base_path = Path(__file__).parent
    file_path = (base_path.name + "/api/data/CBO2002 - Ocupacao.csv")
    ocupacao = pd.read_csv(file_path, sep=';', encoding='latin-1', dtype=str)

    if (cbo in ocupacao['CODIGO'].values):
        str_ocupacao = string_ocupacao(ocupacao, cbo)
        media = media_salarial(ocupacao, str_ocupacao)
    elif (cbo in ocupacao['TITULO'].values):
        str_ocupacao = cbo
        cbo = cbo_ocupacao(ocupacao, str_ocupacao)
        media = media_salarial(ocupacao, str_ocupacao)
    else:
        return HttpResponseNotFound("error")
    
    media = "R$ " + media
    data = {
		"Profissão": str_ocupacao,
		"Média salarial": media,
		"Código da CBO": cbo,
	}

    return JsonResponse({'data': data})