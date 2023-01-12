from inventory_report.inventory.product import Product


# producMock = {
#     "id": 1,
#     "nome_do_produto": "Lama",
#     "nome_da_empresa": "vale",
#     "data_de_fabricacao": "01/06/2022",
#     "data_de_validade": "01/06/2023",
#     "numero_de_serie": "1234567",
#     "instrucoes_de_armazenamento": "conservar longe de crianças do cão",
# }


def test_cria_produto():

    produc = Product(
        1,
        "Lama",
        "Vale",
        "01/06/2022",
        "01/06/2023",
        "1234567",
        "conservar longe de crianças do cão",
    )

    assert produc.id == 1
    assert produc.nome_do_produto == "Lama"
    assert produc.nome_da_empresa == "Vale"
    assert produc.data_de_fabricacao == "01/06/2022"
    assert produc.data_de_validade == "01/06/2023"
    assert produc.numero_de_serie == "1234567"
    assert (
        produc.instrucoes_de_armazenamento
        == "conservar longe de crianças do cão"
    )
