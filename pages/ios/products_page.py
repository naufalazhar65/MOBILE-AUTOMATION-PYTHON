from pages.ios.base_page import BasePage
from locators.ios.products_locator import ProductsLocator


class ProductsPage(BasePage):

    def open_sort(self):
        self.click(ProductsLocator.SORT_BUTTON)

    def sort_name_ascending(self):
        self.open_sort()
        self.click(ProductsLocator.NAME_ASC)

    def sort_name_descending(self):
        self.open_sort()
        self.click(ProductsLocator.NAME_DESC)

    def sort_price_ascending(self):
        self.open_sort()
        self.click(ProductsLocator.PRICE_ASC)

    def sort_price_descending(self):
        self.open_sort()
        self.click(ProductsLocator.PRICE_DESC)

    def first_product(self):
        return self.get_text(ProductsLocator.FIRST_PRODUCT)

    def first_price(self):
        return self.get_text(ProductsLocator.FIRST_PRICE)