import re

def valida_url(url):
    modelo = "(http://|https://)?(www\.)?\w+\.com(\.\w{3})?/[a-z]*\?v=.+"
    resposta = re.match(modelo, url)
    return resposta

print(valida_url('https://www.youtube.com/watch?v=-PUy9AEM72Q'))

    # https://www.youtube.com/watch?v=_loRrBA9EpY&ab_channel=PauloJubilut

    # modelo = '[\(]?[0-9]{2}[\)]?[ ]?(9)?[0-9]{4}[\-| ]?[0-9]{4}'
    # resposta = re.findall(modelo, celular)
    # return resposta