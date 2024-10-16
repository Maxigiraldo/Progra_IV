from modules.generator import Generator
from modules.entry import Books
from modules.read import Read

path = "data.json"

def entry_data():
    tittle = input("Ingrese el titulo del libro: ")
    ISBN = int(input("Ingrese el ISBN del libro: "))
    publisher = input("Ingrese la editorial del libro: ")
    author = input("Ingrese el autor del libro: ")
    publication_date = input("Ingrese el año de publicacion del libro: ")
    review = input("Ingrese la reseña del libro: ")
    genre = input("Ingrese el genero del libro: ")
    print("Ingrese un subgenero del libro o ingrese un NO: ")
    list = []
    while True:
        subreview = input("Ingrese el subgenero: ")
        if subreview.upper() == "NO":
            break
        list.append(subreview)
    book = Books(tittle, ISBN, publisher, author, publication_date, review, genre, list)
    return book.register_books()

def main():
    while True:
        print("1. Ingresar libro")
        print("2. Mostrar libros")
        print("3. Salir")
        option = int(input("Ingrese la opción: "))
        if option == 1:
            data = entry_data()
            generator = Generator(data,path)
            generator.generate_json()
        elif option == 2:
            reader = Read(path)
            data = reader.read_json()
            if data != None:
                reader.show_data(data)
        elif option == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no valida")

if __name__ == "__main__":
    main()
