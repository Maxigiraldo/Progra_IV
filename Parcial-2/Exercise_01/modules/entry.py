class Books:
    def __init__(self, tittle: str, ISBN: int, publisher: str, author: str, publication_date: int, review: str, genre: str, sub_genre: str):
        self.__tittle = tittle
        self.__ISBN = ISBN
        self.__publisher = publisher
        self.__author = author
        self.__publication_date = publication_date
        self.__review = review
        self.__genre = genre
        self.__sub_genre = sub_genre
        
    def set_tittle(self, tittle):
        self.__tittle = tittle
        
    def get_tittle(self):
        return self.__tittle
    
    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN
        
    def get_ISBN(self):
        return self.__ISBN
    
    def set_publisher(self, publisher):
        self.__publisher = publisher
        
    def get_publisher(self):
        return self.__publisher
    
    def set_author(self, author):
        self.__author = author
        
    def get_author(self):
        return self.__author
    
    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date
        
    def get_publication_date(self):
        return self.__publication_date
    
    def set_review(self, review):
        self.__review = review
        
    def get_review(self):
        return self.__review
    
    def set_genre(self, genre):
        self.__genre = genre
        
    def get_genre(self):
        return self.__genre
    
    def set_sub_genre(self, sub_genre):
        self.__sub_genre = sub_genre
        
    def get_sub_genre(self):
        return self.__sub_genre
    
    def register_books(self):
        data = {
            "titulo":self.get_tittle(),
            "ISBN": self.get_ISBN(),
            "editorial":self.get_publisher(),
            "autor": self.get_author(),
            "fecha de publicacion": self.get_publication_date(),
            "reseña":self.get_review(),
            "genero":self.get_genre(),
            "sub_genero":self.get_sub_genre()
        }
        return data