# 🏦 Simulador de Cajero Automático

¡Bienvenido a mi primer proyecto en Python! Este es un simulador interactivo de cajero automático que corre directamente en la consola. Lo diseñé para poner en práctica las bases de la lógica de programación y el control de flujos.

## 🚀 Características

A través de un menú interactivo continuo, el programa te permite realizar las siguientes acciones:
1. **Consultar saldo:** Muestra de forma dinámica el dinero actual disponible en la cuenta.
2. **Depositar dinero:** Permite ingresar un monto entero y lo suma automáticamente al saldo total.
3. **Retirar dinero:** Incluye un sistema de seguridad que valida si tienes fondos suficientes antes de hacer la transacción. Si el monto es válido, lo resta del saldo; si no, arroja un mensaje de error.
4. **Salir:** Despide al usuario y rompe el ciclo del programa de forma limpia.
5. **Validación de opciones:** Cuenta con un sistema por defecto que detecta si ingresas un número inválido en el menú.

## 🛠️ Tecnologías utilizadas

* **Lenguaje:** Python 3
* **Conceptos clave:** Bucles infinitos (`while True`), condicionales anidados (`if`, `elif`, `else`), variables de estado, operadores de asignación compuesta (`+=`, `-=`) y conversión de tipos de datos (`int`).

## 💻 Cómo ejecutar el proyecto

1. Asegúrate de tener instalado **Python**.
2. Descarga el archivo `main.py`.
3. Abre tu terminal o consola en la carpeta del archivo y ejecuta:
   ```bash
   python main.py
   ```
