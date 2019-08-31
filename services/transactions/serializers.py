from rest_framework.serializers import HyperlinkedModelSerializer, \
    Serializer, CharField, DecimalField

from services.transactions.models import Product, Transaction


class ProductSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'city',)


class TransactionSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'amount', 'product', 'date_time',)


class ProductSummarySerializer(Serializer):
    product_name = CharField(source='product__name')
    total_amount = DecimalField(
        max_digits=11,
        decimal_places=2,
        source='amount__sum')

    class Meta:
        fields = ('product_name', 'total_amount',)


class CitySummarySerializer(Serializer):
    city_name = CharField(source='product__city')
    total_amount = DecimalField(
        max_digits=11,
        decimal_places=2,
        source='amount__sum')

    class Meta:
        fields = ('city_name', 'total_amount',)
