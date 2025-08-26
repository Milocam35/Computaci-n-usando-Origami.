from abc import ABC, abstractmethod
from .exceptions import UndefinedSignalError, InvalidConnectionError

class Gadget(ABC):
    """Clase base abstracta para todos los gadgets (compuertas lógicas)"""
    
    def __init__(self, name, input_pleats, output_pleats):
        self.name = name
        self.input_pleats = input_pleats if input_pleats else []
        self.output_pleats = output_pleats if output_pleats else []
        self.validate_connections()
    
    @abstractmethod
    def validate_connections(self):
        """Valida que el número de entradas y salidas sea correcto"""
        pass
    
    @abstractmethod
    def evaluate(self):
        """Evalúa las entradas y calcula las salidas"""
        pass
    
    def get_input_values(self):
        """Obtiene los valores de todas las entradas"""
        return [pleat.get_value() for pleat in self.input_pleats]
    
    def has_undefined_inputs(self):
        """Verifica si alguna entrada es None"""
        return None in self.get_input_values()
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"

class NOTGadget(Gadget):
    """Compuerta NOT: 1 entrada, 1 salida"""
    
    def validate_connections(self):
        if len(self.input_pleats) != 1:
            raise InvalidConnectionError(f"NOT requiere 1 entrada, recibió {len(self.input_pleats)}")
        if len(self.output_pleats) != 1:
            raise InvalidConnectionError(f"NOT requiere 1 salida, recibió {len(self.output_pleats)}")
    
    def evaluate(self):
        input_val = self.input_pleats[0].get_value()
        
        if input_val is None:
            self.output_pleats[0].set_value(None)
        else:
            result = not input_val
            self.output_pleats[0].set_value(result)

class ANDGadget(Gadget):
    """Compuerta AND: 2 entradas, 1 salida"""
    
    def validate_connections(self):
        if len(self.input_pleats) != 2:
            raise InvalidConnectionError(f"AND requiere 2 entradas, recibió {len(self.input_pleats)}")
        if len(self.output_pleats) != 1:
            raise InvalidConnectionError(f"AND requiere 1 salida, recibió {len(self.output_pleats)}")
    
    def evaluate(self):
        a = self.input_pleats[0].get_value()
        b = self.input_pleats[1].get_value()
        
        if a is None or b is None:
            self.output_pleats[0].set_value(None)
        else:
            result = a and b
            self.output_pleats[0].set_value(result)

class ORGadget(Gadget):
    """Compuerta OR: 2 entradas, 1 salida"""
    
    def validate_connections(self):
        if len(self.input_pleats) != 2:
            raise InvalidConnectionError(f"OR requiere 2 entradas, recibió {len(self.input_pleats)}")
        if len(self.output_pleats) != 1:
            raise InvalidConnectionError(f"OR requiere 1 salida, recibió {len(self.output_pleats)}")
    
    def evaluate(self):
        a = self.input_pleats[0].get_value()
        b = self.input_pleats[1].get_value()
        
        if a is None or b is None:
            self.output_pleats[0].set_value(None)
        else:
            result = a or b
            self.output_pleats[0].set_value(result)

class NANDGadget(Gadget):
    """Compuerta NAND: 2 entradas, 1 salida"""
    
    def validate_connections(self):
        if len(self.input_pleats) != 2:
            raise InvalidConnectionError(f"NAND requiere 2 entradas, recibió {len(self.input_pleats)}")
        if len(self.output_pleats) != 1:
            raise InvalidConnectionError(f"NAND requiere 1 salida, recibió {len(self.output_pleats)}")
    
    def evaluate(self):
        a = self.input_pleats[0].get_value()
        b = self.input_pleats[1].get_value()
        
        if a is None or b is None:
            self.output_pleats[0].set_value(None)
        else:
            result = not (a and b)
            self.output_pleats[0].set_value(result)