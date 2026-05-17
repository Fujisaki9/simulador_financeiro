from base import CalculosFinanceiros

class JurosSimples(CalculosFinanceiros):    # Subclasse
    """
    Simulador de investimentos baseado no regime de juros simples.
    """
    def __init__(self, aporte_inicial, juros, tempo, inflacao):
        """
        Atributos de instância.
        :param aporte_inicial: Valor em dinheiro depositado no início.
        :param juros: Taxa de juros mensal em porcentagem (será convertido em decimal).
        :param tempo: Período de investimento em meses (int).
        :param inflacao: Taxa de inflação do período em porcentagem (será convertido em decimal).
        """
        super().__init__(aporte_inicial, juros, tempo, inflacao)


    def calcular_investimento(self) -> float:
        """
        Retorna o capital inicial investido na simulação.
        :return: O valor do aporte inicial.
        """
        return self.aporte_inicial


    def calcular_montante_bruto(self) -> float:
        """
        Calcula o montante final utilizando a fórmula de juros simples.
        Fórmula: M = C * (1 + i * t).
        :return: Montante final sem descontos.
        """
        return self.aporte_inicial * (1 + self.juros * self.tempo)


class JurosCompostos(CalculosFinanceiros):  # Subclasse
    """
    Simulador de investimentos baseado no regime de juros compostos.
    """

    def __init__(self,aporte_inicial, juros, tempo, aporte_mensal, inflacao):
        """
        Atributos de instância.
        :param aporte_inicial: Valor em dinheiro depositado no início.
        :param juros: Taxa de juros mensal em porcentagem (será convertido em decimal).
        :param tempo: Período de investimento em meses (int).
        :param aporte_mensal: Valor depositado mensalmente (float)
        :param inflacao: Taxa de inflação do período em porcentagem (será convertido em decimal).
        """
        super().__init__(aporte_inicial, juros, tempo, inflacao)
        self.aporte_mensal = aporte_mensal


    def calcular_investimento(self) -> float:
        """
        Calcula o investimento somando o aporte inicial aos aportes mensais corrigidos pelo tempo.
        :return: Valor total do investimento.
        """
        return self.aporte_inicial + (self.aporte_mensal * self.tempo)


    def calcular_montante_bruto(self) -> float:
        """
        Calcula o montante acumulado utilizando a lógica de juros compostos mensais.
        Fórmula: M = C * (1 + i) ^ t.
        :return: Montante final sem descontos.
        """
        montante = self.aporte_inicial
        for i in range(1, self.tempo + 1):
            rendimento_mensal = montante * self.juros
            montante += rendimento_mensal + self.aporte_mensal
        return montante

