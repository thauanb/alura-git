from os import system
import time
import psutil
from plyer import notification
from colorama import Fore, Style

COLOR_GREEN = Fore.GREEN
COLOR_RED = Fore.RED
COLOR_YELLOW = Fore.YELLOW
STYLE_RESET = Style.RESET_ALL

SIMBOL_OK = f'[{COLOR_GREEN}+{STYLE_RESET}]'
SIMBOL_FAIL = f'[{COLOR_RED}-{STYLE_RESET}]'
SIMBOL_LOADING = f'[{COLOR_RED}.{STYLE_RESET}]'
SYMBOL_EXCLAMATION = f'[{COLOR_RED}!{STYLE_RESET}]'


def limpar_tela() -> None:
    system('cls')


def check() -> bool:
    '''
    Check if the battery is 100% and if it is connected to the power supply    
    '''
    try:
        battery = psutil.sensors_battery()
    except:
        print(f'{SIMBOL_FAIL} Erro ao verificar a bateria')
        battery = None
    try:
        plugged = battery.power_plugged
    except:
        print(f'{SIMBOL_FAIL} Erro ao verificar se está conectado')

    percent = int(battery.percent)
    isplugged = f"{SIMBOL_OK} Conectado" if plugged == True else f"{SIMBOL_FAIL} Desconectado"
    
    if (percent <= 50):
        print(f'{SYMBOL_EXCLAMATION} Bateria {COLOR_RED}{percent}{STYLE_RESET} %')
    elif (percent > 50):
        print(f'{SIMBOL_LOADING} Bateria {COLOR_YELLOW}{percent}{STYLE_RESET} %')

    if (percent == 100) and (plugged == True):
        notification.notify(
            title='Bateria  100%', message='A bateria está completamente carregada', timeout=100)
        system('shutdown /s /t 0"')
        input()
        return True
    return False


def run(mode: bool, minutes_to_wait: int = 5):
    while mode == True:
        limpar_tela()
        print('======== Battery Saver ========\n ')
        check()
        print(f'{SYMBOL_EXCLAMATION} Verificando a cada {minutes_to_wait}min ...')
        time.sleep(minutes_to_wait*60)
        check()
        
system('title Battery Saver')
run(True, 10)
