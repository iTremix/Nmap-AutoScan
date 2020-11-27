# -*- coding: utf-8 -*-
from termcolor import colored
import os
def menu():
  green = colored('Verde : Rápido','green')
  yellow = colored('Amarelo : Médio','yellow')
  red = colored('Vermelho : Lento','red')
  um = colored('[1] CTF scans','cyan')
  dois = colored('[2] Scans','cyan')
  usage = colored('Usage : ')
  chaveta = '{'
  chvt = '}'
  banner = '''
                                       
                        i T r e m i x  
                       =============== 

                    ♡ Scans automáticos ♡

                     github.com/iTremix

                     '''

  print(
    f'''{colored(banner,'cyan')}
      ---------------------------------------------------

                        {colored('Color scheme :','magenta')} 

                {chaveta}

                  {green}
                  {yellow}
                  {red}

                {chvt}



                      {um}

      {colored('[1] Scan completo','yellow')}
      {colored('[2] Scan de portas comuns','green')}
      {colored('[3] Portas & Serviços','yellow')}
      {colored('[4] Heartbleed SSL Vulnerability','green')}
      {colored('[5] Obter os Headers (http)','green')}
      


                    {dois}

      {colored('[1] Scan default','green')}
      {colored('[2] Scan de SO','green')}
      {colored('[3] Scan completo w/ -Pn','green')}
      {colored('[4] UDP Scan','yellow')}
      {colored('[5] TCP Scan','yellow')}
      {colored('[6] Descubrir hosts (ping scan)','green')}
      {colored('[7] Ip Info','yellow')}




                          {colored('[99] Sair','magenta')}
  ''')
def um():
  print(f'''
                    {colored('[1] CTF scans','cyan')}

      {colored('[1] Scan completo','yellow')}
      {colored('[2] Scan de portas comuns','green')}
      {colored('[3] Portas & Serviços','yellow')}
      {colored('[4] Heartbleed SSL Vulnerability','green')}
      {colored('[5] Headers','green')}

      ''')
def dois():
  print(f'''
                    {colored('[2] Scans','cyan')}

      {colored('[1] Scan default','green')}
      {colored('[2] Scan de SO','green')}
      {colored('[3] Scan completo w/ -Pn','green')}
      {colored('[4] UDP Scan','yellow')}
      {colored('[5] TCP Scan','yellow')}
      {colored('[6] Descubrir hosts (ping scan)','green')}
      {colored('[7] Ip Info','yellow')}
    ''')
