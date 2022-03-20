# Generated by Django 4.0.3 on 2022-03-20 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название курса')),
            ],
        ),
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='Оценка')),
                ('updated_at', models.DateTimeField()),
                ('homework', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.homework')),
            ],
        ),
        migrations.CreateModel(
            name='HomeAssignment',
            fields=[
                ('task', models.TextField(verbose_name='Задание')),
                ('updated_at', models.DateTimeField()),
                ('score', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='course.score')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('updated_at', models.DateTimeField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t_comments', to='course.score')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ManyToManyField(related_name='teachers', to='course.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('updated_at', models.DateTimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_comments', to='course.score')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ManyToManyField(related_name='courses', to='course.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.teacher'),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название лекции')),
                ('file', models.FileField(upload_to='uploads/')),
                ('updated_at', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.teacher')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='course.course')),
            ],
        ),
        migrations.AddField(
            model_name='homework',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeworks', to='course.student'),
        ),
        migrations.AddField(
            model_name='homework',
            name='home_assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.homeassignment'),
        ),
        migrations.AddField(
            model_name='homeassignment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.teacher'),
        ),
        migrations.AddField(
            model_name='homeassignment',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_assignments', to='course.lecture'),
        ),
    ]
