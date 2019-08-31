"""API view sets for rest-api

    Reference: https://www.django-rest-framework.org/tutorial/quickstart/#views
"""

from datetime import timedelta
from django.utils import timezone
from django.db.models import Sum

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pizza_transaction.transactions.mixins import \
    MultiSerializerViewSetMixin
from pizza_transaction.transactions.models import Product, Transaction
from pizza_transaction.transactions.serializers import ProductSerializer, \
    TransactionSerializer, ProductSummarySerializer, CitySummarySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TransactionViewSet(
        MultiSerializerViewSetMixin,
        viewsets.ModelViewSet):
    """
    API endpoint that allows transactions to be viewed or edited.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    """
    Action serializer map
    MultipleSerializerViewSetMixin.get_serializer_class
    will automatically determin the serializer
    """
    serializer_action_classes = {
        'product_summary': ProductSummarySerializer,
        'manufacturing_city_summary': CitySummarySerializer
    }

    def _create_summary_response(self, value, last_n_days):
        threshold = timezone.now() - timedelta(days=int(last_n_days))
        summary = Transaction.objects.\
            values(value).\
            annotate(Sum('amount')).\
            filter(date_time__date__gte=threshold)
        serializer = self.get_serializer(summary, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['get'],
        url_path='products/summary/(?P<last_n_days>[0-9]+)')
    def product_summary(self, request, last_n_days):
        """
        Equivalent of API
        /assignment/transactionSummaryByProducts/{last_n_days}
        """
        return self._create_summary_response('product__name', last_n_days)

    @action(
        detail=False,
        methods=['get'],
        url_path='manufacturing-cities/summary/(?P<last_n_days>[0-9]+)')
    def manufacturing_city_summary(self, request, last_n_days):
        """
        Equivalent of API
        /assignment/transactionSummaryByManufacturingCity/{last_n_days}
        """
        return self._create_summary_response('product__city', last_n_days)
