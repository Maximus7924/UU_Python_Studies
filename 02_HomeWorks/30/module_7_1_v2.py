class Product:
    '''Характеристики продуктов'''
    
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category
    
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category},\n'


class Shop:
    '''Магазин'''
   
    __file_name = 'product_list.txt'
    
    def __init__(self):
        self.__file_name = Shop.__file_name
        self.add_list = [] # список в который попадают добавляемые объекты трансформированные в виде строк, должен обнуляться как-то иначе будет швах.
        self.wrt_list = [] # список с продуктами которые должны быть записаны в файл после проверки наличия\отсутсвия их в файле.
        self.fil_list = [] # список продуктов уже содержащихся в файле.
        self.srt_list = [] # список сортировки, путём способа множеств выдаст уникальный список на запись.
        self.make_file()

    
    def add_products(self, *products):
        self.products = products
        # тип у "продуктов" это кортеж в котором ссылки на объекты и если посмотреть их тип то это будут экземпляры класса.
        for product in products:
            self.add_list.append(product.__str__())
            # здесь добавляется сформированная строка методом класса Продукт к пустому списку который создаётся при создании Магазина.
        self.read_file() # после прочтения файла список "self.fil_list" будет заполняться если будет чем поэтому не забываем об очистках.
        
        # проверка корректности данных
        
        # print('лист для добавки ', self.add_list)
        # print('лист из файла ', self.fil_list)
        
        # этот блок будет срабатывать только один раз при первом добавлении продуктов в базу.
        
        if len(self.fil_list) < 1:
            self.wrt_list = self.add_list
            # print('список на запись в файл при первом вызове программы ', type(self.wrt_list), len(self.wrt_list), self.wrt_list)
            self.write_file()
            self.add_list.clear()
            self.wrt_list.clear()
            self.get_products()
        else:
        # конец блока первичной обновки базы продуктов в файле.
            for a in range(len(self.add_list)):
                if self.add_list[a] in self.fil_list:
                    print(f'Продукт {self.add_list[a]} уже имеется с базе.')
                    # self.add_list.pop(a)
                    # удаляем элемент списка из списка чтобы не спамить множественный швах.
                else:
                    self.srt_list.append(self.add_list[a])
                    print(f'Продукт {self.add_list[a]} успешно будет добавлен в базу.')
        
        # for a in range(len(self.add_list)):
        #     for f in range(len(self.fil_list)):
        #         if self.add_list[a] != self.fil_list[f]: # если элемент списка на добавку не равен элементу списка из файла.
        #             self.srt_list.append(self.add_list[a])  # если элемент списка на добавку не встретился в списке из файла то он уходить в список сортировки.
        #             print(f'Продукт {self.add_list[a]} успешно добавлен в список ожидания.')
        #         else:
        #             print(f'Продукт {self.add_list[a]} уже имеется с базе.')  # выводим инфу об обломе.
        #             self.add_list.pop(a)
        # удаляем элемент списка ( .рор(а)) из списка чтобы не спамить множественный швах.... именно это сцуко в швах и привело !
        # в похожем блоке коде выше подобный метод уменшал длинну списка а переменная о состоянии (длинне списка) в цикле не изменялась
        # что привело к ошибке выхода за границы ....
        # два дня мозголомства ушли как страшный сон , да прибудет дебаг извечный с нами.
            
            self.add_list.clear()
            self.fil_list.clear()
            # print('список сортировки ', type(self.srt_list), len(self.srt_list), self.srt_list)
            self.wrt_list = list(set(self.srt_list))
        # print('это список для записи в файл ', self.wrt_list)
        self.write_file()
    
    
    def get_products(self):
        self.read_file() # вызывается функция чтения из файла и наполнения списка что в файле есть.
        print(self.fil_list)
        self.fil_list.clear() # очищает список продуктов содержащихся в файле после их показа\вывода, для безопасности.
    
    
    def make_file(self):
        self.__file_name = Shop.__file_name
        file = open(self.__file_name, 'a+', encoding='utf-8')
        file.close()
        
        
    def read_file(self):
        file = open(self.__file_name, 'r', encoding='utf-8')
        self.fil_list = file.readlines()  # потом список очистится но инфа в файле затронута не будет.
        file.close()
        
        
    def write_file(self):
        file = open(self.__file_name, 'a+', encoding='utf-8')
        file.writelines(self.wrt_list)  # потом список очистится но инфа в файле затронута не будет.
        file.close()
        self.fil_list.clear() # очистка списка элементов для безопасности\корректности работы.
    
    
    # def db_products(self):
    #   '''это заготовка''' ... не берусь реализовывать т.к. неделю убил на одно задание...
    #     pass

# Проверочный код для созданной программы.
    
s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add_products(p1, p2, p3)

p4 = Product('Apple', 45.9, 'Fruits')

print(p2.__str__())

s1.add_products(p2, p4)

s1.get_products()
