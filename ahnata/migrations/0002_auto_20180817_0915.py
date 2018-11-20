# Generated by Django 2.0.6 on 2018-08-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahnata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ('-date_ajout',)},
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='categorie',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='available',
            new_name='disponible',
        ),
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=2, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_logo',
            field=models.ImageField(blank=True, upload_to='ahnata/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='nom',
            field=models.CharField(db_index=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='category',
            name='nom',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterIndexTogether(
            name='articles',
            index_together={('id', 'slug')},
        ),
    ]
