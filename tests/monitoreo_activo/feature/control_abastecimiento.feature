
# language: es

Característica: Control de abastecimiento de efectivo
  Como operador autorizado del Banco del Pacífico
  Quiero recibir notificaciones cuando la cantidad de billetes de una denominación sea inferior al mínimo establecido
  Para gestionar oportunamente el abastecimiento de los cajeros

#  Esquema del escenario: Notificar cuando falten billetes de una denominación
#    Dado que el cajero A tiene un mínimo establecido de <minimo> billetes de <denominacion>
#    Y el cajero A dispone de <disponibles> billetes de <denominacion>
#    Cuando el sistema verifica la cantidad de billetes disponibles
#    Entonces debe enviar una notificación al operador autorizado asignado
#    Y la notificación debe indicar la denominación de <denominacion> y la cantidad disponible

#    Ejemplos:
#      | denominacion | minimo | disponibles |
#      | $5           | 20     | 10          |
#      | $10          | 20     | 5           |
#      | $20          | 15     | 8           |



  Escenario: Notificar al operador cuando el efectivo del cajero cae por debajo del mínimo
    Dado un operador autorizado que tiene asignado el cajero ATM-A, activo y conectado
    Y la capacidad de cada casillero es la siguiente:
      | denominacion | capacidad_maxima | monto_minimo |
      | 20           | 40               | 10           |
      | 10           | 20               | 5            |
    Y actualmente cuenta con 8 billetes de 20 dólares y 2 billetes de 10 dólares
    Cuando se verifica la capacidad actual
    Entonces debe enviar la alerta de nivel crítico para el atm-a al operador asignado con el siguiente mensaje:
      """
      Se requieren 32 billetes de 20 dólares y 18 de 10 dólares
      """



#Cuando se verifica el monto entonces debe registrar una alerta de nivel critico para "ATM-A"
#Y Notificar a Juan en su bandeja de alertas
 # Y

 # Esquema del escenario: No notificar cuando la cantidad de billetes sea suficiente
  #  Dado que el cajero A tiene un mínimo establecido de <minimo> billetes de <denominacion>
   # Y el cajero A dispone de <disponibles> billetes de <denominacion>
   # Cuando el sistema verifica la cantidad de billetes disponibles
   # Entonces no debe generar una notificación de abastecimiento

    #Ejemplos:
    #  | denominacion | minimo | disponibles |
     # | $5           | 20     | 25          |
     # | $10          | 20     | 20          |
     # | $20          | 15     | 18          |
