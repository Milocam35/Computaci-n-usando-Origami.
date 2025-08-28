# Computación de Origami

## Descripción del Proyecto

Este proyecto implementa un modelo computacional basado en origami que demuestra la completitud de Turing a través de la abstracción de pliegues y gadgets. El sistema utiliza programación orientada a objetos en Python para modelar las estructuras y operaciones fundamentales del origami computacional.

## Conceptos Fundamentales

### Completitud de Turing en Origami

El origami ha sido demostrado como Turing completo, lo que significa que puede simular cualquier máquina de Turing y, por tanto, cualquier algoritmo computable. Este proyecto modela esta capacidad a través de:

- **Pleats (Pliegues)**: Estructuras básicas que representan las operaciones elementales
- **Gadgets**: Componentes más complejos construidos a partir de pleats que implementan operaciones lógicas
- **Network**: Red de gadgets interconectados que forma el sistema computacional completo

## Arquitectura del Sistema

### Estructura de Clases

El proyecto está organizado en tres clases principales:

1. **Pleat**: Clase base que representa un pliegue individual del origami
2. **Gadget**: Clase abstracta que define la interfaz para componentes computacionales
3. **Network**: Clase que maneja la red de gadgets y su interconexión

### Métodos Abstractos

El sistema utiliza métodos abstractos en la clase `Gadget` para garantizar que todas las implementaciones concretas proporcionen las funcionalidades necesarias para el cómputo.

### Algoritmo de Orden Topológico

Para el recorrido y evaluación de la red de gadgets, se implementa un algoritmo de ordenamiento topológico que asegura que las dependencias entre componentes se respeten durante la ejecución.

### Manejo de Errores

El sistema incluye excepciones personalizadas definidas en `exceptions.py` para manejar casos de error específicos del dominio del origami computacional.

## Estructura del Proyecto

```
Computadora-Origami/
├── src/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── exceptions.py      # Excepciones personalizadas
│   ├── gadgets.py        # Implementación de gadgets
│   ├── network.py        # Sistema de red de gadgets
│   └── pleat.py          # Clase base de pliegues
├── tests/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── test_gadgets.py   # Pruebas para gadgets
│   └── test_integration.py # Pruebas de half-adder
├── main.py               # Punto de entrada principal
└── README.md            # Este archivo
```

## Instalación

### Prerrequisitos

- Python 3.8 o superior
- pytest para ejecutar las pruebas

### Configuración del Entorno

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd Computadora-Origami
```

2. (Opcional) Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install pytest
```

## Uso del Sistema

### Ejecución Principal

Para ejecutar el programa principal:

```bash
python main.py
```

### Configuración de Entrada

Las entradas del sistema (pleats y gadgets para la network) están definidas mediante código hardcodeado en los archivos de prueba y en el archivo principal. Esto permite un control preciso sobre la configuración inicial del sistema.


## Pruebas

### Ejecutar Todas las Pruebas

```bash
pytest tests/
```

### Ejecutar Pruebas Específicas

```bash
# Pruebas de gadgets
pytest tests/test_gadgets.py

# Pruebas del half-adder
pytest tests/test_integration.py
```

## Grupo

Santiago Castellanos, Catalina Gutiérrez, Camilo Millan

---

