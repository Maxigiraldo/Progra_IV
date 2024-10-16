import json

class Shop:
    def __init__(self, data, path):
        self.__data = data
        self.__path = path
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def path(self):
        return self.__path
    
    @path.setter
    def path(self, path):
        self.__path = path
    
    def show_products(self):
        print("Productos disponibles:")
        for category, products in self.data.items():  # .items gets the key and value of the dictionary
            print(f"Categoria: {category}")
            for product in products:
                print(f"\tNombre: {product['name']}")
                print(f"\tPrecio: {product['price']}")
                print(f"\tStock: {product['stock']}")
                if category == "Electronics":
                    print(f"\tGarantia: {product['warranty']}")
                elif category == "Food":
                    print(f"\tFecha de vencimiento: {product['expiration_date']}")
                elif category == "Clothes":
                    print(f"\tTalla: {product['size']}")
                print("\n")
            print("\n")
    
    def payment(self, order_list):
        total = 0
        for product in order_list:
            for key in product:
                # Iterating over the dictionary
                for category, items in self.data.items():
                    for item in items:
                        if item["name"] == key:
                            if product[key] >= 5:
                                total += item["price"] * product[key] * 0.8  # 20% discount
                            else:
                                total += item["price"] * product[key]
        return total
    
    def order_product(self, name, stock):
        # We search for the product in the data
        for category, products in self.data.items():
            for product in products:
                if product["name"] == name:
                    if product["stock"] >= stock:
                        product["stock"] -= stock
                        print(f"Se han comprado {stock} {name}")
                        return {name: stock}
                    else:
                        print(f"No hay suficiente cantidad de {name}")
                        return None
        print(f"Producto {name} no encontrado")
        return None
    
    def save_products(self):
        with open(self.path, "w") as file:
            json.dump(self.data, file, indent=4)