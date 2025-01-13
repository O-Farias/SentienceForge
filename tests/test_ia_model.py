import pytest
from app.models.ia import IA

def test_create_ia():
    ia = IA(name="Mateus", capabilities=["Força", "Inteligência", "Resistência"])
    assert ia.name == "Mateus"
    assert ia.capabilities == ["Força", "Inteligência", "Resistência"]
    assert str(ia) == "IA: Mateus - Capacidades: Força, Inteligência, Resistência"
