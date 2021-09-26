def start():
    while True:
        print('Укажите размер поля в виде: 10x10; 100x10; 5X3;'
              ' 3x2. Минимальный количество клеток на игровом поле - 2 клетки.')
        a = str(input()).split('x')
        if len(a) != 2:
            print('Ошибка во входных данных. Некорректно введены входные данные.'
                  'Введите по новой входные данные по типу: 100x10; '
                  '5X3; 3x2. Без пробела в начале. И значения сторон поля должны '
                  'являться положительным числом.')
        elif a[1].isdigit() and a[0].isdigit():
            b = [int(i) for i in a]
            if b[0] * b[1] < 2:
                print('Ошибка во входных данных. Слишком маленькое значение поля.'
                      'Введите по новой входные данные по типу: 100x10; '
                      '5X3; 3x2. Без пробела в начале. И значения сторон '
                      'поля должны являться положительным числом.')
            else:
                mtr_o_cl_fl = [['#' for _ in range(b[0])] for _ in range(b[1])]
                mtr_res = [[0 for _ in range(b[0])] for _ in range(b[1])]
                break
        else:
            print('Ошибка во входных данных. Некорректно введены входные данные.'
                  'Введите по новой входные данные по типу: 100x10;'
                  '5X3, 3x2. Без пробела в начале. И значения сторон поля должны являться положительным числом.')
    while True:
        print('Введите количество бомб. Не меньше 1 и не больше чем -> размер поля - 1')
        a = str(input())
        if a.isdigit():
            if 1 <= int(a) <= b[0] * b[1] - 1:
                am_bombs = int(a)
                break
            else:
                print('Некорректное количество бомб бомб')
        else:
            print('Ошибка во входных данных')
    return b, mtr_res, mtr_o_cl_fl, am_bombs


def flag(x_g, y_v, mtr_o_cl_fl):
    if mtr_o_cl_fl[y_v - 1][x_g - 1] == '#':
        mtr_o_cl_fl[y_v - 1][x_g - 1] = 'F'
        return
    elif mtr_o_cl_fl[y_v - 1][x_g - 1] == 'F':
        mtr_o_cl_fl[y_v - 1][x_g - 1] = '#'
        return
    else:
        return


