Feature: Abastecer de efectivo a un cajero automático

  Para mantener dinero disponible para los clientes
  Como trabajador autorizado del Banco Pacífico
  Quiero registrar la reposición de efectivo de un cajero automático hasta su capacidad máxima permitida

  Scenario: Abastecer correctamente un cajero
    Given que el trabajador está autorizado para abastecer cajeros
    And el cajero tiene capacidad disponible para recibir efectivo
    When el trabajador registra una reposición de efectivo válida
    Then el sistema confirma el abastecimiento
    And muestra el nuevo monto de efectivo disponible

  Scenario: Intentar abastecer más dinero del permitido
    Given que el trabajador está autorizado para abastecer cajeros
    And el cajero tiene una capacidad máxima establecida
    When el trabajador registra un monto superior a la capacidad disponible
    Then el sistema rechaza el abastecimiento
    And muestra un mensaje indicando el monto máximo permitido

  Scenario: Intentar abastecer sin autorización
    Given que la persona no está autorizada para abastecer cajeros
    When intenta registrar una reposición de efectivo
    Then el sistema rechaza la operación
    And muestra un mensaje indicando que no tiene autorización

  Scenario: Intentar registrar un monto inválido
    Given que el trabajador está autorizado para abastecer cajeros
    When registra un monto igual o menor a cero
    Then el sistema rechaza el abastecimiento
    And solicita ingresar un monto válido
