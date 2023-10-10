import re

# Exemplos de URLs válidas:

# bytebank.com/cambio
# bytebank.com.br/cambio
# www.bytebank.com/cambio
# www.bytebank.com.br/cambio
# http://www.bytebank.com/cambio
# http://www.bytebank.com.br/cambio
# https://www.bytebank.com/cambio
# https://www.bytebank.com.br/cambio

# Exemplos de URLs inválidas:

# https://bytebank/cambio
# https://bytebank.naoexiste/cambio
# ht://bytebank.naoexiste/cambio
# ------------------------------------
# https://www.bytebank.com.br/cambio

url = "https://www.bytebank.com.br/cambio"

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if match:
    print("A url eh valida")
else:
    raise ValueError("a url nao eh valida")