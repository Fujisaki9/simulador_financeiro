from abc import ABC, abstractmethod

class CalculosFinanceiros(ABC): # Classe abstrata
    """
    Base para simuladores financeiros. Processa inputs da interface e define métodos de cálculo.
    """
    def __init__(self, aporte_inicial, juros, tempo, inflacao):
        """
        Atributos de instância.
        :param aporte_inicial: Valor em dinheiro depositado no início.
        :param juros: Taxa de juros mensal em porcentagem (será convertido em decimal).
        :param tempo: Período de investimento em meses (int).
        :param inflacao: Taxa de inflação do período em porcentagem (será convertido em decimal).
        """
        self.aporte_inicial = aporte_inicial
        self.juros = juros / 100
        self.tempo = int(tempo)
        self.inflacao = inflacao / 100


    @abstractmethod
    def calcular_investimento(self) -> float:
        """
        Calcula o valor total do aporte inicial somado aos aportes mensais, se houver.
        :return: Valor total investido.
        """
        pass


    @abstractmethod
    def calcular_montante_bruto(self) -> float:
        """
        Calcula o valor total acumulado ao final do período, incluindo os juros.
        Deve ser implementado para aplicar a fórmula de juros correspondente (Simples ou Compostos) sobre o capital
        investido.
        :return: Montante final sem descontos de impostos.
        """
        pass


    def calcular_taxa_imposto_renda(self) -> float:
        """
        Determina a alíquota do Imposto de Renda com base no tempo de investimento.
        Segue a tabela regressiva padrão para investimentos de renda fixa:
        - Até 6 meses: 22,5%
        - De 6 a 12 meses: 20%
        - De 12 a 24 meses: 17,5%
        - Acima de 24 meses: 15%
        :return: Alíquota do imposto em formato decimal (ex: 0.15)
        """
        if self.tempo < 6:
            taxa_imposto_renda = 0.225
        elif 6 <= self.tempo < 12:
            taxa_imposto_renda = 0.20
        elif 12 <= self.tempo < 24:
            taxa_imposto_renda = 0.175
        else:
            taxa_imposto_renda = 0.15
        return taxa_imposto_renda


    def coletar_dados_simulacao(self) -> dict:
        """
        Efetua os cálculos necessários e insere-os dentro de um dicionário.
        :return: Retorna o dicionário com todos os dados coletados.
        """
        dicionario = dict()

        dicionario["investimento"]  = self.calcular_investimento()
        dicionario["montante_bruto"] = self.calcular_montante_bruto()
        dicionario["rendimento_bruto"] = dicionario["montante_bruto"] - dicionario["investimento"]
        dicionario["rentabilidade_bruta"] = (dicionario["rendimento_bruto"] / dicionario["investimento"] ) * 100
        dicionario["lucro_bruto"] = (dicionario["rentabilidade_bruta"] * dicionario["investimento"] ) / 100

        taxa_imposto_renda = self.calcular_taxa_imposto_renda()
        dicionario["aliquota_ir"] = taxa_imposto_renda * 100
        dicionario["valor_imposto"] = dicionario["rendimento_bruto"] * taxa_imposto_renda

        dicionario["rendimento_liquido"] =  dicionario["rendimento_bruto"] * (1 - taxa_imposto_renda)
        dicionario["rentabilidade_liquida"] = (dicionario["rendimento_liquido"] / dicionario["investimento"] ) * 100
        dicionario["montante_liquido"] = dicionario["rendimento_liquido"] + dicionario["investimento"]
        dicionario["ganho_real"] = ((1 + (dicionario["rentabilidade_liquida"] / 100)) /
                                    (1 + self.inflacao) - 1) * 100

        return dicionario

