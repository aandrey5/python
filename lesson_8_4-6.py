# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
def dv():
    print('=' * 150)

class NoDigit(Exception):
    def __init__(self, txt):
        self.txt = txt

dv()
print('СКЛАД ОРГТЕХНИКИ V1.0')
dv()


# -------------------------классы оргтезники______________--

class OfficeEquipment:
    def __init__(self, id, model, year, made_in):
        self.trade_name = id
        self.year = year
        self.made_in = made_in
        self.model = model
        # print(f'Trade name = {trade_name}, Manufacture year = {year}, Made in = {made_in}')


class Printer(OfficeEquipment):
    def __init__(self, id, model, year, made_in, is_color=False):
        super(Printer, self).__init__(id, model, year, made_in)
        self.is_color = is_color
        print(f'СОЗДАН PRINTER: ID = {id}, Модель = {model}, Manufacture year = {year}, Made in = {made_in}, '
              f'Цветной принтер? = {is_color}')
        self.printer_obj = [id, 'PRINTER', model, year, made_in, is_color]


class Scaner(OfficeEquipment):
    def __init__(self, id, model, year, made_in, dpi=1200):
        super(Scaner, self).__init__(id, model, year, made_in)
        self.dpi = dpi
        print(f'СОЗДАН SCANNER: ID = {id}, Модель = {model}, Manufacture year = {year}, Made in = {made_in}, '
              f'Разрешение = {dpi}')
        self.scaner_obj = [id, 'SCANNER', model, year, made_in, dpi]


class Xerox(OfficeEquipment):
    def __init__(self, id, model, year, made_in, is_laser=True, is_color=False):
        super(Xerox, self).__init__(id, model, year, made_in)
        self.is_laser = is_laser
        self.is_color = is_color
        print(f'СОЗДАН COPIER: ID = {id}, Модель = {model}, Manufacture year = {year}, Made in = {made_in}, '
              f'Лазерный[да/нет] = {is_laser}, Цветной = [да/нет] = {is_color}')
        self.xerox_obj = [id, 'COPIER', model, year, made_in, is_laser, is_color]


# ---------------пример классов отргтехники,проверка------------------

print('ПРИМЕРЫ КЛАССОВ')
dv()
hp_laserjet = Scaner(1001, 'hp_laserjet', 2019, 'China')

samsung_ml_4700 = Printer(1002, 'Samsung_ml_4700', 2020, 'Malaysia', True)

hp_scanjet_1250 = Scaner(1003, 'HP_scanjet_1250', 2019, 'Japan', 4500)

brother_dcx_7500 = Xerox(1004, 'Brother_dcx_7500', 2020, 'Japan', True)
dv()

#---------------- складской блок ---------------------------------

