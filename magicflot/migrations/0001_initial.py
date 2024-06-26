# Generated by Django 4.1.13 on 2024-05-21 14:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=300, verbose_name='Вопрос')),
                ('answer_1', models.CharField(max_length=100, null=True, verbose_name='Ответ 1')),
                ('value_1', models.BooleanField(default=False, verbose_name='Верно?')),
                ('answer_2', models.CharField(max_length=100, null=True, verbose_name='Ответ 2')),
                ('value_2', models.BooleanField(default=False, verbose_name='Верно?')),
                ('answer_3', models.CharField(max_length=100, null=True, verbose_name='Ответ 3')),
                ('value_3', models.BooleanField(default=False, verbose_name='Верно?')),
                ('answer_4', models.CharField(max_length=100, null=True, verbose_name='Ответ 4')),
                ('value_4', models.BooleanField(default=False, verbose_name='Верно?')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('play_session_id', models.AutoField(primary_key=True, serialize=False)),
                ('play_session_time', models.DateTimeField(auto_now_add=True)),
                ('is_true_answer', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('school', models.CharField(max_length=30, verbose_name='Школа №')),
                ('the_class', models.CharField(max_length=30, verbose_name='Класс')),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Фамилия',
                'verbose_name_plural': 'Фамилии',
                'ordering': ['last_name'],
            },
        ),
        migrations.AddIndex(
            model_name='winner',
            index=models.Index(fields=['last_name'], name='magicflot_w_last_na_e31a53_idx'),
        ),
        migrations.AddField(
            model_name='statistic',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magicflot.question'),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='magicflot.category', verbose_name='Категория'),
        ),
    ]
