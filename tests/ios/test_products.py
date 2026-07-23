from pages.products_page import ProductsPage


def test_sort_price_ascending(driver):

    product = ProductsPage(driver)

    product.sort_price_ascending()

    assert product.first_price() == "$7.99"