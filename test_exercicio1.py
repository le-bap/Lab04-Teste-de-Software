def validar_nota(nota):
    return 0 <= nota <= 10


def calcular_media(notas):
    return sum(notas) / len(notas)


def test_nota_zero():
    assert validar_nota(0) is True


def test_nota_dez():
    assert validar_nota(10) is True


def test_nota_negativa():
    assert validar_nota(-1) is False


def test_nota_maior_que_dez():
    assert validar_nota(11) is False


def test_nota_dentro_do_intervalo():
    assert validar_nota(7) is True


def test_calcular_media():
    assert calcular_media([6, 7, 8]) == 7