import behave.runner
from behave import *
from behave.matchers import use_step_matcher
from src.entidades.Operador import Operador
from src.entidades.ATM import ATM
from src.entidades.Casillero import Casillero


use_step_matcher("parse")

@step("un operador autorizado que tiene asignado el cajero {atm_nombre}, activo y conectado")
def step_impl(context: behave.runner.Context, atm_nombre: str):
    """
    :type context: behave.runner.Context
    :type atm_nombre: str
    """
    context.operador = Operador(estaAutorizado=True)
    context.atm = ATM(atm_nombre, estaActivo=True)

    context.operador.asignar_atm(context.atm)

    assert context.operador.atm_asignado == context.atm
    assert context.atm.operador_asignado == context.operador

@step("la capacidad de cada casillero es la siguiente:")
def step_impl(context: behave.runner.Context):
    """
    :type context: behave.runner.Context
    """
    for fila in context.table:
        denominacion = int(fila["denominacion"])
        capacidad_maxima = int(fila["capacidad_maxima"])
        monto_minimo = int(fila["monto_minimo"])

        casillero = Casillero(
            denominacion,
            capacidad_maxima,
            monto_minimo
        )

        context.atm.agregar_casillero(casillero)

        assert context.atm.casilleros[denominacion] == casillero


@step("actualmente cuenta con {cantidad_primera_denominacion:d} billetes de "
      "{primera_denominacion:d} dólares y "
      "{cantidad_segunda_denominacion:d} billetes de "
      "{segunda_denominacion:d} dólares")

def step_impl(context: behave.runner.Context,
              cantidad_primera_denominacion: int,
              primera_denominacion: int,
              cantidad_segunda_denominacion: int,
              segunda_denominacion: int):
    """
    :type context: behave.runner.Context
    :type cantidad_primera_denominacion: int
    :type primera_denominacion: int
    :type cantidad_segunda_denominacion: int
    :type segunda_denominacion: int
    """
    context.atm.establecer_cantidad_billetes(
        primera_denominacion, cantidad_primera_denominacion
    )

    context.atm.establecer_cantidad_billetes(
        segunda_denominacion, cantidad_segunda_denominacion
    )

    assert context.atm.casilleros[primera_denominacion].cantidad_actual == cantidad_primera_denominacion
    assert context.atm.casilleros[segunda_denominacion].cantidad_actual == cantidad_segunda_denominacion


@step("se verifica la capacidad actual")
def step_impl(context: behave.runner.Context):
    """
    :type context: behave.runner.Context
    """
    context.atm.verificar_capacidad()


@step("debe enviar la alerta de nivel crítico para el {atm_nombre} al operador asignado con el siguiente mensaje:")
def step_impl(context: behave.runner.Context, atm_nombre: str):
    """
    :type context: behave.runner.Context
    :type atm_nombre: str
    """
    mensaje_esperado = context.text.strip()

    assert len(context.operador.notificaciones) > 0

    alerta_recibida = context.operador.notificaciones[-1]

    assert alerta_recibida["atm"].lower() == atm_nombre.lower()
    assert alerta_recibida["nivel"] == "critico"
    assert alerta_recibida["mensaje"] == mensaje_esperado