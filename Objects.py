import os.path, json

class Pituxos:
    def __init__(self):
        if os.path.isfile('dados.json'):
            print('\nCarregando os módulos...')
        else:
            self.cria_cache()

    def escreve_json(self, cache):
        with open('dados.json', 'w+') as arqv:
            json.dump(cache, arqv)
            #arqv.write(cache)

    def cria_cache(self):
        while True:
            try:
                custo = round(float(input('\nQual o custo do novelo?\nValor: R$ ').replace(',','.')))
                metragem = int(input('\nQual o tamanho do novelo? (Em metros)\nTamanho: '))
                valor_hora = float(input('\nQual o valor da sua hora de trabalho?\nTamanho: ').replace(',', '.'))
                cache = {'Custo': custo, "Metragem": metragem, "Hora": valor_hora}
                self.escreve_json(cache)
                break
            except ValueError:
                print('Insira um número válido.\n\nRestartando o módulo...\n')
                print(' '*500)
                continue

    def ler_cache(self):
        arqv = open('dados.json')
        valores = json.load(arqv)
        arqv.close()
        return valores

    def calcula_pituxo(self, tamanho_base, valor_base, tamanho_usado, valor_usado):
        pass

    def calculadora(self):
        while True:
            try:
                print('\n<'+'='*10+' Calculadora de Pituxos '+'='*10+'>')
                tempo = float(input('\nQuanto tempo você levou no projeto? (Em horas decimais. Ex. 8 horas e 35 minutos = 8,35)\nValor: ').replace(',', '.'))
                qtde = int(input('\nQuantas cores foram utilizadas?\nValor: '))
                retorno = self.ler_cache()
                projeto = {}
                for i in range(qtde):
                    cor = input(f'\nQual a {i+1}ª cor utilizada?\nCor: ').title()
                    fio = float(input(f'\nQuanto da cor {cor} foi utilizada? (Em centímetros)\nValor: ').replace('.', '').replace(',', '.'))/100
                    pituxo = lambda fio: (retorno['Custo']*fio)/retorno['Metragem']
                    projeto[cor] = round(pituxo(fio), 2)
                homem_hora = retorno['Hora'] * tempo
                print(f'\nO valor do pituxo é R$ {round((sum(projeto.values())*2) + homem_hora, 2)}')
                final = input('\nDeseja calcular outro Pituxo? (S/N)\nResposta: ').upper()
                if final == 'N':
                    break
                print(' '*500)
            except ValueError:
                print('Insira um número válido.\n\nRestartando o módulo...\n')
                print(' '*500)
                continue
        return

    def altera_valor_rolo(self):
        print('\n<'+'='*10+' Configurações da Pituxos '+'='*10+'>')
        custo = round(float(input('\nQual o NOVO custo de um rolo de tecido?\nValor: R$ ').replace(',','.')))
        retorno = self.ler_cache()
        retorno['Custo'] = custo
        self.escreve_json(retorno)
    
    def altera_valor_hora(self):
        print('\n<'+'='*10+' Configurações da Pituxos '+'='*10+'>')
        valor_hora = float(input('\nQual o NOVO valor da sua hora de trabalho?\nTamanho: ').replace(',', '.'))
        retorno = self.ler_cache()
        retorno['Hora'] = valor_hora
        self.escreve_json(retorno)

    def consulta_valores_registrados(self):
        print('\n<'+'='*10+' Configurações da Pituxos '+'='*10+'>\n')
        retorno = self.ler_cache()
        for i in retorno.items():
            print(f'O valor do(a) {i[0]} é {i[1]}')
