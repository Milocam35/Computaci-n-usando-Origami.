from src.network import Network
from src.pleat import Pleat
from src.gadgets import ANDGadget, ORGadget, NOTGadget, NANDGadget

def ejemplo_basico():
    """Ejemplo básico: AND gate"""
    print("=== Ejemplo Básico: Compuerta AND ===")
    
    net = Network()
    
    # Crear pleats
    a = net.add_pleat("A")
    b = net.add_pleat("B")
    result = net.add_pleat("RESULT")
    
    # Crear gadget AND
    and_gate = ANDGadget("AND1", [a, b], [result])
    net.add_gadget(and_gate)
    
    # Test con diferentes entradas
    test_cases = [(False, False), (False, True), (True, False), (True, True)]
    
    for a_val, b_val in test_cases:
        net.set_inputs({"A": a_val, "B": b_val})
        net.run(log=False)
        output = net.get_outputs(["RESULT"])
        print(f"A={a_val}, B={b_val} -> RESULT={output['RESULT']}")

def ejemplo_half_adder():
    """Ejemplo del medio sumador"""
    print("\n=== Ejemplo: Medio Sumador (Half Adder) ===")
    
    def create_half_adder():
        net = Network()
        
        # Pleats de entrada
        a = net.add_pleat("A")
        b = net.add_pleat("B")
        
        # Pleats intermedios para XOR = (A OR B) AND NOT(A AND B)
        a_or_b = net.add_pleat("A_OR_B")
        a_and_b = net.add_pleat("A_AND_B")
        not_a_and_b = net.add_pleat("NOT_A_AND_B")
        
        # Pleats de salida
        sum_out = net.add_pleat("SUM")
        carry_out = net.add_pleat("CARRY")
        
        # Construir XOR usando OR, AND, NOT
        or_gate = ORGadget("OR1", [a, b], [a_or_b])
        and_gate1 = ANDGadget("AND1", [a, b], [a_and_b])
        not_gate = NOTGadget("NOT1", [a_and_b], [not_a_and_b])
        xor_and = ANDGadget("AND2", [a_or_b, not_a_and_b], [sum_out])
        
        # Carry = A AND B
        carry_and = ANDGadget("AND3", [a, b], [carry_out])
        
        # Añadir todos los gadgets
        net.add_gadget(or_gate)
        net.add_gadget(and_gate1)
        net.add_gadget(not_gate)
        net.add_gadget(xor_and)
        net.add_gadget(carry_and)
        
        return net
    
    # Test del medio sumador
    test_cases = [
        (False, False, "0 + 0 = 0"),
        (False, True, "0 + 1 = 1"),
        (True, False, "1 + 0 = 1"),
        (True, True, "1 + 1 = 10 (binario)")
    ]
    
    for a_val, b_val, description in test_cases:
        net = create_half_adder()
        net.set_inputs({"A": a_val, "B": b_val})
        net.run(log=False)
        
        outputs = net.get_outputs(["SUM", "CARRY"])
        print(f"{description}: SUM={outputs['SUM']}, CARRY={outputs['CARRY']}")

def ejemplo_con_log():
    """Ejemplo mostrando el log de ejecución"""
    print("\n=== Ejemplo con Log de Ejecución ===")
    
    net = Network()
    
    # Crear una pequeña red: NOT(A AND B) = NAND
    a = net.add_pleat("A")
    b = net.add_pleat("B")
    intermediate = net.add_pleat("INTERMEDIATE")
    result = net.add_pleat("RESULT")
    
    and_gate = ANDGadget("AND1", [a, b], [intermediate])
    not_gate = NOTGadget("NOT1", [intermediate], [result])
    
    net.add_gadget(and_gate)
    net.add_gadget(not_gate)
    
    # Establecer entradas y ejecutar con log
    net.set_inputs({"A": True, "B": True})
    net.run(log=True)
    
    print("\nLog de ejecución:")
    net.print_log()
    
    print(f"\nResultado final: {net.get_outputs(['RESULT'])}")

if __name__ == "__main__":
    ejemplo_basico()
    ejemplo_half_adder() 
    ejemplo_con_log()
    
    print("\n=== Ejecutando Tests ===")
    print("Para ejecutar todos los tests, usa: python -m unittest discover tests/")