
class IA:
    def __init__(self, name, capabilities):
        """
        Representa uma IA com nome e capacidades.
        :param name: Nome da IA.
        :param capabilities: Lista de capacidades (ex.: ["aprender", "explorar", "resolver problemas"]).
        """
        self.name = name
        self.capabilities = capabilities
        self.memory = []

    def add_memory(self, memory):
        """Adiciona uma memória à IA."""
        self.memory.append(memory)

    def __str__(self):
        return f"IA: {self.name} - Capacidades: {', '.join(self.capabilities)}"
