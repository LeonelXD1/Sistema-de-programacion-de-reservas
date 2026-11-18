class Casillero:
    def __init__(self, denominacion, capacidad_maxima, monto_minimo):
        self.denominacion = denominacion
        self.capacidad_maxima = capacidad_maxima
        self.monto_minimo = monto_minimo
        self.cantidad_actual = 0

    def establecer_cantidad_billetes(self, cantidad_billetes):
        self.cantidad_actual = cantidad_billetes

    def esta_en_nivel_critico(self) -> bool:
        return self.cantidad_actual < self.monto_minimo

    def calcular_billetes_faltantes(self) -> int:
        return self.capacidad_maxima - self.cantidad_actual