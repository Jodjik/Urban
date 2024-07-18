def svs(simvol, stroka): #simvol_v_stroke
    j = True
    for i in stroka:
        if i == simvol:
            j = True
            break
        else:
            j = False
    return j

def send_emails(message, recipient, sender = "university.help@gmail.com"):
    if not svs('@', sender) or not svs('@', recipient): #Не получилось записать проверки 12 и 14 строки в одну, были разделены с одинаковыми сообщениями
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not sender.endswith((".ru", ".com", ".net")) or not recipient.endswith((".ru", ".com", ".net")):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

#message = input('Введите сообщение: ')  #Тут я проверял себя вводя разные значения переменных через консоль
#recipient = input('Ваш Email@.com: ')
#sender = input('Введите адрес отправителя (university.help@gmail.com по умолчанию): ')
#if sender == '':
#    sender = 'university.help@gmail.com'

send_emails('Здраствуйте Преподователи Urban', 'jodjikmail.ru', sender='urban.superpuper.teacher@mail.ru')

send_emails('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_emails('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_emails('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_emails('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
