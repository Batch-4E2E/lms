# Generated by Django 4.1.13 on 2024-03-31 10:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lmsapp", "0004_remove_book_user_booklending"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="booklending",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="booklending",
            name="book",
        ),
    ]
