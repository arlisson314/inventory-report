from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products_list):
        report = super().generate(products_list)

        empresas = [key["nome_da_empresa"] for key in products_list]

        estoque = Counter(empresas).most_common()

        report += "\nProdutos estocados por empresa:\n"

        for value in estoque:
            report += f"- {value[0]}: {value[1]}\n"

        return report
