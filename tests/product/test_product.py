from inventory_report.inventory.product import Product


productMock = {
    "id": 1,
    "nome_do_produto": "Lama",
    "nome_da_empresa": "Vale",
    "data_de_fabricacao": "01/06/2022",
    "data_de_validade": "01/06/2023",
    "numero_de_serie": "1234567",
    "instrucoes_de_armazenamento": "conservar longe de crianças do cão",
}


def test_cria_produto():

    """** espalha o conteudo do productMock na instancia de Product"""
    produc = Product(**productMock)

    assert produc.id == productMock["id"]
    assert produc.nome_do_produto == productMock["nome_do_produto"]
    assert produc.nome_da_empresa == productMock["nome_da_empresa"]
    assert produc.data_de_fabricacao == productMock["data_de_fabricacao"]
    assert produc.data_de_validade == productMock["data_de_validade"]
    assert produc.numero_de_serie == productMock["numero_de_serie"]
    assert (
        produc.instrucoes_de_armazenamento
        == productMock["instrucoes_de_armazenamento"]
    )
