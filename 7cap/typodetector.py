#! /usr/bin/python
# typodetector.py - programa que procura "erros" de escrita como:    muitos
#                   espaços, palavras palavras acidentalmente repetidas ou 
#                   muitos !!!! ou ???? e as devolve sem esses erros pro cli#                   pboard. 
import pyperclip, re

#regexes
espacosRegex = re.compile(r'(\s){2,}') #
palavras_repetidasRegex =  re.compile(r'\b(\w+)\s\1') #
exclamacaoRegex = re.compile(r'(\?)\1')
interrogacaoRegex = re.compile(r'(\!)\1')

#pegar o texto do clipboard
text = str(pyperclip.paste())

#substitui os espaços repetidos por espaços simples
text = espacosRegex.sub(' ',text)
print('Espaços repetidos apagados!')

#"apaga" as !! repetidas
while exclamacaoRegex.findall(text) != []:
    text = exclamacaoRegex.sub(r'\1',text)
print('Exclamacoes repetidas apagadas!')

#"apaga as ?? repetidas
while interrogacaoRegex.findall(text) != []:
    text = interrogacaoRegex.sub(r'\1',text)
print('Interrogacoes repetidas apagadas!')

#"apaga" as palavras repetidas
while palavras_repetidasRegex.findall(text) != []:
    text = palavras_repetidasRegex.sub(r'\1', text)
print('Palavras repetidas apagadas!')

#joga o texto alterado de volta ao clipboard
pyperclip.copy(text)
print('Copiado para o clipboard:')
