import colorama
from colorama import Fore, Back, Style

# needed to initiate colorama
colorama.init(autoreset=True)

print(Fore.RED + '\nsome red text')
print(Fore.GREEN + '\nsome green text')
print(Style.DIM + '\nThis is dim text')