class Warehouse:
    warehouse_main = []
    warehouse_nord = []
    warehouse_damaged = []

    whses = {'1': warehouse_main, '2': warehouse_nord, '3': warehouse_damaged}

    @staticmethod
    #ПОСТУПЛЕНИЕ ТОВАРА
    def eq_income():
        ask = int(input('Введите тип новой номенклатуры: 1 - принтер, 2 - сканер, 3 - копир: '))
        if ask == 1:
            obj = Printer(
                input('Введите id: '),
                input('Введите модель: '),
                input('Введите год: '),
                input('Введите страну производства: '),
                bool(input('Введите True (0) если цветной: '))
            )
            try:

                ask_quant = input('Введите количество шт.: ')
                if ask_quant.isdigit() == False:
                    raise NoDigit('\n!!! Вы ввели текстовое значение !!!\n')
                else:
                    ask_quant = int(ask_quant)
                    print(obj.printer_obj)
                    Warehouse.warehouse_main.append(
                        {"id": obj.printer_obj[0], "param": obj.printer_obj[1:], "quant": ask_quant})
                    print(Warehouse.warehouse_main)

            except NoDigit as err:
                print(err)



        elif ask == 2:
            obj = Scaner(
                input('Введите id: '),
                input('Введите модель: '),
                input('Введите год: '),
                input('Введите страну производства: '),
                int(input('Введите dpi (300 - 4500): '))
            )
            try:

                ask_quant = input('Введите количество шт.: ')
                if ask_quant.isdigit() == False:
                    raise NoDigit('\n!!! Вы ввели текстовое значение !!!\n')
                else:
                    ask_quant = int(ask_quant)
                    print(obj.scaner_obj)
                    Warehouse.warehouse_main.append(
                        {"id": obj.scaner_obj[0], "param": obj.scaner_obj[1:], "quant": ask_quant})
                    print(Warehouse.warehouse_main)

            except NoDigit as err:
                print(err)


        elif ask == 3:
            obj = Xerox(
                input('Введите id: '),
                input('Введите модель: '),
                input('Введите год: '),
                input('Введите страну производства: '),
                bool(input('Введите True (0) если лазерный: ')),
                bool(input('Введите True (0) если цветной: '))
            )
            try:

                ask_quant = input('Введите количество шт.: ')
                if ask_quant.isdigit() == False:
                    raise NoDigit('\n!!! Вы ввели текстовое значение !!!\n')
                else:
                    ask_quant = int(ask_quant)
                    print(obj.xerox_obj)
                    Warehouse.warehouse_main.append(
                        {"id": obj.xerox_obj[0], "param": obj.xerox_obj[1:], "quant": ask_quant})
                    print(Warehouse.warehouse_main)

            except NoDigit as err:
                print(err)


    @staticmethod
    #ПЕРЕМЕЩЕНИЕ ТОВАРА
    def moving():
        print('\nПЕРЕМЕЩЕНИЕ ПРОИЗВОДИТСЯ ЦЕЛЫМИ ЯЧЕЙКАМИ СКЛАДА\n')
        try:
            wh_out = input(f'Введите склад отгрузки'
                           f'\n1 - главный'
                           f'\n2 - NORD'
                           f'\n3 - брак'
                           f'\nВВОД: ')
            wh_out_sku = int(input(f'\nВведите номер SKU в аналитике склада:  ')) - 1
            wh_in = input(f'\nВведите склад приемки'
                          f'\n1 - главный'
                          f'\n2 - NORD'
                          f'\n3 - брак'
                          f'\nВВОД: ')

            Warehouse.whses.get(wh_in).append(Warehouse.whses.get(wh_out)[wh_out_sku])
            Warehouse.whses.get(wh_out).pop(wh_out_sku)
            print('отправитель', Warehouse.whses.get(wh_out))
            print('получатель', Warehouse.whses.get(wh_in))
            print('\nНовая аналитика по складам теперь такая')
            Warehouse.show_analytics()
        except (IndexError, AttributeError):
            print('\n!!! Товар под таким номером отсутсвует, либо вы выбрали неправильный номер склада !!! \n')

    @staticmethod
    #АНАЛИТИКА ПО СКЛАДАМ
    def show_analytics():
        print('Наличие на главном складе')
        for i, el in enumerate(Warehouse.warehouse_main, 1):
            print(f'{i}. SKU {el}')
        print('Наличие на складе NORD')
        for i, el in enumerate(Warehouse.warehouse_nord, 1):
            print(f'{i}. SKU {el}')
        print('Наличие на складе брака')
        for i, el in enumerate(Warehouse.warehouse_damaged, 1):
            print(f'{i}. SKU {el}')


while True:
    print('\nВЫБОР ОПЕРАЦИИ И ВВОД ДАННЫХ')
    dv()
    choose_operation = int(input('\nВведите: \n1 - для прихода на ГЛАВНЫЙ склад \n2 - для перемещения между любыми складами  \n3 - вывод аналитики по всем складам \n0 - выход\nВВОД: '))

    if choose_operation == 0:
        break

    elif choose_operation == 1:
        Warehouse.eq_income()

    elif choose_operation == 2:
        Warehouse.moving()

    elif choose_operation == 3:
        Warehouse.show_analytics()

    else:
        print('Не корректный ввод номера операции')