def open_field(x_st, y_st, mtr_res, mtr_o_cl_fl, amount_bombs):
    if mtr_o_cl_fl[y_st][x_st] != 'F':
        if mtr_res[y_st][x_st] == 0:
            mtr_o_cl_fl[y_st][x_st] = 0
            queue = [[x_st, y_st]]
            while queue:
                x, y = queue.pop(0)

                if y - 1 >= 0:
                    if x - 1 >= 0:
                        if (mtr_o_cl_fl[y - 1][x - 1] == '#' or mtr_o_cl_fl[y - 1][x - 1] == 'F') and mtr_res[y_st][x_st] != 'b':
                            mtr_o_cl_fl[y - 1][x - 1] = mtr_res[y - 1][x - 1]
                            if mtr_res[y - 1][x - 1] == 0:
                                queue.append([x - 1, y - 1])

                    if x + 1 <= cords[0] - 1:
                        if (mtr_o_cl_fl[y - 1][x + 1] == '#' or mtr_o_cl_fl[y - 1][x + 1] == 'F') and mtr_res[y_st][x_st] != 'b':
                            mtr_o_cl_fl[y - 1][x + 1] = mtr_res[y - 1][x + 1]
                            if mtr_res[y - 1][x + 1] == 0:
                                queue.append([x + 1, y - 1])
                    if x == x:
                        if (mtr_o_cl_fl[y - 1][x] == '#' or mtr_o_cl_fl[y - 1][x] == 'F') and mtr_res[y_st][x_st] != 'b':
                            mtr_o_cl_fl[y - 1][x] = mtr_res[y - 1][x]
                            if mtr_res[y - 1][x] == 0:
                                queue.append([x, y - 1])

                if y + 1 <= cords[1] - 1:
                    if x - 1 >= 0:
                        if (mtr_o_cl_fl[y + 1][x - 1] == '#' or mtr_o_cl_fl[y + 1][x - 1] == 'F') and mtr_res[y_st][x_st] != 'b':
                            mtr_o_cl_fl[y + 1][x - 1] = mtr_res[y + 1][x - 1]
                            if mtr_res[y + 1][x - 1] == 0:
                                queue.append([x - 1, y + 1])

                    if x + 1 <= cords[0] - 1:
                        if (mtr_o_cl_fl[y + 1][x + 1] == '#' or mtr_o_cl_fl[y + 1][x + 1] == 'F') and mtr_res[y_st][x_st] != 'b':
                            mtr_o_cl_fl[y + 1][x + 1] = mtr_res[y + 1][x + 1]
                            if mtr_res[y + 1][x + 1] == 0:
                                queue.append([x + 1, y + 1])
                    if x == x:
                        if (mtr_o_cl_fl[y + 1][x] == '#' or mtr_o_cl_fl[y + 1][x] == 'F') and mtr_res[y_st][x_st] != 'b':
                            mtr_o_cl_fl[y + 1][x] = mtr_res[y + 1][x]
                            if mtr_res[y + 1][x] == 0:
                                queue.append([x, y + 1])

                if x + 1 <= cords[0] - 1:
                    if (mtr_o_cl_fl[y][x + 1] == '#' or mtr_o_cl_fl[y][x + 1] == 'F') and mtr_res[y_st][x_st] != 'b':
                        mtr_o_cl_fl[y][x + 1] = mtr_res[y][x + 1]
                        if mtr_res[y][x + 1] == 0:
                            queue.append([x + 1, y])

                if x - 1 >= 0:
                    if (mtr_o_cl_fl[y][x - 1] == '#' or mtr_o_cl_fl[y][x - 1] == 'F') and mtr_res[y_st][x_st] != 'b':
                        mtr_o_cl_fl[y][x - 1] = mtr_res[y][x - 1]
                        if mtr_res[y][x - 1] == 0:
                            queue.append([x - 1, y])
            if check_field_for_win(mtr_o_cl_fl, amount_bombs) == 'Win':
                return 'Win'
            return 'Ok'
        elif mtr_res[y_st][x_st] == 'b':
            mtr_o_cl_fl[y_st][x_st] = mtr_res[y_st][x_st]
            return 'Boom'
        elif 1 <= mtr_res[y_st][x_st] <= 8:
            mtr_o_cl_fl[y_st][x_st] = mtr_res[y_st][x_st]
            if check_field_for_win(mtr_o_cl_fl, amount_bombs) == 'Win':
                return 'Win'
            return 'Ok'
    else:
        return 'Ok '


def check_field_for_win(mtr_o_cl_fl, bombs):
    count = 0
    for i in mtr_o_cl_fl:
        for j in i:
            if j == '#' or j == 'F':
                count += 1
    if count == bombs:
        return 'Win'
    else:
        return 'No win'


def save_game(field_status, cords, mtr_res, mtr_o_cl_fl, amount_bombs):
    import pickle, os
    dict_res = {1: field_status, 2: cords, 3: mtr_res, 4: mtr_o_cl_fl, 5: amount_bombs}
    while True:
        print('Введите название сохранения')
        a = str(input())
        if os.path.exists(f'{a}.pickle'):
            print('Вы увекрены что хотите перезаписать сохранение?.')
            print('Y - да, N - нет.')
            while True:
                b = str(input())
                if b == 'Y':
                    with open(f'{a}.pickle', 'wb') as f:
                        pickle.dump(dict_res, f)
                    return
                elif b == 'N':
                    break
        else:
            with open(f'{a}.pickle', 'wb') as f:
                pickle.dump(dict_res, f)
                return


def open_game():
    import pickle, os

    print('Введите название сохранения без расширения файла')
    print('Если не хотите открывать файл с сохранением напшите в командной строчке "execute order 66"')
    while True:
        a = str(input())
        if os.path.exists(f'{a}.pickle'):
            with open(f'{a}.pickle', 'rb') as f:
                inf = pickle.load(f)
            return inf[1], inf[2], inf[3], inf[4], inf[5]
        elif a == 'execute order 66':
            return 0, 0, 0, 0, 0
        else:
            print('Файл не найден')


