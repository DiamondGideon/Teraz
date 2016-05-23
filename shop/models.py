from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import transaction

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_(u"Пользователь"))
    balance = models.IntegerField(default=0, verbose_name=_(u"баланс"))
    info = models.TextField(null= True)
    phone = models.CharField(max_length = 200, null= True)
    skype = models.CharField(max_length = 200, null= True)
    address = models.CharField(max_length = 200, null= True)


    def __str__(self):
        return "%s's profile" % self.user
    def get_balance(self):
        return self.balance
    def set_balance(self, new):
        self.balance = self.balance + new
        return self.balance

class Bucket(models.Model):
    owner = models.OneToOneField(UserProfile)



class Category(models.Model):
    chield = models.ManyToManyField("self", blank=True)
    title = models.CharField(max_length = 200)
    pic = models.ImageField()


class Post(models.Model):
    author = models.ForeignKey(UserProfile, verbose_name=_(u"Автор"))
    category = models.ForeignKey(Category, null = True)
    bucket = models.ForeignKey(Bucket, null = True)
    title = models.CharField(max_length=200, verbose_name=_(u"Титл"))
    text = models.TextField()
    type = models.SmallIntegerField(default = 1)
    isAccept = models.PositiveSmallIntegerField(default = 0)
    price = models.IntegerField(default = 0)
    cur_price = models.IntegerField(default = 0)
    discount = models.SmallIntegerField(default = 0)
    pic = models.ImageField(null = True)
    sold = models.BooleanField(default = False)

    # win_coef = models.PositiveSmallIntegerField(default=0, verbose_name=_(u"Коэфициен на победу"))
    # result = models.SmallIntegerField(null = True, verbose_name=_(u"результат"))
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True, verbose_name=_(u"дата публикации"))


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



# class RGroup(models.Model):
#     group_name = models.CharField(max_length=100, verbose_name=_(u"Название Группы"))
#     keyword = models.CharField(max_length= 200, verbose_name=_(u"Ключевые слова"))
#     sub_groups = models.ManyToManyField('self', through='SubGroup', symmetrical=False)
#     # group_image = models.ImageField
#
#
#     def validate_no_group_loops(self, seen=None):
#         if seen is None:
#             seen = []
#         if self.id in seen:
#             raise ValidationError("LOOP DETECTED")
#         seen.append(self.id)
#         for sub_group in self.target.all():
#             sub_group.target.validate_no_group_loops(seen)
#
#     def clean(self):
#         self.validate_no_group_loops()
#
#     def save(self, *args, **kwargs):
#         super(RGroup, self).save(*args, **kwargs)
#         try:
#             self.validate_no_group_loops()
#         except ValidationError as e:
#             transaction.rollback()
#             raise e
#         else:
#             transaction.commit()
#
#
# class RItem(models.Model):
#     group = models.ForeignKey(RGroup, verbose_name=_(u"Группа"))
#     # item_image
#
#
# class Rcharact(models.Model):
#     chara


class Bet(models.Model):
        user = models.ForeignKey(User , verbose_name=_(u"пользователь"))
        bet = models.IntegerField(default=0, verbose_name=_(u"ставка"))
        result = models.CharField(max_length=20, verbose_name=_(u"результат"))
        product = models.ForeignKey(Post, verbose_name=_(u"продукт"))

        def __str__(self):
            return str(self.user.username)
