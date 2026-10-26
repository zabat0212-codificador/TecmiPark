import datetime

# Configuración del estacionamiento (Módulo 3)
CAPACIDAD_TOTAL = 10
TARIFAS = {
    "auto": 25.0,
    "moto": 15.0,
    "camioneta": 35.0
}

# Estructura de almacenamiento en memoria: {placa: {hora_ingreso, tipo}}
estacionamiento = {}

def mostrar_disponibilidad():
    """Módulo 3: Disponibilidad de Lugares en Tiempo Real"""
    ocupados = len(estacionamiento)
    libres = CAPACIDAD_TOTAL - ocupados
    print("\n--- ESTADO DEL ESTACIONAMIENTO ---")
    print(f"Capacidad total: {CAPACIDAD_TOTAL} | Ocupados: {ocupados} | Lugares disponibles: {libres}")
    return libres

def registrar_ingreso():
    """Módulo 1: Registro de Ingreso de Vehículo (Placa, Hora, Tipo)"""
    if len(estacionamiento) >= CAPACIDAD_TOTAL:
        print("\n[ERROR] Estacionamiento lleno. No se permiten más ingresos.")
        return

    print("\n--- REGISTRO DE INGRESO ---")
    placa = input("Ingrese la placa del vehículo: ").strip().upper()
    if placa in estacionamiento:
        print("[ERROR] Este vehículo ya se encuentra dentro.")
        return

    print(f"Tipos permitidos: {', '.join(TARIFAS.keys())}")
    tipo = input("Ingrese el tipo de vehículo: ").strip().lower()
    if tipo not in TARIFAS:
        print("[ERROR] Tipo de vehículo inválido.")
        return

    hora_ingreso = datetime.datetime.now()
    estacionamiento[placa] = {
        "hora_ingreso": hora_ingreso,
        "tipo": tipo
    }
    print(f"[ÉXITO] Vehículo {placa} ({tipo}) registrado a las {hora_ingreso.strftime('%H:%M:%S')}.")

def calcular_salida_y_cobro():
    """Módulo 2: Cálculo de Tarifa por Hora y Cobro"""
    print("\n--- SALIDA Y COBRO ---")
    placa = input("Ingrese la placa del vehículo que sale: ").strip().upper()
    if placa not in estacionamiento:
        print("[ERROR] La placa no se encuentra registrada.")
        return

    datos = estacionamiento.pop(placa)
    hora_ingreso = datos["hora_ingreso"]
    hora_salida = datetime.datetime.now()
    tipo = datos["tipo"]

    # Cálculo del tiempo (mínimo 1 hora base para la práctica)
    diferencia = hora_salida - hora_ingreso
    horas = max(1, int(diferencia.total_seconds() // 3600) + (1 if diferencia.total_seconds() % 3600 > 0 else 0))
    tarifa_base = TARIFAS[tipo]
    total_cobro = horas * tarifa_base

    print(f"\nResumen de Salida:")
    print(f"  Placa: {placa} | Tipo: {tipo}")
    print(f"  Hora de ingreso: {hora_ingreso.strftime('%H:%M:%S')}")
    print(f"  Hora de salida:  {hora_salida.strftime('%H:%M:%S')}")
    print(f"  Tiempo cobrado:  {horas} hora(s)")
    print(f"  Tarifa por hora: ${tarifa_base:.2f}")
    print(f"  TOTAL A PAGAR:   ${total_cobro:.2f}")

def main():
    while True:
        mostrar_disponibilidad()
        print("\n1. Registrar ingreso de vehículo (Módulo 1)")
        print("2. Cobro y salida de vehículo (Módulo 2)")
        print("3. Salir del sistema")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
   
