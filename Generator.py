import random
import string
import requests
from colorama import Fore
import numba
numba.jit()
print(Fore.MAGENTA + "██████╗██████╗  █████╗ ██╗   ██╗ ██████╗ ██╗      █████╗       ")
print("██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝██╔═══██╗██║     ██╔══██╗   ")
print("██║     ██████╔╝███████║ ╚████╔╝ ██║   ██║██║     ███████║ ")
print("██║     ██╔══██╗██╔══██║  ╚██╔╝  ██║   ██║██║     ██╔══██║ ")
print("╚██████╗██║  ██║██║  ██║   ██║   ╚██████╔╝███████╗██║  ██║ ")
print("╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ")
print('')
print(Fore.LIGHTWHITE_EX + '1 = PLAYSTATION')
print(Fore.LIGHTWHITE_EX + '2 = XBOX')
print('')
q = input('Choose an option: ')
if q == '1':
 inputnum = input(Fore.MAGENTA + "How Many Gift-Cards Would You Like To Generate?: ")
 num = int(inputnum)
 for x in range(num):
  print("")
  amnt = str(random.choices(string.ascii_uppercase + string.digits, k=12))
  url = "https://playstation.com/api/redeem/" + amnt
  amnt1 = amnt.replace('[', '')
  amnt2 = amnt1.replace(']', '')
  amnt3 = amnt2.replace("'", '')
  amnt4 = amnt3.replace(',', '')
  amnt0 = amnt4.replace(' ', '')
  s = requests.post(url)
  if s == 200:
   print(f"{Fore.GREEN} Valid | {amnt0}")
  else:
   print(f"{Fore.RED} Invalid | {amnt0}")
if q == '2':
 chars = 'BCDFGHJKMNPQRTVWXYZ2346789'
 inpnum = input(Fore.MAGENTA + "How Many Gift-Cards Would You Like To Generate?: ")
 nmb = int(inpnum)
 for x in range(nmb):
  print("")
  amount = str(random.choices(chars + string.digits, k=25))
  link = "https://microsoft.com/api/entitlements/redeem/" + amount
  amount1 = amount.replace('[', '')
  amount2 = amount1.replace(']', '')
  amount3 = amount2.replace("'", '')
  amount4 = amount3.replace(',', '')
  amount0 = amount4.replace(' ', '')
  s = requests.get(link)
  if s == 200:
   print(f"{Fore.GREEN} Valid | {amount0}")
  else:
   print(f"{Fore.RED} Invalid | {amount0}")
