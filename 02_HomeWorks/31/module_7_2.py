
def custom_write(file_name, strings: list):
    """Функция которая принимает аргументы:
        file_name - название файла для записи,
        strings - список строк для записи."""
    
    file_name = 'text.txt'
    
    line_number = []
    byte_number = []
    text_string = strings
    string_position = {}
    
    file = open(file_name, 'w+', encoding='utf-8')
    
    for l in range (len(text_string)):
        byte_number.append(file.tell())
        line_number.append(l)
        file.write(text_string[l] + '\n')
        string_position.update({(line_number[l] + 1, byte_number[l]):text_string[l]})
        
    file.close()
    
    return string_position

# код для проверки работы

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

    
    
    
