# from django.test import TestCase
# from services.pizza.models import PizzaType, Pizza, Transactions
# import decimal
# import random


# # TODO: Test by requesting graphql API (queries, mutations)
# # This are wrong test cases anyway :)

# class PizzaTestClass(TestCase):

#     def test_create_pizza(self):
#         pizza_type = PizzaType.objects.create(name='test type')
#         pizza = Pizza.objects.create(name='Pizza 1', price=decimal.Decimal('100.10'), pizza_type_id=pizza_type.id)
#         self.assertEqual(pizza.name, 'Pizza 1')

#     def test_create_pizza_type(self):
#         pizza_type = PizzaType.objects.create(name='test type')
#         self.assertEqual(pizza_type.name, 'test type')

#     def test_create_transaction(self):
#         pizza_type = PizzaType.objects.create(name='test type')
#         pizza = Pizza.objects.create(
#             name='Pizza 1', price=decimal.Decimal('100.10'), pizza_type_id=pizza_type.id)
#         transactions = [
#             Transactions.objects.create(price=decimal.Decimal(random.randrange(0, 300)) / 100, pizza_id=pizza.id)
#             for i in range(5)
#         ]

#         self.assertEqual(pizza_type.name, 'test type')
#         self.assertEqual(len(transactions), 5)

#     def test_list_pizzas(self):
#         pizza_type = PizzaType.objects.create(name='test type')
#         pizza1 = Pizza.objects.create(
#             name='Pizza 1', price=decimal.Decimal('100.10'), pizza_type_id=pizza_type.id)
#         pizza2 = Pizza.objects.create(
#             name='Pizza 2', price=decimal.Decimal('100.10'), pizza_type_id=pizza_type.id)
#         transactions1 = [
#             Transactions.objects.create(price=decimal.Decimal(random.randrange(0, 300)) / 100, pizza_id=pizza1.id)
#             for i in range(5)
#         ]
#         transactions2 = [
#             Transactions.objects.create(price=decimal.Decimal(random.randrange(0, 300)) / 100, pizza_id=pizza2.id)
#             for i in range(5)
#         ]

#         # This is wrong
#         pizzas = Pizza.objects.all().order_by('-transactions')

#         # test order_by best seller
#         self.assertEqual(pizzas[0].name, 'Pizza 2')
