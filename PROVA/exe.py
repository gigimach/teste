from prova import *


class ControledeSeguros:
    def __init__(self, total_valores=0, total_premio=0):
        self._total_valores = total_valores
        self._total_premio = total_premio
        self._seguros = []


    def cadastrarSeguros(self, seguro):
        self._seguros.append(seguro)
        print(f'O seguro foi cadastrado!')


    def relatorio(self):
        self._total_valores = 0
        seguro_auto = seguro_veiculo = 0
        for i in self._seguros:
            self._total_valores += i.calcularValor()
            self._total_premio += i.calcularPremio()
            if isinstance(i, SeguroAutomovel):
                seguro_auto += 1
            else:
                seguro_veiculo += 1
            print(i)
            print(10*'=')
        print(f"Seguro de Automóveis -> quantidade: {seguro_auto}\nSeguro de Vida --> quantidade: {seguro_veiculo}")


    @property
    def total_valores(self):
        return self._total_valores
    
    @property
    def total_premio(self):
        return self._total_premio


controle = ControledeSeguros()
Joao = Cliente('111.111.111-11','João',35)
Paulo = Cliente('222.222.222-22','Paulo', 49)
Luana = Cliente('333.333.333-33','Luana', 24)
controle.cadastrarSeguros(SeguroVida(1,Joao, Paulo))
controle.cadastrarSeguros(SeguroVida(2,Paulo, Luana))
controle.cadastrarSeguros(SeguroAutomovel(3, Paulo, 20, 'Onix', 2022, 50000))
controle.relatorio()
print(f"O Total dos Valores: R$ {controle._total_valores:.2f}")
print(f"O Total dos Premios: R$ {controle._total_premio:.2f}")