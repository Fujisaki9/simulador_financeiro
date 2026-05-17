from rich import print as rprint
from rich.console import Console
from rich.table import Table
from time import sleep


def validar_integer(pergunta: str) -> int:
    """
    Recebe uma string e garante que a resposta seja '1', '2' ou '3'.
        :param pergunta: String
    :return: O número escolhido convertido para inteiro.
    """
    console = Console()
    while True:
        string = console.input(pergunta).strip()
        if string in ('1', '2', '3'):
            valor = int(string)
            return valor
        else:
            rprint("[bold red]Comando inválido, digite novamente![/]")


def validar_float(pergunta: str) -> float:
    """
    Recebe uma string e garante que a resposta seja um número decimal (float)
    :param pergunta: String
    :return: O valor escolhido convertido em decimal (float)
    """
    console = Console()
    while True:
        try:
            string = console.input(pergunta).strip()
            valor = float(string)
            if valor <= 0:
                rprint("[bold red]Não é possível utilizar esse valor![/]")
            else:
                return valor
        except ValueError:
            rprint("[bold red]Erro: Digite um valor válido![/]")


def formatar_relatorio_final(dicionario: dict) -> dict:
    """
    :param dicionario: Dicionário com os dados coletados
    :return: Retorna um novo dicionário com as chaves e valores formatados
    """
    novo_dicionario = dict()
    for k, v in dicionario.items():
        nova_chave = k.title().replace('_', ' ')
        if k in ("rentabilidade_bruta", "rentabilidade_liquida", "aliquota_ir", "ganho_real"):
            novo_valor = f"{v:.2f} %"
        else:
            novo_valor = f"R$ {v:,.2f}".replace(',','x').replace('.',',').replace('x','.')
        novo_dicionario[nova_chave] = novo_valor
    return novo_dicionario


def inserir_dados_txt(dicionario: dict):
    """
    Pergunta ao usuário se deseja salvar os dados e coordena a exportação para TXT.
    :param dicionario: Dicionário contendo os dados processados da simulação.
    :return: Retorna um 'arquivo.txt' com o resultado da simulação ou apenas encerra o programa.
    """
    console = Console()
    while True:
        try:
            string = (console.input("[bold green]Deseja guardar os resultados da simulação em um arquivo.txt?: [S/N][/] ")
                        .strip().upper())
            if string in ("S", "N"):
                if string == "S":
                    exportar_relatorio_txt(formatar_relatorio_final(dicionario))
                    break
                else:
                    rprint("[bold green]Simulação finalizada![/]")
                    sleep(1)
                    rprint("[bold green]Programa encerrado![/]")
                    break
            else:
                rprint("[bold red]ERRO: Digite um comando válido![/]")
        except Exception as e:
            rprint("[bold red]Ocorreu um erro inesperado[/]")


def exportar_relatorio_txt(dicionario: dict):
    """
    Cria uma tabela utilizando os dados do dicionário e exporta para um arquivo.txt.
    :param dicionario: Dicionário contendo os resultados da simulação.
    """
    print()
    nome_arquivo = "relatorio.txt"
    console_export = Console(record = True, width = 100)

    table = Table(title="Relatório da Simulação")

    table.add_column("Descrição", style="dim")
    table.add_column("Valor", justify="right")
    table.add_section()
    table.add_row("Aporte Inicial", dicionario["Investimento"])
    table.add_row("Montante Bruto", dicionario["Montante Bruto"])
    table.add_row("Rentabilidade Bruta (%)", dicionario["Rentabilidade Bruta"])
    table.add_row("Lucro Bruto (sem descontos)", dicionario["Lucro Bruto"])
    table.add_section()
    table.add_row("Alíquota de IR (%)", dicionario["Aliquota Ir"])
    table.add_row("Valor do Desconto", dicionario["Valor Imposto"])
    table.add_section()
    table.add_row("Rentabilidade Líquida (%)", dicionario["Rentabilidade Liquida"])
    table.add_row("Lucro Líquido (com descontos)", dicionario["Rendimento Liquido"])
    table.add_section()
    table.add_row("Total para Saque (Montante Líquido)", dicionario["Montante Liquido"])
    table.add_row("Ganho Real (acima da inflação) (%)", dicionario["Ganho Real"])

    rprint("[bold green]Criando um arquivo.txt...[/]")
    sleep(1)
    rprint("[bold green]Adicionando o resultado da simulação...[/]")
    sleep(1)

    console_export.print(table)
    conteudo_tabela = console_export.export_text()

    with open(nome_arquivo, "a", encoding = "utf-8") as arquivo:
        arquivo.write(conteudo_tabela)
        arquivo.write("\n")

    sleep(1)
    rprint("[bold green]Informações adicionadas com sucesso![/]")
    sleep(1)
    rprint("[bold green]Programa encerrado![/]")

