# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_orders_create_order_order_post(self):
        """Test case for orders_create_order_order_post

        Create a new order
        """
        response = self.client.open(
            '/dhillondemos/SandwichShop/1/orders/createOrder/{order}'.format(order='order_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_add_product_name_nameproduct_namepriceproduct_price_post(self):
        """Test case for products_add_product_name_nameproduct_namepriceproduct_price_post

        Add a new item to menu
        """
        response = self.client.open(
            '/dhillondemos/SandwichShop/1/products/addProduct/name/name={productName}&price={productPrice}'.format(product_name='product_name_example', product_price=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_get_all_products_get(self):
        """Test case for products_get_all_products_get

        Returns a list of all the products available
        """
        response = self.client.open(
            '/dhillondemos/SandwichShop/1/products/getAllProducts',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_prices_product_id_get(self):
        """Test case for products_prices_product_id_get

        Returns the price (rounded up) of a single product based on productId
        """
        response = self.client.open(
            '/dhillondemos/SandwichShop/1/products/prices/{productId}'.format(product_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_product_id_get(self):
        """Test case for products_product_id_get

        Returns a product/product name based on its unique product id
        """
        response = self.client.open(
            '/dhillondemos/SandwichShop/1/products/{productId}'.format(product_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_remove_product_product_id_delete(self):
        """Test case for products_remove_product_product_id_delete

        Delete an item based on product id provided
        """
        response = self.client.open(
            '/dhillondemos/SandwichShop/1/products/removeProduct/{productId}'.format(product_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_update_price_pidproduct_idnew_pricenew_price_put(self):
        """Test case for products_update_price_pidproduct_idnew_pricenew_price_put

        Update the price of a an item
        """
        response = self.client.open(
            '/dhillondemos/SandwichShop/1/products/updatePrice/pid={productId}&newPrice={newPrice}'.format(product_id='product_id_example', new_price=56),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
