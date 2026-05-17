from rich import print as rprint
from simulators import JurosSimples, JurosCompostos
from view import *
from services import *

mostrar_menu()
opcao = validar_integer("[bold green]Escolha uma opção:[/] ")
match opcao:
    case 1:
        while True:
            aporte_inicial = validar_float("[bold yellow]Aporte inicial: R$[/]  ")
            taxa_juros = validar_float("[bold yellow]Taxa de juros mensal (%):[/]  ")
            tempo_investimento = validar_float("[bold yellow]Tempo de investimento (meses):[/]  ")
            taxa_inflacao = validar_float("[bold yellow]Inflação no período (%):[/]  ")
            break

        # Cria o objeto Juros Simples
        juros_simples = JurosSimples(aporte_inicial, taxa_juros, tempo_investimento, taxa_inflacao)

        # Faz os cálculos e armazena-os dentro de um dicionário
        dicionario = juros_simples.coletar_dados_simulacao()

        # Mostra uma tabela com o resultado da simulação
        mostrar_relatorio_final(formatar_relatorio_final(dicionario))

        # Insere o resultado da simulação dentro de um arquivo.txt caso o usuário queira
        inserir_dados_txt(dicionario)


    case 2:
        while True:
            aporte_inicial = validar_float("[bold yellow]Aporte inicial: R$[/]  ")
            taxa_juros = validar_float("[bold yellow]Taxa de juros mensal (%):[/]  ")
            tempo_investimento = validar_float("[bold yellow]Tempo de investimento (meses):[/]  ")
            aporte_mensal = validar_float("[bold yellow]Aporte mensal: R$[/]  ")
            taxa_inflacao = validar_float("[bold yellow]Inflação no período (%):[/]  ")
            break

        # Cria o objeto Juros Compostos
        juros_compostos = JurosCompostos(aporte_inicial, taxa_juros, tempo_investimento, aporte_mensal, taxa_inflacao)

        # Faz os cálculos e armazena-os dentro de um dicionário
        dicionario = juros_compostos.coletar_dados_simulacao()

        # Mostra uma tabela com o resultado da simulação
        mostrar_relatorio_final(formatar_relatorio_final(dicionario))

        # Insere o resultado da simulação dentro de um arquivo.txt caso o usuário queira
        inserir_dados_txt(dicionario)

    case 3:
        rprint("[bold green]Programa encerrado![/]")