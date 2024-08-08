calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    string_tuple = []
    string_length = len(string)
    string_tuple.append(string_length)
    string_tuple.append(string.upper())
    string_tuple.append(string.lower())
    string_tuple = tuple(string_tuple)
    count_calls()
    return string_tuple

def is_contains(string, list_to_search):
    compare = False
    string = string.lower()
    list = []
    for j in list_to_search:
        j = str(j.lower())
        list.append(j)
    if string in list:
        compare = True
    count_calls()
    return string, list_to_search, compare


print(string_info('AbraK'))
print(string_info('AbraKadabra'))
print(is_contains('Maxim', ['family', 'Maximus', 'FRIEND']))
print(is_contains('family', ['FAmilY', 'Maximus', 'FRIEND']))
print(is_contains('friend', ['fAMiLy', 'Maximus', 'friend']))
print(string_info('UrbanUnivercity'))
print(calls)