def action(field_status, cords, mtr_res, mtr_o_cl_fl, amount_bombs):
    import random
    from collections import defaultdict

    if field_status == 'create_new_field':
        print('Введите действие')
        a = str(input())

        if a == 'Save':
            save_game(field_status, cords, mtr_res, mtr_o_cl_fl, amount_bombs)
            return 'save'
        s = a.split(',')

        if len(s) == 3 and s[0].isdigit() and s[1].isdigit() and s[2] in ['Flag', 'Open']:
            if (1 <= int(s[0]) <= cords[0] and 1 <= int(s[1]) <= cords[1]) is False:
                print('Ошибка в ходных данных')
                return field_status
            if s[2] == 'Flag':
                flag(int(s[0]), int(s[1]), mtr_o_cl_fl)
                field_status = 'create_new_field'
            elif s[2] == 'Open':
                x_st, y_st = int(s[0]) - 1, int(s[1]) - 1
                if mtr_o_cl_fl[y_st][x_st] != 'F':
                    dict_bombs = defaultdict(list)
                    for _ in range(amount_bombs):
                        while True:
                            x = random.randint(0, cords[0] - 1)
                            y = random.randint(0, cords[1] - 1)
                            if (x == x_st and y == y_st) is False and (y not in dict_bombs[x]):
                                dict_bombs[x].append(y)

                                mtr_res[y][x] = 'b'

                                if y - 1 >= 0:
                                    if x - 1 >= 0:
                                        if mtr_res[y - 1][x - 1] != 'b':
                                            mtr_res[y - 1][x - 1] += 1
                                    if x + 1 <= cords[0] - 1:
                                        if mtr_res[y - 1][x + 1] != 'b':
                                            mtr_res[y - 1][x + 1] += 1
                                    if x == x:
                                        if mtr_res[y - 1][x] != 'b':
                                            mtr_res[y - 1][x] += 1

                                if y + 1 <= cords[1] - 1:
                                    if x - 1 >= 0:
                                        if mtr_res[y + 1][x - 1] != 'b':
                                            mtr_res[y + 1][x - 1] += 1
                                    if x + 1 <= cords[0] - 1:
                                        if mtr_res[y + 1][x + 1] != 'b':
                                            mtr_res[y + 1][x + 1] += 1
                                    if x == x:
                                        if mtr_res[y + 1][x] != 'b':
                                            mtr_res[y + 1][x] += 1

                                if x + 1 <= cords[0] - 1:
                                    if mtr_res[y][x + 1] != 'b':
                                        mtr_res[y][x + 1] += 1

                                if x - 1 >= 0:
                                    if mtr_res[y][x - 1] != 'b':
                                        mtr_res[y][x - 1] += 1
                                break
                    result = open_field(x_st, y_st, mtr_res, mtr_o_cl_fl, amount_bombs)
                    if result == 'Ok':
                        field_status = 'game'
                    elif result == 'Win':
                        field_status = 'win'
                    else:
                        field_status = 'game_over'
            return field_status
        else:
            print('Ошибка в входных данных')
            return field_status

    elif field_status == 'game':
        print('Введите действие')
        a = str(input())

        if a == 'Save':
            save_game(field_status, cords, mtr_res, mtr_o_cl_fl, amount_bombs)
            return 'save'

        s = a.split(',')
        if len(s) == 3 and s[0].isdigit() and s[1].isdigit() and s[2] in ['Flag', 'Open']:
            if (1 <= int(s[0]) <= cords[0] and 1 <= int(s[1]) <= cords[1]) is False:
                print('Ошибка в входных данных')
                return field_status
            if s[2] == 'Flag':
                flag(int(s[0]), int(s[1]), mtr_o_cl_fl)
            elif s[2] == 'Open':
                x_st, y_st = int(s[0]) - 1, int(s[1]) - 1
                result = open_field(x_st, y_st, mtr_res, mtr_o_cl_fl, amount_bombs)
                if result == 'Ok':
                    field_status = 'game'
                elif result == 'Win':
                    field_status = 'win'
                else:
                    field_status = 'game_over'
            return field_status
        else:
            print('Ошибка в входных данных')
            return field_status


