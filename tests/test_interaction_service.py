import pytest
from app.models.ia import IA
from app.models.environment import Environment
from app.services.interaction_service import simular_interacao

def test_simular_interacao():
    ia = IA(name="TesteIA", capabilities=["Força", "Resistência"])
    ambiente = Environment(description="Ambiente difícil", challenges=["Força", "Inteligência"])
    
    resultados = simular_interacao(ia, ambiente)
    assert resultados["sucessos"] == 1
    assert resultados["falhas"] == 1
    assert resultados["nota"] == 5.0
