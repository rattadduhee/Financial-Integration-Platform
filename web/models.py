# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('WebUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class WebApartment(models.Model):
    id = models.BigAutoField(primary_key=True)
    apt_name = models.CharField(max_length=100)
    area = models.IntegerField()
    price = models.IntegerField()
    floor = models.IntegerField()
    arc_year = models.IntegerField()
    gu = models.CharField(max_length=10)
    dong = models.CharField(max_length=10)
    pyeong = models.IntegerField()
    cont_year = models.IntegerField()
    age = models.IntegerField()
    

    class Meta:
        managed = False
        db_table = 'web_apartment'


class WebCard(models.Model):
    age = models.CharField(max_length=100)
    card_name = models.CharField(max_length=100)
    benefit1 = models.CharField(max_length=100)
    benefit2 = models.CharField(max_length=100)
    benefit3 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'web_card'


class WebConsume(models.Model):
    username = models.ForeignKey('WebUser', models.DO_NOTHING, db_column='username')
    food = models.IntegerField()
    cafe = models.IntegerField()
    shopping = models.IntegerField()
    education = models.IntegerField()
    leisure = models.IntegerField()
    medical = models.IntegerField()
    traffic = models.IntegerField()
    life = models.IntegerField()
    travel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'web_consume'


class WebSaving(models.Model):
    saving_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    interest_rate = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'web_saving'


class WebUser(AbstractUser):
    password = models.CharField(max_length=128)
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254)
    age = models.CharField(max_length=50)
    child = models.CharField(max_length=10)
    Marriage = models.CharField(max_length=10)  # Field name made lowercase.
    work = models.CharField(max_length=10)
    work_address = models.CharField(max_length=100)
    hope_address = models.CharField(max_length=100)
    available_asset = models.CharField(max_length=100)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password','age','hope_address','available_asset']
    
    class Meta(AbstractUser.Meta):
        managed = False
        db_table = 'web_user'



class WebUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(WebUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'web_user_groups'
        unique_together = (('user', 'group'),)


class WebUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(WebUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'web_user_user_permissions'
        unique_together = (('user', 'permission'),)

class StockAct(models.Model):
    id = models.BigAutoField(primary_key=True)
    act = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_act'


class StockChart(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    open = models.FloatField()
    close = models.FloatField()
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'stock_chart'


class StockInteg(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    close = models.IntegerField()
    diff = models.IntegerField(blank=True, null=True)
    diff_ratio = models.CharField(max_length=10, blank=True, null=True)
    open = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    volume = models.IntegerField()
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'stock_integ'