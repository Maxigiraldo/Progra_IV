from modules.product import Electronic, Food, Clothes
from modules.shop import Shop
import json

path = 'data.json'

def load_products(path):
    with open(path, 'r') as file:
        return json.load(file)

def main():
    data = load_products(path)
    shop = Shop(data, path) # We create the shop object
    while True:
        print("Que desea hacer?")
        print("1. Mostrar productos")
        print("2. Comprar productos")
        print("3. Salir")
        option = input("Ingrese la opcion: ")
        if option == "1":
            shop.show_products()
        elif option == "2":
            order_list = []
            while True:
                name = input("Ingrese el nombre del producto: ")
                # We search for the product in the data
                found = False
                for category, products in data.items():
                    for product in products:
                        if product["name"] == name:
                            print(f"Producto disponible en la categoria {category}")
                            stock = int(input("Ingrese la cantidad: "))
                            order_list.append(shop.order_product(name, stock))
                            found = True
                            break
                    if found:
                        break
                if not found:
                    print("Ese producto no existe")
                
                new_order = input("Desea comprar otro producto? (y/n): ")
                if new_order == "n":
                    break
            print(f"El total a pagar es: {shop.payment(order_list)}")
            shop.save_products()
        elif option == "3":
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()