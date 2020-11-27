# -*- coding: utf-8 -*-
from termcolor import colored
import os
import menu
import scan
import scan2
import time

if os.name == 'nt':
	print(colored('!!  AVISO  !!', 'red', attrs=['blink']))
	print(colored('ESTE SCRIPT FOI FEITO PARA LINUX!','red'))
	barra()
	print(colored('~ Bye ^^','cyan'))
	print(colored('github.com/iTremix', 'red', attrs=['blink']))
	exit()
if not os.geteuid() == 0:
    print(colored("\nEste script só pode ser corrido como root!\n",'red'))
    exit()

def clear():
	os.system('clear')
def barra():
	print('====================================')
os.system('clear')
clear()
menu.menu()
while True:
	print(colored('Selecione primeiro o numero do tipo de scan que quer realizar...','cyan'))
	escolha = input(colored('TIPO > ','green'))
	if escolha == '1':
		clear()
		menu.um()
		while True:
			real = input(colored('Qual scan quer realizar > ','cyan'))
			if real == '1':
				scan.scan1()
			if real == '2':
				scan.scan2()
			if real == '3':
				scan.scan3()
			if real == '4':
				scan.scan4()
			if real == '5':
				scan.scan5()
	elif escolha == '2':
		clear()
		menu.dois()
		while True:
			real = input(colored('Qual scan quer realizar > ','cyan'))
			if real == '1':
				scan2.scan11()
			if real == '2':
				scan2.scan22()
			if real == '3':
				scan2.scan33()
			if real == '4':
				scan2.scan44()
			if real == '5':
				scan2.scan55()
			if real == '6':
				scan2.scan66()
			if real == '7':
				scan2.scan77()
	elif escolha == '99':
		barra()
		print(colored('~ Bye ^^','cyan'))
		print(colored('github.com/iTremix', 'red', attrs=['blink']))
		exit()
	else:
		print(colored('Por favor insira um opção válida.','red'))
		#break