from datetime import datetime
import psutil
from os import system
from time import sleep

def banner():
    system('cls')
    print(
        '''
   __            __           
  / /____  _____/ /____  _____
 / __/ _ \/ ___/ __/ _ \/ ___/
/ /_/  __(__  ) /_/  __/ /    
\__/\___/____/\__/\___/_/-gp
         kinite-gp
        '''
    )
    
def writeout(target,text):
        file = open(target,'a')
        file.write(f'{text}\n')
        file.close()

def analises():
    battery = psutil.sensors_battery()
    var = datetime.now()
    timedate = var.strftime("%Y/%m/%d %H:%M:%S")

    textlog = f'''date&time: {timedate}\nbattry: {battery.percent}%\nplugged: {battery.power_plugged}\ncpu: {psutil.cpu_percent(4)}%\nram: {psutil.virtual_memory()[2]}%\n----------------------------------'''
    return textlog
    
while True:
    banner()
    dt = analises()
    print(dt)
    writeout('tester-gp.txt',dt)
    sleep(45)