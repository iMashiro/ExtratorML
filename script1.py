#1 - Definir pacotes
#2 - Definir sintaxes
#3 - Minerar todos os repositorios com python (1000) 
#4 - Buscar sintaxes dentro dos repositorios
import json, requests


# Definindo pacotes

raw_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0,10):
    
    response = requests.get("https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc&per_page=100&page=" + str(i+1))

    raw_data[i] = response.json()

data = {}
data['repository'] = []
for i in raw_data:
    for j in i['items']:
        data['repository'].append({'name': j['name'], 'link': j['html_url']})

# Definindo Sintaxes

# TensorFlow, Theano, Scikit-learn, Caffe, H2O, Amazon Machine Learning, Torch, Google Cloud ML Engine,
# Azure ML Studio, Spark ML lib, PyTorch

# Formas comuns de import em python: 

# from package import resource
# import package
# import package as name
