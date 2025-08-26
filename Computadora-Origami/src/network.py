from collections import defaultdict, deque
from .exceptions import CyclicDependencyError, InvalidConnectionError
from .pleat import Pleat

class Network:
    """Red de gadgets y pleats interconectados (DAG)"""
    
    def __init__(self):
        self.gadgets = []
        self.pleats = {}  # nombre -> Pleat
        self.execution_log = []
    
    def add_pleat(self, name):
        """Añade un pleat a la red, segun el json de entrada"""
        if name in self.pleats:
            raise InvalidConnectionError(f"Pleat {name} ya existe")
        
        pleat = Pleat(name)
        self.pleats[name] = pleat
        return pleat
    
    def get_pleat(self, name):
        """Obtiene un pleat por nombre"""
        if name not in self.pleats:
            return self.add_pleat(name)
        return self.pleats[name]
    
    def add_gadget(self, gadget):
        """Añade un gadget a la red"""
        self.gadgets.append(gadget)
        
        # Asegurarse de que todos los pleats existen en la red
        all_pleats = gadget.input_pleats + gadget.output_pleats
        for pleat in all_pleats:
            if pleat.name not in self.pleats:
                self.pleats[pleat.name] = pleat
    
    def set_inputs(self, input_values):
        """Establece valores iniciales para pleats de entrada"""
        for name, value in input_values.items():
            if name not in self.pleats:
                raise InvalidConnectionError(f"Pleat {name} no existe")
            self.pleats[name].set_value(value)
    
    def get_outputs(self, output_names):
        """Obtiene valores de pleats de salida"""
        result = {}
        for name in output_names:
            if name not in self.pleats:
                raise InvalidConnectionError(f"Pleat {name} no existe")
            result[name] = self.pleats[name].get_value()
        return result
    
    def _build_dependency_graph(self):
        """Construye el grafo de dependencias gadget -> gadgets que dependen de él"""
        dependencies = defaultdict(set)
        in_degree = defaultdict(int)
        
        # Mapear pleats a gadgets que los producen/consumen
        pleat_producers = {}  # pleat_name -> gadget
        pleat_consumers = defaultdict(list)  # pleat_name -> [gadgets]
        
        for gadget in self.gadgets:
            in_degree[gadget] = 0  # Inicializar
            
            # Registrar qué gadget produce cada pleat de salida
            for out_pleat in gadget.output_pleats:
                if out_pleat.name in pleat_producers:
                    raise InvalidConnectionError(
                        f"Múltiples gadgets producen el pleat {out_pleat.name}"
                    )
                pleat_producers[out_pleat.name] = gadget
            
            # Registrar qué gadgets consumen cada pleat de entrada
            for in_pleat in gadget.input_pleats:
                pleat_consumers[in_pleat.name].append(gadget)
        
        # Construir dependencias: si gadget A produce un pleat que gadget B consume,
        # entonces B depende de A
        for pleat_name, producer in pleat_producers.items():
            for consumer in pleat_consumers[pleat_name]:
                if producer != consumer:  # No auto-dependencia
                    dependencies[producer].add(consumer)
                    in_degree[consumer] += 1
        
        return dependencies, in_degree
    
    def _topological_sort(self):
        """Ordena gadgets topológicamente para evitar dependencias"""
        dependencies, in_degree = self._build_dependency_graph()
        
        # Algoritmo de Kahn para ordenamiento topológico
        queue = deque()
        result = []
        
        # Empezar con gadgets que no tienen dependencias
        for gadget in self.gadgets:
            if in_degree[gadget] == 0:
                queue.append(gadget)
        
        while queue:
            current = queue.popleft()
            result.append(current)
            
            # Reducir grado de entrada de gadgets dependientes
            for dependent in dependencies[current]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
        
        # Verificar si hay ciclos
        if len(result) != len(self.gadgets):
            raise CyclicDependencyError("Se detectó un ciclo de dependencias en la red")
        
        return result
    
    def run(self, max_iterations=3, log=True):
        """Ejecuta la propagación de señales en la red"""
        if log:
            self.execution_log = []
        
        # Obtener orden topológico
        execution_order = self._topological_sort()
        
        if log:
            self.execution_log.append("=== Iniciando propagación ===")
            self.execution_log.append(f"Orden de ejecución: {[g.name for g in execution_order]}")
        
        # Ejecutar gadgets en orden topológico
        for iteration in range(max_iterations):
            if log:
                self.execution_log.append(f"\n--- Iteración {iteration + 1} ---")
            
            changed = False
            
            for gadget in execution_order:
                # Guardar estado anterior de salidas
                old_outputs = {p.name: p.get_value() for p in gadget.output_pleats}
                
                # Evaluar gadget
                gadget.evaluate()
                
                # Verificar si hubo cambios
                new_outputs = {p.name: p.get_value() for p in gadget.output_pleats}
                
                if old_outputs != new_outputs:
                    changed = True
                    if log:
                        self.execution_log.append(
                            f"  {gadget.name}: {old_outputs} -> {new_outputs}"
                        )
                elif log:
                    self.execution_log.append(f"  {gadget.name}: sin cambios")
            
            # Si no hubo cambios, la red se estabilizó
            if not changed:
                if log:
                    self.execution_log.append(f"\nRed estabilizada en iteración {iteration + 1}")
                break
        
        if log:
            self.execution_log.append("=== Propagación completada ===")
    
    def print_log(self):
        """Imprime el log de ejecución"""
        for line in self.execution_log:
            print(line)
    
    def get_all_pleat_values(self):
        """Obtiene todos los valores de pleats"""
        return {name: pleat.get_value() for name, pleat in self.pleats.items()}
