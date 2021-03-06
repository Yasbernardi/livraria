# Generated by Django 4.0.6 on 2022-07-07 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_livro_alter_autor_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.editora'),
            preserve_default=False,
        ),
    ]
