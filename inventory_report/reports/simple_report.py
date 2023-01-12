from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products_list):
        data_de_fabricacao = [
            key["data_de_fabricacao"] for key in products_list
        ]

        data_de_validade = [key["data_de_validade"] for key in products_list]

        empresas = [key["nome_da_empresa"] for key in products_list]
        nome_da_empresa = Counter(empresas).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {min(data_de_fabricacao)}\n"
            f"Data de validade mais próxima: {min(data_de_validade)}\n"
            f"Empresa com mais produtos: {nome_da_empresa}"
        )
