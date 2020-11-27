# -*- coding: utf-8 -*-
from termcolor import colored
import os
import menu
import time
def clear():
	os.system('clear')
def barra():
	print('====================================')
def scan1():
	ip = input(colored('Insira o ip que quer scanear > ','cyan'))
	barra()
	verb = input(colored('Quer verbose? [S/n] > ','cyan'))
	if verb == 'S' or verb == 's':
		print(colored('[+] Verbose','green'))
		print(colored(f'[+] Alvo : {ip} ','green'))
		print(colored('[+] A começar!','green'))
		output = os.system(f'nmap -A -v {ip}')
		barra()
	elif verb == 'N' or verb =='n':
		print(colored('[+] Verbose','green'))
		print(colored(f'[+] Alvo : {ip} ','green'))
		print(colored('[+] A começar!','green'))
		output = os.system(f'nmap -A {ip}')
		barra()
	fchr = input(colored('[?] Deseja criar um ficheiro do resultado? [S/n] > ','yellow'))
	if fchr == 'S' or fchr == 's':
		nome = input(colored('[?] Quer salvar o ficheiro com que nome > ','cyan'))
		print(colored('[+] A criar um ficheiro do resultado (pode levar um bocado)...','cyan'))
		f = open(nome,'w+')
		f.write(str(os.system(f'nmap -A {ip} > {nome}')))
		print (colored('[+] O ficheiro foi criado na mesma pasta do programa!','cyan'))
		time.sleep(1)
		barra()
		print(colored('~ Bye ^^','cyan'))
		print(colored('github.com/iTremix','blue'))
		exit()
	else:
		barra()
		print(colored('~ Bye ^^','cyan'))
		print(colored('github.com/iTremix', 'red', attrs=['blink']))
		exit()

def scan2():
	ip = input(colored('Insira o ip que quer scanear > ','cyan'))
	barra()
	verb = input(colored('Quer verbose? [S/n] > ','cyan'))
	if verb == 'S' or verb == 's':
		print(colored('[+] Verbose','green'))
		print(colored(f'[+] Alvo : {ip} ','green'))
		print(colored('[+] A começar!','green'))
		output = os.system(f'nmap -F -v {ip}')
		barra()
	elif verb == 'N' or verb =='n':
		print(colored('[+] Verbose','green'))
		print(colored(f'[+] Alvo : {ip} ','green'))
		print(colored('[+] A começar!','green'))
		output = os.system(f'nmap -F {ip}')
		barra()
	fchr = input(colored('[?] Deseja criar um ficheiro do resultado? [S/n] > ','yellow'))
	if fchr == 'S' or fchr == 's':
		nome = input(colored('[?] Quer salvar o ficheiro com que nome > ','cyan'))
		print(colored('[+] A criar um ficheiro do resultado (pode levar um bocado)...','cyan'))
		f = open(nome,'w+')
		f.write(str(os.system(f'nmap -A {ip} > {nome}')))
		print (colored('[+] O ficheiro foi criado na mesma pasta do programa!','cyan'))
		time.sleep(1)
		barra()
		print(colored('~ Bye ^^','cyan'))
		print(colored('github.com/iTremix','blue'))
		exit()
	else:
		barra()
		print(colored('~ Bye ^^','cyan'))
		print(colored('github.com/iTremix', 'red', attrs=['blink']))
		exit()
