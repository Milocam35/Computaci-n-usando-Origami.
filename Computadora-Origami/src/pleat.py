class Pleat:
    """Representa un pliegue que transporta una señal booleana"""
    
    def __init__(self, name):
        self.name = name
        self.value = None  # True, False, o None (indefinido)
    
    def set_value(self, value):
        """Establece el valor del pleat"""
        if value is not None and not isinstance(value, bool):
            raise ValueError(f"El valor debe ser bool o None, recibido: {type(value)}")
        self.value = value
    
    def get_value(self):
        """Obtiene el valor del pleat"""
        return self.value
    
    def __str__(self):
        return f"Pleat({self.name}={self.value})"
    
    def __repr__(self):
        return self.__str__()