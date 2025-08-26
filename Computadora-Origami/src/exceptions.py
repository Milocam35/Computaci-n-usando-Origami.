class CyclicDependencyError(Exception):
    """Error cuando hay dependencias circulares en la red"""
    pass

class UndefinedSignalError(Exception):
    """Error cuando se encuentra una señal indefinida"""
    pass

class InvalidConnectionError(Exception):
    """Error cuando las conexiones de un gadget son inválidas"""
    pass