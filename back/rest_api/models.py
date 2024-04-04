from django.db import models

# Выбор количества путешественников
NUMBER = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('10+', '10+'),
]

# Выбор континента
CONTINENT = [
    ('AS', 'Азия'),
    ('AF', 'Африка'),
    ('EU', 'Европа'),
    ('LA', 'Латинская Америка'),
    ('AU', 'Австралазия '),
    ]

# Выбор типа путешествия
TYPE = [
    ('FAM', 'Семейный отдых'),
    ('HON', 'Медовый месяц'),
    ('CPL', 'Отдых для семейной пары'),
    ('SOL', 'Отдых для одного'),
    ('GRP', 'Отдых с группой друзей'),
    ('OTH', 'Другое'),
    ]


# Контактная информация клиента
class Client(models.Model):   
    name = models.CharField(max_length=50, verbose_name='Имя')
    fam = models.CharField(max_length=50, verbose_name='Фамилия')
    otc = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество') # не обязательное поле
    email = models.EmailField()
    phone = models.TextField(max_length=50, null=True, blank=True, verbose_name='Телефон') # не обязательное поле
    add_time = models.DateTimeField(auto_now_add=True) # время добавления записи (ставиться автоматически)
    number = models.CharField(max_length=3, choices=NUMBER, verbose_name='Количество путешественников')
    continent = models.CharField(max_length=2, choices=CONTINENT, verbose_name='Континент')
    type = models.CharField(max_length=3, choices=TYPE, verbose_name='Тип путешествия')
