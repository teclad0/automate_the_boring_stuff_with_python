#! /usr/bin/python3
# madlibs.py - reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. 

import os, re
name_file = input('File name:: ')
file = open(f'{name_file}.txt','r')
content = file.read()

adjective_reg = re.compile(r'\bADJECTIVE\b') 
noun_reg = re.compile(r'\bNOUN\b') 
verb_reg = re.compile(r'\bVERB\b') 

while adjective_reg.findall(content) != []:
    adjective_sub = input('Enter an adjective:\n')
    content = adjective_reg.sub(adjective_sub, content, 1)

while noun_reg.findall(content) != []:
    noun_sub = input('Enter a noun:\n')
    content = noun_reg.sub(noun_sub, content, 1)

while verb_reg.findall(content) != []:
    verb_sub = input('Enter a verb:\n')
    content = verb_reg.sub(verb_sub, content, 1)

file.close()

file = open(f'{name_file}.txt','w')
file.write(content)

file.close()
