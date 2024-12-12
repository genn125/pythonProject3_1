
#module_3_2.py

# Задача "Рассылка писем" - Способы вызова функции


def send_email(message, recipient, sender="university.help@gmail.com"):

    if ("@" and (".com" or ".ru" or ".net")) not in recipient and ("@" and (".com" or ".ru" or ".net")) not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif sender==recipient:
        print("Нельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
        print(f"Письмо <{message}> успешно отправлено с адреса <{sender}> на адрес <{recipient}>.")

    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо <{message}> отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', "urban.info@gmail.com")

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', "university.help@gmail.com")
