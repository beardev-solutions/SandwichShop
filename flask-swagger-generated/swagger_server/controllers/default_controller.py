import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server import util


def orders_create_order_order_post(order):  # noqa: E501
    """Create a new order

     # noqa: E501

    :param order: Product Order
    :type order: str

    :rtype: None
    """
    return 'do some magic!'


def products_add_product_name_nameproduct_namepriceproduct_price_post(product_name, product_price):  # noqa: E501
    """Add a new item to menu

     # noqa: E501

    :param product_name: Name of the product
    :type product_name: str
    :param product_price: Name of the product
    :type product_price: int

    :rtype: None
    """
    return 'do some magic!'


def products_get_all_products_get():  # noqa: E501
    """Returns a list of all the products available

     # noqa: E501


    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def products_prices_product_id_get(product_id):  # noqa: E501
    """Returns the price (rounded up) of a single product based on productId

     # noqa: E501

    :param product_id: Unique product Id
    :type product_id: int

    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def products_product_id_get(product_id):  # noqa: E501
    """Returns a product/product name based on its unique product id

     # noqa: E501

    :param product_id: Unique prouduct ID
    :type product_id: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def products_remove_product_product_id_delete(product_id):  # noqa: E501
    """Delete an item based on product id provided

     # noqa: E501

    :param product_id: Unique Product Id
    :type product_id: int

    :rtype: None
    """
    return 'do some magic!'


def products_update_price_pidproduct_idnew_pricenew_price_put(product_id, new_price):  # noqa: E501
    """Update the price of a an item

     # noqa: E501

    :param product_id: Unique id of product
    :type product_id: str
    :param new_price: New price of Product
    :type new_price: int

    :rtype: None
    """
    return 'do some magic!'
