# Проектная работа по курсу

https://docs.google.com/spreadsheets/d/1jejmm8k93H6XRbHhLN9sY5vOB9vW2cjdRi1x5_y11j4/edit?usp=sharing

## Описание
Проектная работа представляет собой спроектированный и реализованный ETL пайплайн с использованием
следующих инструментов:
- DIT (nifi, stream sets или механизм CDC)
- Stage-хранилище сырых данных
- Оркестратор airflow, управляющий потоками данных в Data Lake
- Движок вычислений Apache Spark / Hadoop MapReduce
- Аналитические витрины для предоставления аналитики пользователю (Clickhouse)

Результатом работы являются:
- Репозиторий с кодом решения (компонентов системы)
- Архитектурные диаграммы

## Примеры тем проектов


## Тема проекта

Аналитическая система для хранения, анализа и предсказания возникновения критичных событий на основе данных системы мониторинга Zabbix

## Существующий набор данных
1. Данные за несколько месяцев по возникающим событиям (порядка 1000 событий в месяц) с различной степенью критичности (Предупреждение, Средняя, Высокая, Чрезвычайная).
Каждое событие содержит:
    - дата возникновения
    - дата устранения
    - длительность
    - объект на котором произошло событие, тип объекта, модель объекта
    - Отделение, Адрес (здание, кабинет)
    - Системы к которым относится объект (множественное значение в виде json)
2. Список всех объектов подключенных к мониторингу (около 1000 объектов)
3. Список всех реакций персонала по каждому событию:
    - событие к которому относится комментарий
    - пользователь, дата и время комментария
    - тип комментария:
        - подавление - (должно быть для событий высокой критичности длительностью более 20 минут, означает реакцию дежурной службы на событие) 
        - подтверждение - для всех событий - означает дату ознакомления Специалиста с проблемой и принятия ее в работу (должно быть не позднее одного рабочего дня)
        - комментарий - пояснения по ходу решения проблемы


## Возможные варианты анализа
- Предсказание возникновения события на объекте более высокого уровня критичности, на основе предшествующих событий на данном объекте (на базе ML)
- Расчет надежности моделей применяемого оборудования (отношение числа событий вида "отказ оборудования" к общему числу эксплуатируемых объектов данной модели)
- Выявление повторяющихся событий (как на каждом объекте, так и в целом)
- Выявление нарушений регламента (отсутствие по событию в назначенный период времени подавления и/или подтверждения)
- Фильтрация ложных сработок (правда не совсем понятно как их отсеивать, в принципе это кратковременные (менее 5-10 минут), которые самовосстановились, или возможно они были обусловленны другими событиями)
 
