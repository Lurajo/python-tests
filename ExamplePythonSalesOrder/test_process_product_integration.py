from datetime import datetime

from Entities.Customer import Customer
from Entities.Order import Order
from Entities.OrderProduct import OrderProduct
from Entities.Product import Product
from Repositories.CustomerRepository import CustomerRepository
from Repositories.ProductRepository import ProductRepository


def test_process_product_integration():
    # Arrange
    customer1 = Customer(1, "Customer 1")
    customer_repository = CustomerRepository()

    product1 = Product(1, "Product 1", 5.00, 10)
    product_repository = ProductRepository()

    order1 = Order(1, customer1, datetime.today())

    order_product1 = OrderProduct()
    order_product2 = OrderProduct()

    # Act
    customer_repository.append_customer(customer1)
    product_repository.append_product(product_repository)

    order_product1.add_product(product1, 5)
    order_product2.add_product(product1, 6)

    order1.add_order_product(order_product1)
    order1.add_order_product(order_product2)

    order1.update_total_price()

    # Assert
    assert hasattr(order_product2, "product") == False
    assert product1.stock == 5
    assert order1.total_price == order_product1.value_item
