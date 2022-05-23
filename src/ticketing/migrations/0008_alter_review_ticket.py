# Generated by Django 4.0.4 on 2022-05-17 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0007_remove_ticket_note_review_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ticket',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_rel', to='ticketing.ticket'),
        ),
    ]