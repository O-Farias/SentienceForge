class Interaction:
    def __init__(self, ia, environment):
        """
        Representa a interação entre uma IA e um ambiente.
        :param ia: Objeto da classe IA.
        :param environment: Objeto da classe Environment.
        """
        self.ia = ia
        self.environment = environment

    def simulate(self):
        """Simula a interação da IA com o ambiente."""
        for challenge in self.environment.challenges:
            if "resolver problemas" in self.ia.capabilities:
                self.ia.add_memory(f"Superou o desafio: {challenge}")
                print(f"✅ {self.ia.name} superou o desafio: {challenge}")
            else:
                print(f"⚠️ {self.ia.name} falhou no desafio: {challenge}")
