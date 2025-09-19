class Product:
    def __init__(self, id, name, category, price, weight, description=""):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.weight = weight
        self.description = description

    def str(self):
        return f"{self.name} - ${self.price} ({self.category}, {self.weight}g)"

    def display_details(self):
        return f"""
{self.name}
Категория: {self.category}
Цена: ${self.price}
Вес: {self.weight}g
Описание: {self.description}
        """


class ProductCatalog:
    def __init__(self):
        self.products = []
        self.next_id = 1

    def add_product(self, name, category, price, weight, description=""):
        product = Product(self.next_id, name, category, price, weight, description)
        self.products.append(product)
        self.next_id += 1
        return product

    def edit_product(self, product_id, **kwargs):
        product = self.get_product_by_id(product_id)
        if product:
            for key, value in kwargs.items():
                if hasattr(product, key):
                    setattr(product, key, value)
            return product
        return None

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def get_products_by_category(self, category):
        return [p for p in self.products if p.category == category]

    def get_all_products(self):
        return self.products


class CartItem:
    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity

class ShoppingCart:
    def __init__(self, catalog):
        self.items = []
        self.catalog = catalog

    def add_to_cart(self, product_id, quantity=1):
        product = self.catalog.get_product_by_id(product_id)
        if product:
            for item in self.items:
                if item.product.id == product_id:
                    item.quantity += quantity
                    return True
            self.items.append(CartItem(product, quantity))
            return True
        return False

    def display_cart(self):
        print("\n=== ВАША КОРЗИНА ===")
        if not self.items:
            print("Корзина пуста.")
        else:
            for item in self.items:
                print(f"{item.product.name} x {item.quantity} = ${item.get_total_price()}")

    def get_items_for_sorting(self):
        return self.items.copy()

class SortingAlgorithms:
    @staticmethod
    def quick_sort(items, key='price', reverse=False):
        if len(items) <= 1:
            return items

        pivot = items[len(items) // 2]

        if key == 'price':
            pivot_val = pivot.product.price
        elif key == 'weight':
            pivot_val = pivot.product.weight
        elif key == 'category':
            pivot_val = pivot.product.category
        elif key == 'name':
            pivot_val = pivot.product.name

        left = []
        middle = []
        right = []

        for item in items:
            if key == 'price':
                item_val = item.product.price
            elif key == 'weight':
                item_val = item.product.weight
            elif key == 'category':
                item_val = item.product.category
            elif key == 'name':
                item_val = item.product.name

            if item_val < pivot_val:
                left.append(item)
            elif item_val == pivot_val:
                middle.append(item)
            else:
                right.append(item)

        if reverse:
            return SortingAlgorithms.quick_sort(right, key, reverse) + middle + SortingAlgorithms.quick_sort(left, key, reverse)
        else:
            return SortingAlgorithms.quick_sort(left, key, reverse) + middle + SortingAlgorithms.quick_sort(right, key, reverse)

    @staticmethod
    def merge_sort(items, key='price', reverse=False):
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left = SortingAlgorithms.merge_sort(items[:mid], key, reverse)
        right = SortingAlgorithms.merge_sort(items[mid:], key, reverse)

        return SortingAlgorithms.merge(left, right, key, reverse)

    @staticmethod
    def merge(left, right, key, reverse):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if key == 'price':
                left_val = left[i].product.price
                right_val = right[j].product.price
            elif key == 'weight':
                left_val = left[i].product.weight
                right_val = right[j].product.weight
            elif key == 'category':
                left_val = left[i].product.category
                right_val = right[j].product.category
            elif key == 'name':
                left_val = left[i].product.name
                right_val = right[j].product.name

            if reverse:
                if left_val >= right_val:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            else:
                if left_val <= right_val:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

catalog = ProductCatalog()

catalog.add_product("Яблоки", "Фрукты", 1.2, 100)
catalog.add_product("Бананы", "Фрукты", 0.5, 120)
catalog.add_product("Молоко", "Напитки", 1.5, 1000)
catalog.add_product("Хлеб", "Выпечка", 0.8, 500)
catalog.add_product("Сыр", "Молочные", 3.0, 200)
catalog.add_product("Вода", "Напитки", 0.5, 1500)

cart = ShoppingCart(catalog)

cart.add_to_cart(1, 3)  # 3 единицы Яблок
cart.add_to_cart(2, 2)  # 2 единицы Бананов
cart.add_to_cart(3, 1)  # 1 единица Молока
cart.add_to_cart(4, 1)  # 1 единица Хлеба
cart.add_to_cart(5, 2)  # 2 единицы Сыра
cart.add_to_cart(6, 4)  # 4 единицы Воды

print("=== КОРЗИНА ДО СОРТИРОВКИ ===")
cart.display_cart()


