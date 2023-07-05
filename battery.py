import psutil , time
from os import system
from plyer import notification
from colorama import Fore, Style

# Set the colors
green = Fore.GREEN
red = Fore.RED
style_reset =Style.RESET_ALL

# Symbols
simbol_ok = f'[{green}+{style_reset}]'
simbol_fail = f'[{red}-{style_reset}]'
simbol_exclamation = f'[{red}!{style_reset}]'



def limparTela():
    system('cls')

def check():
    '''
    Check if the battery is 100% and if it is connected to the power supply    
    '''
    try:
        battery   = psutil.sensors_battery()
    except:
        print(f'{simbol_fail} Erro ao verificar a bateria')
        battery = None
    try:
        plugged = battery.power_plugged
    except:
        print(f'{simbol_fail} Erro ao verificar se está conectado')
             
    percent = int(battery.percent)
    isplugged = f"{simbol_ok} Conectado" if plugged==True else f"{simbol_fail} Desconectado"
    print(f'{simbol_ok} Bateria   -> {percent}')

    if (percent == 100) and (plugged==True):
        notification.notify(title='Bateria  100%',message='A bateria está completamente carregada',timeout=100)
        system('shutdown /s /t 0"')
        input()
        return True
    return False



def run(mode:bool,minutes_to_wait:int=5):
    while mode==True:
        limparTela()
        print('======== Battery Saver ========\n ')
        check()
        print()
        print(f'{simbol_exclamation} Verificando a cada {minutes_to_wait}min ...')
        time.sleep(minutes_to_wait*60)
        check()

if __name__ == '__main__':
    system('title Battery Saver')
    run(True,10)

