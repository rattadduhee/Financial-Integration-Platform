# Generated by Django 4.1.1 on 2022-10-22 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WebUser",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
                ("age", models.CharField(max_length=50)),
                ("child", models.CharField(max_length=10)),
                ("marriage", models.CharField(db_column="Marriage", max_length=10)),
                ("work", models.CharField(max_length=10)),
                ("work_address", models.CharField(max_length=100)),
                ("hope_address", models.CharField(max_length=100)),
                ("available_asset", models.CharField(max_length=100)),
            ],
            options={"db_table": "web_user", "abstract": False, "managed": False,},
        ),
        migrations.CreateModel(
            name="ApartInfo",
            fields=[
                (
                    "apt_name",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("size", models.IntegerField(blank=True, null=True)),
                ("price", models.IntegerField(blank=True, null=True)),
                ("layer", models.IntegerField(blank=True, null=True)),
                ("bir_year", models.IntegerField(blank=True, null=True)),
                ("gu", models.CharField(blank=True, max_length=10, null=True)),
                ("dong", models.CharField(blank=True, max_length=10, null=True)),
                ("pyeong", models.IntegerField(blank=True, null=True)),
                ("con_year", models.IntegerField(blank=True, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
            ],
            options={"db_table": "apart_info", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={"db_table": "auth_group", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[("id", models.BigAutoField(primary_key=True, serialize=False)),],
            options={"db_table": "auth_group_permissions", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={"db_table": "auth_permission", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={"db_table": "django_admin_log", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={"db_table": "django_content_type", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={"db_table": "django_migrations", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={"db_table": "django_session", "managed": False,},
        ),
        migrations.CreateModel(
            name="WebApartment",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("area", models.IntegerField()),
                ("day", models.IntegerField()),
                ("price", models.IntegerField()),
                ("floor", models.IntegerField()),
                ("arc_year", models.IntegerField()),
                ("gu", models.IntegerField()),
                ("dong", models.IntegerField()),
                ("pyeong", models.IntegerField()),
                ("cont_year", models.IntegerField()),
                ("cont_mon", models.IntegerField()),
                ("river", models.IntegerField()),
                ("age", models.IntegerField()),
                ("rebuild", models.IntegerField()),
                ("apt_name", models.CharField(max_length=100)),
            ],
            options={"db_table": "web_apartment", "managed": False,},
        ),
        migrations.CreateModel(
            name="WebCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("age", models.CharField(max_length=100)),
                ("card_name", models.CharField(max_length=100)),
                ("benefit1", models.CharField(max_length=100)),
                ("benefit2", models.CharField(max_length=100)),
                ("benefit3", models.CharField(max_length=100)),
            ],
            options={"db_table": "web_card", "managed": False,},
        ),
        migrations.CreateModel(
            name="WebConsume",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("food", models.IntegerField()),
                ("cafe", models.IntegerField()),
                ("shopping", models.IntegerField()),
                ("education", models.IntegerField()),
                ("leisure", models.IntegerField()),
                ("medical", models.IntegerField()),
                ("traffic", models.IntegerField()),
                ("life", models.IntegerField()),
                ("travel", models.IntegerField()),
            ],
            options={"db_table": "web_consume", "managed": False,},
        ),
        migrations.CreateModel(
            name="WebSaving",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("saving_name", models.CharField(max_length=100)),
                ("age", models.CharField(max_length=100)),
                ("period", models.CharField(max_length=100)),
                ("price", models.CharField(max_length=100)),
                ("interest_rate", models.CharField(max_length=100)),
            ],
            options={"db_table": "web_saving", "managed": False,},
        ),
        migrations.CreateModel(
            name="WebUserGroups",
            fields=[("id", models.BigAutoField(primary_key=True, serialize=False)),],
            options={"db_table": "web_user_groups", "managed": False,},
        ),
        migrations.CreateModel(
            name="WebUserUserPermissions",
            fields=[("id", models.BigAutoField(primary_key=True, serialize=False)),],
            options={"db_table": "web_user_user_permissions", "managed": False,},
        ),
    ]
