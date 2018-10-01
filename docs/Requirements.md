#1 ВВЕДЕНИЕ

##1.1 Цели

Данный документ содержит функциональные и нефункциональные требования для мобильного приложения "ExRates" для системы Android. Документ предназначен для ознакомления со структурой продукта.
##1.2 Бизнес требования 

###1.2.1 Исходные данные

В век информационных технологий и постоянного движения мировой экономики людям важно знать, какая валюта наиболее стабильна и какой ресурс наиболее ценен на рынке. Курс валют влияет на уровень доходов в стране и цены на импортные товары и услуги, следовательно, знание состояния финансового рынка позволяет вынести максимальную выгоду для человека.

###1.2.2 Бизнес возможности

Динамика современного мира не всегда позволяет отследить состояние финансового рынка, и многим людям хотелось бы иметь необходимую информацию о курсе валют и ценных ресурсах у себя под рукой. Данное приложение позволит быстро получить актуальную информацию и конвертировать валюты по текущему курсу. Спроектированный интерфейс пользователя позволяет использовать приложение людям с минимальными техническими знаниями.

##1.3 Аналоги

Основное отличие от аналогов - упрощенный интерфейс и оффлайн-доступ к последним обновлениям курса.
+**Финансы TUT.BY -курсы валют, конвертер банки** by TUT.BY

![](https://lh3.googleusercontent.com/MlxRymVwDGg2D3ZwXP5WKrBgAyJW-UYI5yKAaml-8d6zrxoblSeIHL96N09EPGDX-jA=s180)

Данное приложение позволяет получить актуальную информацию по курсу валют, их динамику и подробную информацию по отделениям банков и обменным пунктам.

+**Курсы валют Беларуси** by Yurchuk Viktor

![](https://lh3.googleusercontent.com/5Q6omcxFV-mJ0UvmneNfgTtv-BRxHBLlB5O4uSWqvLoHTVbMJSJ2HP4hqaxGlHrU3XMr=s90)

Курсы валют Беларуси предоставляет курсы различных валют по отношению к белорусскому рублю, удобный конвертер валют по актуальному курсу и стоимость ценных ресурсов на рынке. 

#2 ТРЕБОВАНИЯ ПОЛЬЗОВАТЕЛЯ


##2.1 Программные интерфейсы

Для получения актуальных данных, продукт должен взаимодействовать с наиболее проверенными источниками информации о ценных валютах: Национальный банк Республики Беларусь и ОАО "Сберегательный банк Беларусбанк", предоставляющие простой API для получения необходимой информации.

##2.2 Интерфейс пользователя

![](https://github.com/Shalynishka/ExRates/blob/master/docs/mockups/start.png)

Изображение 1 - стартовое окно

![](https://github.com/Shalynishka/ExRates/blob/master/docs/mockups/menu.png)

Изображение 2 - меню

![](https://github.com/Shalynishka/ExRates/blob/master/docs/mockups/all%20currency.png)

Изображение 3 - меню "Все валюты"

##2.3 Характеристики пользователей

1. Банковские служащие - 
2. Финансовые работники -
3. Пользователи с деньгой -
4. Пользователи без деньги - 

##2.4 Предположения и зависимости

Основным фактором предоставления актуальной информации является доступ в Интернет.


#3 СИСТЕМНЫЕ ТРЕБОВАНИЯ

##3.1 Функциональные требования

1. Получение информации о курсе наиболее распространенных валют
2. Получение информации о курсе заданной валюты
3. Конвертер валют
4. Получение стоимости основных ценных ресурсов

##3.2 Нефункциональные требования

###3.2.1 АТРИБУТЫ КАЧЕСТВА

Продукт должен:
1. предоставлять актуальную и точную информацию.
2. быть надежным.
3. предоставлять удобный и понятный интерфейс