# Generated by Django 2.0.6 on 2018-08-17 07:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prix', models.FloatField()),
                ('description', models.CharField(max_length=30)),
                ('article_logo', models.ImageField(blank=True, upload_to='ahnata/images/fer.png')),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('date_ajout', models.DateTimeField(default=django.utils.timezone.now, verbose_name="date d'ajout")),
                ('date_modif', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date de modification')),
            ],
        ),
        migrations.CreateModel(
            name='Boutique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('stock_gerant', models.CharField(max_length=30)),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now, verbose_name="date d'ajout")),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('adresse', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(db_index=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.IntegerField(blank=True, null=True)),
                ('a_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('adresse', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vendeurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('adresse', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('produits', models.ManyToManyField(related_name='_vendeurs_produits_+', through='ahnata.Offre', to='ahnata.Produit')),
                ('produits_sans_prix', models.ManyToManyField(related_name='vendeurs', to='ahnata.Produit')),
            ],
        ),
        migrations.AddField(
            model_name='offre',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ahnata.Produit'),
        ),
        migrations.AddField(
            model_name='offre',
            name='vendeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ahnata.Vendeurs'),
        ),
        migrations.AddField(
            model_name='boutique',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ahnata.Category'),
        ),
        migrations.AddField(
            model_name='articles',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ahnata.Category'),
        ),
    ]
