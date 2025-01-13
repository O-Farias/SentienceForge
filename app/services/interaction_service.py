from app.models.interaction import Interaction

def executar_interacao(ia, ambiente):
    """
    Executa a interação entre a IA e o ambiente.
    :param ia: Objeto da classe IA.
    :param ambiente: Objeto da classe Environment.
    """
    interacao = Interaction(ia, ambiente)
    interacao.simulate()
