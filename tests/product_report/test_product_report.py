from inventory_report.inventory.product import Product

productMock = {
    "id": 1,
    "nome_do_produto": "Lama",
    "nome_da_empresa": "Vale",
    "data_de_fabricacao": "01/06/2022",
    "data_de_validade": "01/06/2023",
    "numero_de_serie": "1234567",
    "instrucoes_de_armazenamento": "longe de crianças do cão",
}


def test_relatorio_produto():
    produc = Product(**productMock)
    produc_data = str(produc)

    assert (isinstance(produc_data, str)) is True

    assert (produc_data) == (
        f"O produto {produc.nome_do_produto}"
        f" fabricado em {produc.data_de_fabricacao}"
        f" por {produc.nome_da_empresa} com validade"
        f" até {produc.data_de_validade}"
        f" precisa ser armazenado {produc.instrucoes_de_armazenamento}."
    )
