
Переменные окружения
-
Часть настроек проекта берётся из переменных окружения. Переменные окружения это переменные, значения которых присваиваются программе Python извне. Чтобы их определить, создайте файл .env рядом с main.py и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.
Пример содержания файла .env:

```
BITLY_TOKEN=21ecde8d68b8de54395928e7e4199dd7e27f9e78
```

Получить токен BITLINK можно на сайте Bitly.

Цель проекта
-

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.


## Описание

Проект создан для сокращения или подсчета кликов по ссылке. Для получения сокращенной ссылки необходимо передать программе ссылку для сокращения. В ином случае, если вы хотите узнать сколько раз переходили по вашей сслыке, необходимо передать сокращенную ссылку.

## Установка

Скачайте необходимые файлы, затем используйте рір (или ріp3, если есть конфликт с Python2) для установки зависимостей и установить зависимости. Зависимости можно установить командой, представленной ниже.

Установите зависимости командой:

```
pip install -r requirements.txt
```

## Пример запуска скрипта

Для запуска скрипта у вас уже должен быть установлен Python3.

Для получения сокращенной ссылки, необходимо написать команду в таком формате:

```
python main.py --url https://translate.google.ru
```
После аргумента --url необходимо указать ссылку для работы кода, документацию можно найти на сайте Сократить ссылку Bitly.

Для получения количества кликов, необходимо написать команду в таком формате:
```
python main.py --url bit.ly/3uujaSR
```