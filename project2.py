# Ресторан решил оптимизировать работу сотрудников и на входе поставить электронного робота, который посредством
# опроса будет определять, что хочет посетитель(поесть, зарезервировать столик или узнать информацию),
# а так же принимать заказы и (при надобности) консультировать посетителя при выборе блюд.
print('Как вас можно называть?')
name = input()
print('Здравсвуйте,', name, '!', 'Мы рады видеть вас в ресторане "MoonLight".')
print('Хотели бы вы присесть за столик?')                                         # Purpose of the visitor's visit
enter = input()
if (enter == 'Да') or (enter == 'ДА') or (enter == 'да'):
    print('Прошу за мной, я покажу Вам Ваш столик. Пожалуста ознакомьтесь с меню... Готовы ли вы сделать заказ?')
    menu = input()
    if (menu == 'Да') or (menu == 'ДА') or (menu == 'да'):
        print('Я готов записать...')
        order = input()                                                           # Take orders
        print('Ваш заказ:', order)
        print('Спасибо за Ваш заказ, блюда готовятся в течении 10-30 минут, приятного Вам вечера!')
    else:
        print('Вам помочь с выбором блюд?')                                       # Helps with food selection
        help_order = input()
        if (help_order == 'Да') or (help_order == 'ДА') or (help_order == 'да'):
            print('Могу посоветовать Вам блюда от Шеф-повара нашего ресторана:\n'
                  'Мясо нежного ягненка средней прожарки \nПаста с грибами под сливочным соусом\nЛосось под фирменым '
                  'соусом "MoonLight"')
            print('Надеюсь я помог вам определиться. Готов записать Ваш заказ.')
            order = input()                                                       # Take orders
            print('Ваш заказ:', order)
            print('Блюда будут готовы в течение 10-30 минут. Приятного Вам вечера.')
        else:
            print('Буду ожидать, когда вы готовы будете заказать.')
            print('Готов записать Ваш заказ.')
            order = input()                                                       # Take orders
            print('Ваш заказ:', order)
            print('Ваш заказ будет готов в течение 10-30 минут, приятного вечера!')
else:
    print('Хотели бы вы зарезервировать столик?')                                 # Purpose of the visitor's visit
    answer = input()
    if (answer == 'Да') or (answer == 'ДА') or (answer == 'да'):
        print('На какой день недели вы бы хотели зарезервировать столик?')
        day = input()
        if (day == 'Среда') or (day == 'среда') or (day == 'СРЕДА'):              # Changing the case of a word
            day = 'среду'
        elif (day == 'ПЯТНИЦА') or (day == 'Пятница') or (day == 'пятница'):
            day = 'пятницу'
        elif (day == 'Суббота') or (day == 'СУББОТА') or (day == 'суббота'):
            day = 'субботу'
        print('На какое бы время вы бы хотели зарезервировать столик?')           # Booking time
        time = input()
        print('На сколько персон вы бы хотели забронировать столик?')             # Number of people
        people = int(input())
        if people == 1:                                                           # The change in the number of words
            persons = 'человека.'
        else:
            persons = 'человек.'
        print('Хотели бы вы заранее заказать блюда?')
        help_order = input()
        if (help_order == 'Да') or (help_order == 'ДА') or (help_order == 'да'):
            print('Я готов записать Ваш заказ.')
            order = input()                                                       # Take orders
            print('Будем ждать Вас в', day, 'в', time, 'в колличестве', people, persons,
                  'Для Вас будут приготовлены:', order)
        else:
            print('Будем ждать Вас в', day, 'в', time, 'в количестве', people, persons)
    else:                                                                         # Give information
        print('К сожалению, ничем не могу Вам помочь. По другим вопросам вы можете обратиться к администратору, '
              'позвонив на номер 89223425234. Спасибо за визит.')
