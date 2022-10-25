def tableprint(dicts): # Вывод ТАБЛИЦЫ в консоль
    print("{:<3} {:<30} {:<6} {:<12} {:<15} {:<10}".format('Num','Task','Time','Date','Status','Result'))
    for dict in dicts:
        num, task, time, date, status, result = dict.values()
        print("{:<3} {:<30} {:<6} {:<12} {:<15} {:<10}".format(num, task, time, date, status, result))

def notebooks_data():
    with open('DATA.csv', encoding='utf-8') as data:
        schedule_lst = list(map(lambda x: list(x.strip('\n').split(',')), data.readlines()))

#Наполняем НОВЫЙ список 'schedule' СЛОВАРЯМИ, со значениями из каждой строки
    schedule = []
    keys = ["Num","Name", "Path"]
    for String in schedule_lst:
        Dictionary = {}
        for index in range(len(keys)):
            Dictionary[keys[index]] = String[index]
        schedule.append(Dictionary)
    return schedule

def schedule_data(): # Запись данных с ФАЙЛА 'notebook1.csv'

    # Считываем файл и сохраняем в СПИСОК
    with open('notebook1.csv', encoding='utf-8') as data:
        schedule_lst = list(map(lambda x: list(x.strip('\n').split(',')),data.readlines()))

#Наполняем НОВЫЙ список 'schedule' СЛОВАРЯМИ, со значениями из каждой строки
    schedule = []
    keys = ["Num","Task","Time","Date","Status","Result"]
    for String in schedule_lst:
        Dictionary = {}
        for index in range(len(keys)):
            Dictionary[keys[index]] = String[index]
        schedule.append(Dictionary)
    return schedule


def schedule_remove(schedule, index):
    schedule.pop(int(index))
    #renumbering
    for i in range(1, len(schedule)):
        schedule[i]["Num"] = str(i)
    #-----------
    return schedule


def schedule_edit(schedule, index):
    change = list(input("Введите столбец, новый параметр:\n").split(', '))
    schedule[int(index)][change[0]] = change[1]
    if change[0] == "Num":
        schedule.insert(int(change[1]), schedule[int(index)])
        schedule.pop(int(index)+1)
        #renumbering
        for i in range(1, len(schedule)):
            schedule[i]["Num"] = str(i)
    #-----------
    return schedule


def schedule_add(schedule): # Добавление заметки
    notice = input('Введите новую заметку:\n')
    note = list(notice.split(', '))
    note[3]=str('(' + note[3] + ')')
    position = input('Введите номер новой заметки:\n')
    note.insert(0, position)
    #List to Dict
    keys = ["Num","Task","Time","Date","Status","Result"]
    notice = {}
    for i in range(len(keys)):
        notice[keys[i]] = note[i]
    schedule.insert(int(position), notice)
    #renumbering
    for i in range(1, len(schedule)):
        schedule[i]["Num"] = str(i)
    #----------
    return schedule

def schedule_write(schedule):
    with open('notebook1.csv', 'w', encoding='utf-8') as String:
        for k in schedule:
            lst=[]
            for i in k:
                lst.append(k[i])
            String.write(','.join(lst)  + '\n')

# Блок работы приложения
while True:
    schedule = schedule_data()
    tableprint(schedule)
    path = list(input("Введите действие:\n").split(' '))
    if path[0] == "Закрыть": break
    elif path[0] == "Удалить":
        schedule = schedule_remove(schedule, path[1])
    elif path[0] == "Изменить":
        schedule = schedule_edit(schedule, path[1])
    elif path[0] == "Добавить":
        schedule = schedule_add(schedule)
    elif path[0] == "Очистить":
        schedule = [{
        "Num" : "|",
        "Task" : "|",
        "Time" : "|",
        "Date" : "|",
        "Status" : "|",
        "Result" : "|"
        }]
    else:
        print("Введено несуществующее действие, попробуйте снова")
        continue
    schedule_write(schedule)