from saludo_app.domain.entities import Saludo
from saludo_app.domain.ports import SaludarInputPort

class SaludarUseCase(SaludarInputPort):
    def ejecutar(self, nombre: str) -> str:
        saludo = Saludo(nombre=nombre)
        return saludo.generar_mensaje()