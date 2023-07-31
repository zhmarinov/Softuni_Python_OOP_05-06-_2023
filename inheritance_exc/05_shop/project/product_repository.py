from typing import List

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, name: str):

        res = [pr for pr in self.products if pr.name == name]
        if res:
            return res[0]

    def remove(self, name: str):
        product = self.find(name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f"{pr.name}: {pr.quantity}" for pr in self.products])


