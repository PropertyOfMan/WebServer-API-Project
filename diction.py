dictionary = {1: ('В золотом окне востока лик свой солнце показало.', 'Ромео и Джульетта'), 2: ('— Через столько лет? — Всегда.', 'Северус Снегг (Северус Снейп)'), 3: ('Ни одного правителя не поддерживают все до единого.', 'Игра престолов'), 4: ('Он коснулся пальцами ее волос, она ощутила, что к ней прикоснулась любовь.', 'Сцены из жизни за стеной'), 5: ('Воины-победители сперва побеждают и только потом вступают в битву; те же, что терпят поражение, сперва вступают в битву и только затем пытаются победить.', 'Сунь-Цзы')}
while 1:
    n = input()
    if n != '0':
        input()
        author = input()
        dictionary[len(dictionary) + 1] = n, author
        print('OK')
    else:
        break

print(dictionary)