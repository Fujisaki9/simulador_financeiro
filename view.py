from rich.console import Console
from rich.table import Table


def mostrar_menu():
    """
    Exibe o menu principal do simulador financeiro no console.
    """
    table = Table(header_style = "bold",
                  width = 24,
                  style = "blue")
    table.add_column("Simulador Financeiro", justify = "left")
    table.add_row("[bold][1] Juros Simples[/]")
    table.add_row("[bold][2] Juros Compostos[/]")
    table.add_row("[bold][3] Sair do programa[/]")
    console = Console()
    console.print(table)


def mostrar_relatorio_final(dicionario: dict):
    """
    Formata e exibe no console uma tabela detalhada com os resultados da simulação.
    Utiliza a biblioteca "rich".
    :param dicionario: Dicionário contendo os dados coletados da simulação.
    """
    print()
    table = Table(title = "[bold blue]Relatório Final - Simulação[/]",
                  style = "red")

    table.add_column("Descrição", style = "dim", width = 35)
    table.add_column("Valor", justify = "right")
    table.add_section()
    table.add_row("[bold bright_white]Aporte Inicial[/]", dicionario["Investimento"])
    table.add_row("[bold bright_white]Montante Bruto[/]", dicionario["Montante Bruto"])
    table.add_row("[bold bright_white]Rentabilidade Bruta (%)[/]", dicionario["Rentabilidade Bruta"])
    table.add_row("[bold bright_white]Lucro Bruto (sem descontos)[/]", dicionario["Lucro Bruto"])
    table.add_section()
    table.add_row("[bold bright_white]Alíquota de IR (%)[/]", dicionario["Aliquota Ir"])
    table.add_row("[bold bright_white]Valor do Desconto[/]", dicionario["Valor Imposto"])
    table.add_section()
    table.add_row("[bold bright_white]Rentabilidade Líquida (%)[/]", dicionario["Rentabilidade Liquida"])
    table.add_row("[bold bright_white]Lucro Líquido (com descontos)[/]", dicionario["Rendimento Liquido"])
    table.add_section()
    table.add_row("[bold bright_white]Total para Saque (Montante Líquido)[/]", dicionario["Montante Liquido"])
    table.add_row("[bold bright_white]Ganho Real (acima da inflação) (%)[/]", dicionario["Ganho Real"])
    console = Console()
    console.print(table)


