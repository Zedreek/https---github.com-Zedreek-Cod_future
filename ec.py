import keyboard as keyb
import time

print('До в ключения 20 сек!!!')
time.sleep(20)
print('Старт!!!')
sc = 0
while True:
    keyb.press('b')
    time.sleep(1)
    keyb.release('b')
    time.sleep(17)
    # keyb.press('2')
    # time.sleep(3)
    # keyb.release('2')
    # keyb.press('1')
    # time.sleep(0.1)
    # keyb.release('1')
    # time.sleep(480)
    # sc+=1
    # print('Итерация -', sc)b