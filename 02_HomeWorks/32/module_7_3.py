class WordsFinder:
    """
    Объект этого класса должен принимать при создании неограниченного количество названий файлов
    и записывать их в атрибут file_names в виде списка или кортежа.
    """
    def __init__(self, *args):
        self.file_names = args
    
    
    def get_all_words(self):
        """
        подготовительный метод, который возвращает словарь следующего вида:
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
            Где:
                'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
                ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
        """
        all_words = {}
        
        for f in self.file_names:
            with open(f, 'r', encoding='utf-8') as file:
                file_name = file.name
                content = file.read().splitlines() # получаем содержимое, убираем переход строки, заносим в список строку
                word_list = []
                for c in content: # для каждой строки в списке
                    words = c.split() # пробуем добыть пословно из строки
                    for w in words:
                        word = w.strip(',.=!?;:-')
                        word_list.append(word.lower())
                all_words.update({file_name: word_list})
        return all_words
        
        
    def count(self, word):
        """
        использует метод get_all_words для получения названия файла и списка его слов.
        """
        word_count = word.lower()
        
        for name, words in self.get_all_words().items():
            counter = words.count(word_count)
            print({name:counter})
    
    
    def find(self, word):
        """
        использует метод get_all_words для получения названия файла и списка его слов.
        """
        word_find = word.lower()
        
        for name, words in self.get_all_words().items():
            position = words.index(word_find) + 1
            print({name:position})


# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt', 'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))