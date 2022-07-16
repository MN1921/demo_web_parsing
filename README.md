Демонстрация сбора данных с сайта 
[Хабр Карьера](https://career.habr.com/vacancies?type=all)

Использовались библиотеки:
- `requests` - для формирования http запросов
- `lxml` - для разбора html

Указывался заголовок `User-Agent` - `Mozilla/5.0 ...` из [файла](./user_agent.txt)

Пример запуска:
```
python career_habr_com.py
```

Пример вывода данных:
```
Bell Integrator - DevOps инженер
РТЛабс - Руководитель проекта
...
```