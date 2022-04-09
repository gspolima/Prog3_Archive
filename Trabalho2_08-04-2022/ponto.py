class Ponto:

    __nome: str;
    __eixo_x: int;
    __eixo_y: int;

    def __init__(self, nome, eixo_x , eixo_y):
        self.__nome = nome
        self.__eixo_x = eixo_x
        self.__eixo_y = eixo_y

    def __str__(self):
        return f'{self.__nome.title()}: ({self.__eixo_x},{self.__eixo_y})'

