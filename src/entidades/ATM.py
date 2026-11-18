class ATM:
    def __init__(self, atm_nombre, estaActivo):
        self.atm_nombre = atm_nombre
        self.estaActivo = estaActivo
        self.casilleros = {}
        self.casilleros_criticos = []
        self.operador_asignado = None

    def agregar_casillero(self, casillero):
        self.casilleros[casillero.denominacion] = casillero

    def establecer_cantidad_billetes(self, denominacion, cantidad_billetes):
        casillero = self.casilleros[denominacion]
        casillero.establecer_cantidad_billetes(cantidad_billetes)

    def verificar_capacidad(self):
        self.casilleros_criticos = []

        for casillero in self.casilleros.values():
            if casillero.esta_en_nivel_critico():
                self.casilleros_criticos.append(casillero)

        if self.casilleros_criticos:
            self.enviar_alerta_nivel_critico()

    def generar_mensaje_alerta(self) -> str:
        detalles_abastecimiento = []

        for indice, casillero in enumerate(self.casilleros_criticos):
            billetes_faltantes = casillero.calcular_billetes_faltantes()

            if indice == 0:
                detalle = (
                    f"{billetes_faltantes} billetes de "
                    f"{casillero.denominacion} dólares"
                )
            else:
                detalle = (
                    f"{billetes_faltantes} de "
                    f"{casillero.denominacion} dólares"
                )

            detalles_abastecimiento.append(detalle)

        return "Se requieren " + " y ".join(detalles_abastecimiento)

    def enviar_alerta_nivel_critico(self):
        if self.operador_asignado is not None:
            alerta = {
                "atm": self.atm_nombre,
                "nivel": "critico",
                "mensaje": self.generar_mensaje_alerta()
            }

            self.operador_asignado.recibir_alerta(alerta)