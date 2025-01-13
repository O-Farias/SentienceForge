from app.models.interaction import Interaction

def simular_interacao(ia, ambiente):
    """
    Simula a interação entre a IA e o ambiente.
    Retorna os resultados da simulação.
    :param ia: Objeto da classe IA.
    :param ambiente: Objeto da classe Environment.
    :return: Dicionário com os resultados da simulação.
    """
    desafios = ambiente.challenges
    capacidades = ia.capabilities

    sucessos = 0
    falhas = 0

    for desafio in desafios:
        if desafio.strip().lower() in [cap.lower() for cap in capacidades]:
            sucessos += 1
        else:
            falhas += 1

    total_desafios = len(desafios)
    nota = (sucessos / total_desafios) * 10 if total_desafios > 0 else 0

    return {
        "sucessos": sucessos,
        "falhas": falhas,
        "nota": nota
    }
