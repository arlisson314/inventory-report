from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():

    list_mock = [
        {
            "id": "1",
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 1",
        }
    ]

    data_antiga = "Data de fabricação mais antiga:"
    data_validade = "Data de validade mais próxima:"
    empresa = "Empresa com mais produtos:"
    data_a = "2021-02-18"
    data_v = "2023-09-17"
    emp = "Target Corporation"

    report = ColoredReport(SimpleReport).generate(list_mock)

    assert f"\033[32m{data_antiga}\033[0m \033[36m{data_a}\033[0m" in report
    assert f"\033[32m{data_validade}\033[0m \033[36m{data_v}\033[0m" in report
    assert f"\033[32m{empresa}\033[0m \033[31m{emp}\033[0m" in report
