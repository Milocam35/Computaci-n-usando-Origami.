import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.network import Network
from src.pleat import Pleat
from src.gadgets import ANDGadget, ORGadget, NOTGadget

class TestIntegration(unittest.TestCase):
    
    def create_half_adder(self):
        """Crea un medio sumador usando gadgets básicos
        Half Adder:
        - Sum = A XOR B = (A OR B) AND NOT(A AND B)
        - Carry = A AND B
        """
        net = Network()
        
        # Pleats de entrada
        a = net.add_pleat("A")
        b = net.add_pleat("B")
        
        # Pleats intermedios
        a_or_b = net.add_pleat("A_OR_B")
        a_and_b = net.add_pleat("A_AND_B")
        not_a_and_b = net.add_pleat("NOT_A_AND_B")
        
        # Pleats de salida
        sum_out = net.add_pleat("SUM")
        carry_out = net.add_pleat("CARRY")
        
        # Gadgets
        or_gate = ORGadget("OR1", [a, b], [a_or_b])
        and_gate1 = ANDGadget("AND1", [a, b], [a_and_b])
        not_gate = NOTGadget("NOT1", [a_and_b], [not_a_and_b])
        and_gate2 = ANDGadget("AND2", [a_or_b, not_a_and_b], [sum_out])
        and_gate3 = ANDGadget("AND3", [a, b], [carry_out])  # Carry = A AND B

        """- Sum = A XOR B = (A OR B) AND NOT(A AND B)
        - Carry = A AND B"""
        
        # Añadir gadgets a la red
        net.add_gadget(or_gate)
        net.add_gadget(and_gate1)
        net.add_gadget(not_gate)
        net.add_gadget(and_gate2)
        net.add_gadget(and_gate3)
        
        return net
    
    def test_half_adder(self):
        """Test completo del medio sumador con las 4 combinaciones"""
        test_cases = [
            # (A, B, expected_sum, expected_carry)
            (False, False, False, False),  # 0 + 0 = 0, carry 0
            (False, True, True, False),    # 0 + 1 = 1, carry 0
            (True, False, True, False),    # 1 + 0 = 1, carry 0
            (True, True, False, True),     # 1 + 1 = 0, carry 1
        ]
        
        for a_val, b_val, expected_sum, expected_carry in test_cases:
            with self.subTest(A=a_val, B=b_val):
                net = self.create_half_adder()
                
                # Establecer entradas
                net.set_inputs({"A": a_val, "B": b_val})
                
                # Ejecutar red
                net.run(log=False)
                
                # Verificar salidas
                outputs = net.get_outputs(["SUM", "CARRY"])
                
                self.assertEqual(outputs["SUM"], expected_sum, 
                    f"Sum incorrecto para A={a_val}, B={b_val}")
                self.assertEqual(outputs["CARRY"], expected_carry,
                    f"Carry incorrecto para A={a_val}, B={b_val}")