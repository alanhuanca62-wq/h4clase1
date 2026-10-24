from dataclasses import dataclass

@dataclass(frozen=True)
class Saludo:
    nombre: str

    def generar_mensaje(self) -> str:
        nombre_limpio = self.nombre.strip()
        if not nombre_limpio:
            raise ValueError("El nombre es obligatorio y no puede estar vacío.")
        return f"Hola {nombre_limpio}"