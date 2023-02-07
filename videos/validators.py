import re

def valida_url(url):
    modelo = "(http://|https://)?(www\.)?\w+\.com(\.\w{3})?/[a-z]*\?v=.+"
    resposta = re.match(modelo, url)
    return resposta
