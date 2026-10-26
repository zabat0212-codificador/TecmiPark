# TecMi-Park — Sistema de Control de Estacionamiento

Proyecto desarrollado para la práctica de laboratorio de **Ciclo de Vida del Software** (Sesión práctica de 90 minutos). El sistema permite gestionar el flujo de entrada, cálculo de cobro por tiempo de estancia y control de aforo en tiempo real de un estacionamiento vehicular.

---

## 📌 Módulos Implementados

El sistema cubre los requerimientos técnicos de la **Opción A: Sistema de Estacionamiento**:

1. **Módulo 1: Registro de Ingreso de Vehículo**
   * Captura y validación de placa alfanumérica.
   * Registro de estampa de tiempo automática (`datetime.now()`).
   * Clasificación por tipo de vehículo (`auto`, `moto`, `camioneta`).
   * Prevención de duplicidad de placas en estancia activa.

2. **Módulo 2: Cálculo de Tarifa por Hora y Cobro**
   * Validación de salida mediante placa.
   * Cálculo de tiempo transcurrido (tarificación por fracción/hora completa base).
   * Matriz de tarifas diferenciadas según tipo de vehículo:
     * Motocicleta: $15.00 / hora
     * Automóvil: $25.00 / hora
     * Camioneta: $35.00 / hora
   * Desglose final de cobro y liberación automática de la plaza.

3. **Módulo 3: Disponibilidad de Lugares en Tiempo Real**
   * Control de cupo máximo configurable (Capacidad inicial: 10 vehículos).
   * Monitoreo dinámico de plazas ocupadas y libres.
   * Bloqueo preventivo de ingreso al alcanzar capacidad máxima.

---

## 🛠️ Estructura del Repositorio

```text
TecMi-Park-/
├── main.py              # Lógica principal del sistema y menú interactivo
├── requirements.txt     # Dependencias del entorno de ejecución
└── README.md            # Documentación del proyecto y guía de entrega
