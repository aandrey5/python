# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color
from time import sleep
from colorama import Fore


class TrafficLight:

    def div(self):
        print('*'*60)

    __color = ['red', 'yellow', 'green', 'yellow']


    def running(self):
        TrafficLight.div(self)
        print('ПРОГРАММА - СВЕТОФОР\nНачинаем через 3 сек...')
        TrafficLight.div(self)
        sleep(3)


        while True:
            print('\n' * 99999)
            print(Fore.RED, TrafficLight.__color[0])
            sleep(7)
            print('\n'*99999)
            print(Fore.YELLOW, TrafficLight.__color[1])
            sleep(2)
            print('\n'*99999)
            print(Fore.GREEN, TrafficLight.__color[2])
            sleep(7)
            print('\n'*99999)
            print(Fore.YELLOW, TrafficLight.__color[3])
            sleep(2)
            print('\n'*99999)



svetofor = TrafficLight()
svetofor.running()