def scan3():
	ip = input(colored('Insira o ip que quer scanear > ','cyan'))
	barra()
	verb = input(colored('Quer verbose? [S/n] > ','cyan'))
	if verb == 'S' or verb == 's':
		print(colored('[+] Verbose','green'))
		print(colored(f'[+] Alvo : {ip} ','green'))
		print(colored('[+] A começar!','green'))
		output = os.system(f'nmap -sS -sV -v {ip}')
		barra()
	elif verb == 'N' or verb =='n':
		print(colored('[+] Verbose','green'))
		print(colored(f'[+] Alvo : {ip} ','green'))
		print(colored('[+] A começar!','green'))
		output = os.system(f'nmap -sS -sV {ip}')
		barra()
	fchr = input(colored('[?] Deseja criar um ficheiro do resultado? [S/n] > ','yellow'))
	if fchr == 'S' or fchr == 's':
		nome = input(colored('[?] Quer salvar o ficheiro com que nome > ','cyan'))
		print(colored('[+] A criar um ficheiro do resultado (pode levar um bocado)...','cyan'))
		f = open(nome,'w+')
		f.write(str(os.system(f'nmap -A {ip} > {nome}')))
		print (colored('[+] O ficheiro foi criado na mesma pasta do programa!','cyan'))
		time.sleep(1)
		barra()
		print(colored('~ Bye ^^','cyan'))
		print(colored('github.com/iTremix','blue'))
		exit()
	else:
		barra()
		print(colored('~ Bye ^^','cyan'))
		print(colored('github.com/iTremix', 'red', attrs=['blink']))
		exit()
def scan4():
	ip = input(colored('Insira o ip que quer scanear > ','cyan'))
	barra()
	verb = input(colored('Quer verbose? [S/n] > ','cyan'))
	if verb == 'S' or verb == 's':
		print(colored('[+] Verbose','green'))
		print(colored(f'[+] Alvo : {ip} ','green'))
		print(colored('[+] A começar!','green'))
		output = os.system(f'nmap -sV -p 443 --script=ssl-heartbleed.nse {ip}')
		barra()
	elif verb == 'N' or verb =='n':
		print(colored('[+] Verbose','green'))
		print(colored(f'[+] Alvo : {ip} ','green'))
		print(colored('[+] A começar!','green'))
		output = os.system(f'nmap -A {ip}')
		barra()
	fchr = input(colored('[?] Deseja criar um ficheiro do resultado? [S/n] > ','yellow'))
	if fchr == 'S' or fchr == 's':
		nome = input(colored('[?] Quer salvar o ficheiro com que nome > ','cyan'))
		print(colored('[+] A criar um ficheiro do resultado (pode levar um bocado)...','cyan'))
		f = open(nome,'w+')
		f.write(str(os.system(f'nmap -A {ip} > {nome}')))
		print (colored('[+] O ficheiro foi criado na mesma pasta do programa!','cyan'))
		time.sleep(1)
		barra()
		print(colored('~ Bye ^^','cyan'))
		print(colored('github.com/iTremix','blue'))
		exit()
	else:
		barra()
		print(colored('~ Bye ^^','cyan'))
		print(colored('github.com/iTremix', 'red', attrs=['blink']))
		exit()
def scan5():
	ip = input(colored('Insira o ip que quer scanear > ','cyan'))
	barra()
	verb = input(colored('Quer verbose? [S/n] > ','cyan'))
	if verb == 'S' or verb == 's':
		print(colored('[+] Verbose','green'))
		print(colored(f'[+] Alvo : {ip} ','green'))
		print(colored('[+] A começar!','green'))
		output = os.system(f'nmap -sV --script=http-headers {ip}')
		barra()
	elif verb == 'N' or verb =='n':
		print(colored('[+] Verbose','green'))
		print(colored(f'[+] Alvo : {ip} ','green'))
		print(colored('[+] A começar!','green'))
		output = os.system(f'nmap -A {ip}')
		barra()
	fchr = input(colored('[?] Deseja criar um ficheiro do resultado? [S/n] > ','yellow'))
	if fchr == 'S' or fchr == 's':
		nome = input(colored('[?] Quer salvar o ficheiro com que nome > ','cyan'))
		print(colored('[+] A criar um ficheiro do resultado (pode levar um bocado)...','cyan'))
		f = open(nome,'w+')
		f.write(str(os.system(f'nmap -A {ip} > {nome}')))
		print (colored('[+] O ficheiro foi criado na mesma pasta do programa!','cyan'))
		time.sleep(1)
		barra()
		print(colored('~ Bye ^^','cyan'))
		print(colored('github.com/iTremix','blue'))
		exit()
	else:
		barra()
		print(colored('~ Bye ^^','cyan'))
		print(colored('github.com/iTremix', 'red', attrs=['blink']))
		exit()