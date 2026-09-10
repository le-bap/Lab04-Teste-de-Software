def obter_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media > 5:
        return "Recuperacao"
    else:
        return "Reprovado"


def calcular_media(notas):
    if len(notas) == 0:
        raise ValueError("lista de notas vazia")
    return sum(notas) / len(notas)


def test_media_turma_a(notas_exemplo):
    assert calcular_media(notas_exemplo) == 7


def test_media_turma_b(notas_exemplo):
    media = calcular_media(notas_exemplo)
    assert obter_situacao(media) == "Aprovado"