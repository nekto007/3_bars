# Ближайшие бары

После запуска, программа у вас запросит указать путь к файлу с данными
и координаты вашего местонахождения которые Вы можете узнать открыв в бразуере любую карту.
После ввода всех запрашиваемых данных программа выведет на экаран информацию о самом ближайшем баре, самом
о самом большом, самом маленьком и самом ближайшем баре.

# Как запустить

1. Скрипт требует для своей работы установленного интерпретатора Python
версии 3.5 и выше.
2. Файл со списком баров необходимо скачть по ссылке https://devman.org/fshare/1503831681/4/.

Запуск на Linux:

```bash

$ python bars.py bars.json(имя файла со списком баров в формате json)
Введите долготу: 
Введите широту: 
Для примера:
bars.json
37.585498984808645
55.751993247713255

Самый большой бар: Спорт бар «Красная машина»
Самый маленький бар: БАР. СОКИ
Самый ближайший бар: Brash and Blow. Находиться по адресу: улица Новый Арбат, дом 21
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
