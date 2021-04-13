from Objects import Pituxos

print('<'+'='*10+' Loja Pituxos - V1.0 '+'='*10+'>')

p = Pituxos()

class Executor:
    def __init__(self):
        print('\n<'+'='*10+' Menu Pituxos '+'='*10+'>')
        try:
            self.menu = int(input('\nInsira o valor que representa o que deseja fazer:\n\n\t1) Calcular valor do Pituxo;\n\t2) Alterar valor do rolo de tecido;\n\t3) Alterar valor da hora\n\t4) Consultar valores registrados;\n\t5) Sair do programa.\n\nValor: '))
        except ValueError:
            print('Insira um número.\n')
    
    def run(self):
        while True:
            if self.menu == 1:
                p.calculadora()
            elif self.menu == 2:
                p.altera_valor_rolo()
            elif self.menu == 3:
                p.altera_valor_hora()
            elif self.menu == 4:
                p.consulta_valores_registrados()
            elif self.menu == 5:
                break
            else:
                print('\nPor favor, insira uma opção válida.\n')

Executor().run()