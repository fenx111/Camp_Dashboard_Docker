from django.db import models
from django.utils import timezone

class Parent(models.Model):
    last_name = models.CharField(max_length=250)  # фамилия
    first_name = models.CharField(max_length=250)  # имя
    middle_name = models.CharField(max_length=250)  # отчество
    contact_phone = models.CharField(max_length=250)  # контактый телефон

    def __str__(self):
        return self.contact_phone

class Documents(models.Model):
    TYPES_DOC = (
        ('BC', 'Свидетельство о рождении'),
        ('PA', 'Паспорт'),
    )
    type_doc = models.CharField(max_length=250, choices=TYPES_DOC)  # тип документа
    svidetelstvo = models.CharField(max_length=250)  # свидетельство
    passport = models.CharField(max_length=250, null=True)  # паспорт

    def __str__(self):
        return self.type_doc

class Camp(models.Model):
    title = models.CharField(max_length=250)  # название
    label = models.CharField(max_length=250)  # картинка

    def __str__(self):
        return self.title

class Medicine(models.Model):
    last_name = models.CharField(max_length=250)  # фамилия
    first_name = models.CharField(max_length=250)  # имя
    middle_name = models.CharField(max_length=250)  # отчество
    contact_phone = models.CharField(max_length=250)  # контактый телефон
    special = models.CharField(max_length=250)  # специальность работы
    fk_camp = models.ForeignKey(Camp, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

class Leader(models.Model):
    last_name = models.CharField(max_length=250)  # фамилия
    first_name = models.CharField(max_length=250)  # имя
    middle_name = models.CharField(max_length=250)  # отчество
    contact_phone = models.CharField(max_length=250)  # контактый телефон

    def __str__(self):
        return self.first_name

class Squad(models.Model):
    nick = models.CharField(max_length=250)  # название
    slogan = models.CharField(max_length=250)  # девиз
    fk_leader = models.ForeignKey(Leader, on_delete=models.CASCADE)  # вожатый
    fk_camp = models.ForeignKey(Camp, on_delete=models.CASCADE)

    def __str__(self):
        return self.nick

class Children(models.Model):
    last_name = models.CharField(max_length=250)  # фамилия
    first_name = models.CharField(max_length=250)  # имя
    middle_name = models.CharField(max_length=250)  # отчество
    contact_phone = models.CharField(max_length=250)  # контактый телефон
    birthday = models.CharField(max_length=250)  # день рождения
    fk_parent = models.ForeignKey(Parent, on_delete=models.CASCADE)  # родитель
    fk_document = models.ForeignKey(Documents, on_delete=models.CASCADE)  # документы
    mtm_squad = models.ManyToManyField(Squad)

    def __str__(self):
        return self.first_name

class Post(models.Model):
    title = models.CharField(max_length=250)  # название
    content = models.TextField()  # контент
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    picture = models.CharField(max_length=250, null=True)  # картинка
    video = models.CharField(max_length=250, null=True)  # видео
    mtm_squad = models.ManyToManyField(Squad)

class Transactions (models.Model):
   TYPES_TRANSACTIONS = (
       ('WO', 'Списание'),
       ('RE', 'Пополнение'),
   )
   total = models.CharField(max_length=250) # сумма
   description = models.CharField(max_length=250) # описание
   date = models.DateTimeField(default=timezone.now)
   types = models.CharField(max_length=250, choices=TYPES_TRANSACTIONS)

   def __str__(self):
        return self.total

class Score (models.Model):
   balance = models.CharField(max_length=250) # название
   children = models.ForeignKey(Children, on_delete=models.CASCADE) # ребенок
   transactions = models.ForeignKey(Transactions, on_delete=models.CASCADE)

   def __str__(self):
        return self.balance