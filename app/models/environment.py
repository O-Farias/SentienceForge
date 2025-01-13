class Environment:
    def __init__(self, description, challenges):
        """
        Representa o ambiente em que a IA opera.
        :param description: Descrição do ambiente.
        :param challenges: Lista de desafios que o ambiente apresenta.
        """
        self.description = description
        self.challenges = challenges

    def __str__(self):
        return f"Ambiente: {self.description} - Desafios: {', '.join(self.challenges)}"
