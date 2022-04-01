class Automovel(object):
    _placa: str
    _velocidade: float
    def __init__(self, placa, velocidade):
        self._placa = placa
        self._velocidade = velocidade

    def get_placa(self) -> str:
        return self._placa

    def dirigir(self) -> None:
        print(f'Estou dirigindo a {self._velocidade} Km/h!')

    def acelerar(self, valor_acelerado: float) -> None:
        if (valor_acelerado > 0):
            self._velocidade += valor_acelerado
        else:
            print('O valor a ser acelerado precisa ser maior que zero')

    def get_velocidade(self) -> float:
        return self._velocidade

class Passeio(Automovel):
    __lugares: int
    def __init__(self, placa, velocidade, lugares = 4):
        self.__lugares = lugares
        super(Passeio, self).__init__(placa, velocidade)

    def get_lugares(self) -> int:
        return self.__lugares

    def acelerar(self, valor_acelerado: float) -> None:
        if (valor_acelerado > 0):
            if(valor_acelerado <= 10):
                super()._velocidade += valor_acelerado
            else:
                print('Você não pode acelerar tão rápido!')
        else:
            print('O valor a ser acelerado precisa ser maior que zero')



carro = Automovel("XYX-0104", 70)
print('Placa:', carro.get_placa())
carro.dirigir()
carro.acelerar(20.5)
carro.dirigir()

print('--------------------------------')

mille = Passeio("zxc-0987", 120)
print('Placa:', mille.get_placa())
print(mille.get_lugares(), 'lugares')
mille.dirigir()
mille.acelerar(30)
mille.dirigir()
