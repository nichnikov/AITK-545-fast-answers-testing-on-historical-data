# AITK-545-fast-answers-testing-on-historical-data
Тест исторической БД быстрых ответов

https://jira.action-media.ru/browse/AITK-545

Для теста используем таблицы 

fast_answers4.auto_answer_12_118
fast_answers4.auto_answer_16_86

https://conf.action-media.ru/pages/viewpage.action?pageId=442564896

Таблицы актуализируются один раз в сутки, дата последнего обновления в столбце timestamp

Нам нужно забрать из таблицы

Запрос (эталон)

Текст быстрого ответа

Алиасы (по таблице соответсвия добавим им паб айди)

Модуль документа и айди документа для формирования ссылки

is_synonym - синоним или нет

Проверку делаем в два шага

Сначала берем все данные из БД с учетом синонимов и находим ответы с ними

Затем берем данные без синонимов, только эталоны со значением false и ищем ответы с ними

Цель - понять, какой прирост дают синонимы, стоит ли их использовать в дальнейшем

Проверяем на выборке вопросов за неделю для систем в КПИ

Данные по ссылке - https://docs.google.com/spreadsheets/d/181SjsCOfiAewTRNthSIfy7VtQBGYm1iaUmxz540V90w/edit?usp=sharing 

https://docs.google.com/spreadsheets/d/1CDwQMWDm1gPhZIMBusrtO8Bv2kdNzmHQFywJ5EabwjA/edit?gid=0#gid=0


В выборке только вопросы, на которые мы щас не даем ответ, чтобы посмотреть прирост к существующим процентам. Стоит фильтр, робот ответил - 0. Фильтр не снимать

Паб айди

В таблице нет паб айди, но есть алиасы изданий. Для каждого алиаса в таблице соответствия есть свой паб айди (№ издания)

https://docs.google.com/spreadsheets/d/19pTgU58Q69-AWLjHsD2xHc5fUYQEg9KnHSQJ2stuWZQ/edit?gid=0#gid=0

Алиас издания - столбец С