import pyautogui as pg
import PIL
import time

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format + '\n')
        time.sleep(1)
        num_of_secs -= 1
        
    print('Countdown finished.')

resposta = int(input('Digite o tempo em segundos: '))
while True:
    valor = countdown(resposta)
    if valor == None:
        pg.click(1083,661)
        pg.write('!points')
        pg.press('enter')
