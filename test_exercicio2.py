import pytest

def validar_nota(nota):
    return 0 <= nota <= 10

def calcular_media(notas):
    if len(notas) == 0:
        raise ValueError("lista de notas vazia")
    return sum(notas) / len(notas)

def test_media_lista_vazia():
    with pytest.raises(ValueError, match="lista de notas vazia"):
        calcular_media([])