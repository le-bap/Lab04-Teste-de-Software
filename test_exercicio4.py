import pytest
def obter_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperacao"
    else:
        return "Reprovado"

@pytest.mark.parametrize("media, esperado", [
    (10, "Aprovado"),
    (8, "Aprovado"),
    (7, "Aprovado"),
    (6, "Recuperacao"),
    (5, "Recuperacao"),
    (4, "Reprovado"),
])
def test_obter_situacao(media, esperado):
    assert obter_situacao(media) == esperado