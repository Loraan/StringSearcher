# Утилита по поиску подстроки в строке
###### Версия 1.0
###### Авторы: Головачёв Георгий Алексеевич, Щербакова Полина Денисовна
###### Группа: ФТ-203
___

### Описание
Программа для сравнения алгроритмов поиска подстроки в тексте по времени и памяти
___

### Состав
    -исполняемый файл: searcher.py
    -алгоритмы поиска: algorithms.py
    -файл с текстом: text.txt
    -логи для вывода занимаемой памяти: logs.txt
    -тесты: в папаке test:
        -тестирование алгоритмов
    -отрисовка графиков: папка graphs:
        -стилизация графиков: graph_painter.py
        -заполнение массива данных для отрисовки графиков: graph_maker.py
        -вывод и сохранение графиков: graph_saver.py
---

### Консольная версия 
    -Справка по командам: searcher.py {-h|--help}
    -Запуск приложения: searcher.py [-t] [-m] [-s STRING] [-mg] [-tg] SUBSTRING
    P.s. если образ или шаблон состоит из нескольких слов отделённых пробелом, то следует заключать в " "
___

### Флаги
    -h - help по программе
    -t - включает режим замера и вывода времени отработки каждого алгоритма
    -m - включает режим земера и вывода в logs.txt сводки об используемой памяти каждого алгорима
    -s - включает ввод текста с консоли
    -mg - выводит график по памяти
    -tg - выводит график по времени

### Пример ипользования:
`searcher.py -t -m me`

`Name: Brute Force, Position: 556, Time: 0 ms
Name: Knuth Morris Pratt, Position: 556, Time: 63 ms
Name: Rabin Karp, Position: 556, Time: 0 ms
Name: Boyer Moore, Position: 556, Time: 0 ms
Name: Boyer Moore Horspul, Position: 556, Time: 0 ms
`