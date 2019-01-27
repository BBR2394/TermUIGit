#!/usr/local/bin/python3

import os
import sys
import string
import curses
from time import sleep
import json

langFileName = "langFile.json"
langFIle = None
repoFile = None
langJson = None
repoJson = None
sysLang = "en"
langStorage = None

def print_file(fl):
	print("dans print file")
	print(fl.read())

def select_language(tabLang):
	i = 0
	defaultEN = None
	print("dans select language")
	print(len(tabLang))
	while i < len(tabLang) and sysLang != tabLang[i]['code']:
		print(tabLang[i]['test'])
		if tabLang[i]['code'] == 'en':
			defaultEN = tabLang[i]
		i += 1
	
	if i == len(tabLang) :
		#there was no language for the sys lang so take en default
		langStorage = defaultEN
	elif i < len(tabLang):
		langStorage = tabLang[i]

	if langStorage == None:
		raise Exception('language', 'there is no language selected. no default could be selected')
	#print("fin de lang choisi")
	print(langStorage['test'])


def open_lang_file():
	try:
		langFile = open(langFileName, 'r')
		#print("lang file opened")
		data = langFile.read()
		print(data)
	except Exception as inst:
		#print(type(inst))
		#print(inst.args)
		#print(inst)
		print('-> an error occured when openfing the file', sys.stderr)
		return False
	try:
		langJson = json.loads(data)
		#print(langJson)
	except Exception as inst:
		print('-> probleme with json file lang', sys.stderr)

	#print("jessaye de voir pour afficher le json")
	#print(langJson['Languages'])
	#print(langJson['Languages'][0]['code'])
	#print(langJson['Languages'][1]['code'])
	select_language(langJson['Languages'])

def print_repo_file():
	print("=>dans print repo file")
	print(repoJson)
	print(repoJson['repo'])
	print(repoJson['repo']['epitech'])
	print(repoJson['repo']['github'])
	print(repoJson['repo']['epitech']['tek1'])
	print(repoJson['repo']['epitech']['tek2'])
	print(repoJson['repo']['epitech']['tek2']['piscineCpp'])

def open_repo_file():
	global repoJson
	try:
		repoFile = open('repoList.json', 'r')
		print("le fichier est ouvert")
		data = repoFile.read()
		print(data)
	except Exception as inst:
		print(type(inst))
		print(inst.args)
		print(inst)
		print(langStorage['erOpenFile'])
		return False
	try:
		repoJson = json.loads(data)
	except Exception as inst:
		print('-> probleme with json file repo', sys.stderr)
	print_repo_file()

def clone_repo():
	global repoJson
	print("in the clone funtion")
	print(repoJson['repo']['github']['tous'])
	

def stop_curse_window(cuvar):
	curses.nocbreak()
	cuvar.keypad(False)
	curses.echo()
	curses.endwin()
	print("- fin du curse -")

def start_curse_window(cvar):
	print("*dans start curse win*")
	cvar = curses.initscr()
	curses.noecho()
	curses.cbreak()
	cvar.keypad(True)
	return cvar
	

print("* Debut du script *")
print("* démarrage dans *")
# sleep(0.5)
# print("3")
# sleep(0.5)
# print("2")
# sleep(0.5)
# print("1")

print(sys.argv)
open_lang_file()
open_repo_file()
clone_repo()
#curseVar = None
#curseVar = start_curse_window(curseVar)
#stop_curse_window(curseVar)

