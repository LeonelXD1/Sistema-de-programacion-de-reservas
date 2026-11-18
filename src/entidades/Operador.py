class Operador:
    def __init__(self, estaAutorizado):
        self.estaAutorizado = estaAutorizado
        self.atm_asignado = None
        self.notificaciones = []

    def asignar_atm(self, atm):
        self.atm_asignado = atm
        atm.operador_asignado = self

    def recibir_alerta(self, alerta):
        self.notificaciones.append(alerta)