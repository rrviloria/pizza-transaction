from datetime import datetime, timedelta
from django.test import TestCase, Client

from api.transactions.models import Product, Transaction


class TransactionAPITest(TestCase):
    """
    Test case for Transaction APIs
    This only focuses on the APIs defined on the assignment
    """

    def setUp(self):
        self.client = Client()

    def test_get_transactions_request(self):
        # TODO: Use factory_boy for data creation
        product = Product.objects.create(
            name='pizza', city='makati'
        )
        length = 50
        for i in range(length):
            Transaction.objects.create(
                amount=(50.00 * i),
                date_time=datetime.now(),
                product=product
            )
        response = self.client.get('/transactions/')

        # Test if request returns sucessfully
        self.assertEquals(response.status_code, 200)
        # Test if transactions count is equal to DB record count
        self.assertEquals(len(response.data), length)
        # Test if product name is `pizza`
        self.assertEquals(response.data[0]['product'], 'pizza')

    def test_get_transaction_by_id_request(self):
        # TODO: Use factory_boy for data creation
        product = Product.objects.create(
            name='pizza', city='makati'
        )
        transaction = Transaction.objects.create(
            amount=50.00,
            date_time=datetime.now(),
            product=product
        )

        response = self.client.get(
            '/transactions/%s/' % transaction.id)
        # Test if request returns sucessfully
        self.assertEquals(response.status_code, 200)
        # # Test if product name is `pizza`
        self.assertEquals(response.data['product'], 'pizza')
        # Test if amount is `50.00`
        self.assertEquals(float(response.data['amount']), 50.00)

    def test_get_transaction_by_id_fail_request(self):
        # `1` does not exist on database
        response = self.client.get('/transactions/%s/' % 1)
        # Test if request returns 404
        self.assertEquals(response.status_code, 404)

    def test_get_summary_by_product_request(self):
        (pizza_total_amount,
         pasta_total_amount,
         last_n_days) = self._create_summary_data()
        response = self.client.get(
            '/transactions/products/summary/%s/' % last_n_days)

        products = {}
        for name in ['pizza', 'pasta']:
            for item in response.data:
                if item['product_name'] == name:
                    products[name] = item

        # Test if request returns sucessfully
        self.assertEquals(response.status_code, 200)
        # Test if only 2 products are counted.
        # No transaction for product `salad` so it should not be counted
        self.assertEquals(len(response.data), 2)
        # Test if counted total amout for pizza is the same from response
        self.assertEquals(
            float(products['pizza']['total_amount']),
            pizza_total_amount)
        # Test if counted total amout for pasta is the same from response
        self.assertEquals(
            float(products['pasta']['total_amount']),
            pasta_total_amount)

    def test_get_summary_by_city_request(self):
        (makati_total_amount,
         pasig_total_amount,
         last_n_days) = self._create_summary_data()
        response = self.client.get(
            '/transactions/manufacturing-cities/summary/%s/' % last_n_days)

        cities = {}
        for name in ['makati', 'pasig']:
            for item in response.data:
                if item['city_name'] == name:
                    cities[name] = item

        # Test if request returns sucessfully
        self.assertEquals(response.status_code, 200)
        # Test if only 2 cities are counted.
        # No transaction for city `marikina` so it should not be counted
        self.assertEquals(len(response.data), 2)
        # Test if counted total amout for makati is the same from response
        self.assertEquals(
            float(cities['makati']['total_amount']),
            makati_total_amount)
        # Test if counted total amount for pasig is the same from response
        self.assertEquals(
            float(cities['pasig']['total_amount']),
            pasig_total_amount)

    def _create_summary_data(self):
        # TODO: Use factory_boy for data creation
        product1 = Product.objects.create(
            name='pizza', city='makati'
        )
        product2 = Product.objects.create(
            name='pasta', city='pasig'
        )
        # This should not be included on the response
        # because no transactions are created
        Product.objects.create(
            name='salad', city='marikina'
        )
        last_n_days = 5
        pizza_length = 3
        pasta_length = 5
        pizza_total_amount = 0
        pasta_total_amount = 0
        for i in range(1, pizza_length + 1):
            amount = (10.00 * i)
            Transaction.objects.create(
                amount=amount,
                date_time=datetime.now() - timedelta(days=i),
                product=product1
            )
            pizza_total_amount += amount

        # This should not count on the total amount computation
        Transaction.objects.create(
            amount=500.00,
            date_time=datetime.now() - timedelta(days=last_n_days + 2),
            product=product1
        )

        for i in range(1, pasta_length + 1):
            amount = (20.00 * i)
            Transaction.objects.create(
                amount=amount,
                date_time=datetime.now(),
                product=product2
            )
            pasta_total_amount += amount

        return pizza_total_amount, pasta_total_amount, last_n_days
