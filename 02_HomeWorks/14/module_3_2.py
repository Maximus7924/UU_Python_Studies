
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    defaul_sender = 'university.help@gmail.com'
    err1_string = f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>."
    err2_string = "Нельзя отправить письмо сомому себе!"
    inf1_string = f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>."
    inf2_string = f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>."
# 1. проверка корректности почтового адреса
    if recipient.find('@') == -1:
        print(err1_string)
        return
    if sender.find('@') == -1:
        print(err1_string)
        return
    if recipient.find('.com') == -1 and recipient.find('.net') == -1 and recipient.find('.ru') == -1:
        print(err1_string)
        return
    if sender.find('.com') == -1 and sender.find('.net') == -1 and sender.find('.ru') == -1:
        print(err1_string)
        return
# 2. проверка отправки самому себе
    if recipient == sender:
        print(err2_string)
        return
# 3. успешно если дефолтный отправитель
    if sender == defaul_sender:
        print(inf1_string)
        return
# 4. нестандартный отправитель
    if sender != defaul_sender:
        print(inf2_string)
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
