from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        help_text='Product name',
    )
    city = models.CharField(
        max_length=100,
        help_text='Product manufacturing city',
    )

    def __str__(self):
        # Return product name when serialized
        return self.name


class Transaction(models.Model):
    amount = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        help_text='Transaction amount',
    )
    product = models.ForeignKey(
        Product,
        # related_name='transaction_product',
        on_delete=models.CASCADE,
        help_text='Transaction product',
    )

    date_time = models.DateTimeField(
        help_text='Transaction date time',
    )