while True:
    print()
    print('Хотите начать новую игру или продолжить играть в старую?')
    print('Введите 1 для начала новой игры или 2 для продолжения старой игры.')
    name = str(input())
    if name.isdigit():
        if int(name) == 1:
            cords, mtr_res, mtr_o_cl_fl, amount_bombs = start()
            field_status = 'create_new_field'
            while True:
                if field_status == 'game':
                    print()
                    for i in mtr_o_cl_fl:
                        print(' '.join([str(j) for j in i]))
                    print()
                if field_status == 'create_new_field':
                    print()
                    for i in mtr_o_cl_fl:
                        print(' '.join([str(j) for j in i]))
                    print()
                if field_status == 'game_over':
                    print()
                    for i in mtr_o_cl_fl:
                        print(' '.join([str(j) for j in i]))
                    print()
                    print('Вы проиграли.')
                    break
                elif field_status == 'save':
                    print()
                    for i in mtr_o_cl_fl:
                        print(' '.join([str(j) for j in i]))
                    print()
                    print('Игра сохранена.')
                    break
                elif field_status == 'win':
                    print()
                    for i in mtr_o_cl_fl:
                        print(' '.join([str(j) for j in i]))
                    print()
                    print('Вы выиграли.')
                    break
                field_status = action(field_status, cords, mtr_res, mtr_o_cl_fl, amount_bombs)
            if field_status != 'save':
                print('Хотите ли вы сохранить партию?')
                print('Y - да, N - нет.')
                while True:
                    a = str(input())
                    if a == 'Y':
                        save_game(field_status, cords, mtr_res, mtr_o_cl_fl, amount_bombs)
                        print('Игра сохранена.')
                        break
                    elif a == 'N':
                        print('Спасибо за сыгранную партию информация об этой партии стирается в неизвестном.')
                        break
                    else:
                        print('Так вы хотите сохранить')
                print('Хотите закончить играть?')
                print('Y - да, N - нет.')
                while True:
                    a = str(input())
                    if a == 'Y':
                        exit(0)
                    elif a == 'N':
                        break
        elif int(name) == 2:
            field_status, cords, mtr_res, mtr_o_cl_fl, amount_bombs = open_game()
            if field_status == cords == mtr_o_cl_fl == mtr_res == amount_bombs:
                print('Не удалось открыть сохранение')
            else:
                while True:
                    if field_status == 'game':
                        print()
                        for i in mtr_o_cl_fl:
                            print(' '.join([str(j) for j in i]))
                        print()
                    if field_status == 'create_new_field':
                        print()
                        for i in mtr_o_cl_fl:
                            print(' '.join([str(j) for j in i]))
                        print()
                    if field_status == 'game_over':
                        print()
                        for i in mtr_o_cl_fl:
                            print(' '.join([str(j) for j in i]))
                        print()
                        print('Вы проиграли.')
                        break
                    elif field_status == 'save':
                        print()
                        for i in mtr_o_cl_fl:
                            print(' '.join([str(j) for j in i]))
                        print()
                        print('Игра сохранена.')
                        break
                    elif field_status == 'win':
                        print()
                        for i in mtr_o_cl_fl:
                            print(' '.join([str(j) for j in i]))
                        print()
                        print('Вы выиграли.')
                        break
                    field_status = action(field_status, cords, mtr_res, mtr_o_cl_fl, amount_bombs)
                if field_status != 'save':
                    print('Хотите ли изменить информацию в этотм сохранение?')
                    print('Y - да, N - нет.')
                    while True:
                        a = str(input())
                        if a == 'Y':
                            print('Игра снова сохранена.')
                            break
                        elif a == 'N':
                            print('Спасибо за сыгранную партию информация об этой партии останется в этом файле.')
                            break
                        else:
                            print('Так вы хотите сохранить')
                    print('Хотите закончить играть?')
                    print('Y - да, N - нет.')
                    while True:
                        a = str(input())
                        if a == 'Y':
                            exit(0)
                        elif a == 'N':
                            break

    else:
        print('Ошибка во входных данных')