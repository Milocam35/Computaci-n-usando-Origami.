import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from src.pleat import Pleat
from src.gadgets import NOTGadget, ANDGadget, ORGadget, NANDGadget

class TestGadgets(unittest.TestCase):
    
    def test_not_gate(self):
        """Tabla de verdad para NOT"""
        # Test cases: [(input, expected_output)]
        test_cases = [
            (True, False),
            (False, False),
            (None, None)
        ]
        
        for input_val, expected in test_cases:
            with self.subTest(input_val=input_val):
                in_pleat = Pleat("in")
                out_pleat = Pleat("out")
                
                in_pleat.set_value(input_val)
                not_gate = NOTGadget("NOT1", [in_pleat], [out_pleat])
                not_gate.evaluate()
                
                self.assertEqual(out_pleat.get_value(), expected)
    
    def test_and_gate(self):
        """Tabla de verdad para AND"""
        test_cases = [
            (False, False, False),
            (False, True, False),
            (True, False, False),
            (True, True, True),
            (None, True, None),
            (True, None, None)
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                in_a = Pleat("a")
                in_b = Pleat("b")
                out_pleat = Pleat("out")
                
                in_a.set_value(a)
                in_b.set_value(b)
                
                and_gate = ANDGadget("AND1", [in_a, in_b], [out_pleat])
                and_gate.evaluate()
                
                self.assertEqual(out_pleat.get_value(), expected)
    
    def test_or_gate(self):
        """Tabla de verdad para OR"""
        test_cases = [
            (False, False, False),
            (False, True, True),
            (True, False, True),
            (True, True, True),
            (None, True, None),
            (False, None, None)
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                in_a = Pleat("a")
                in_b = Pleat("b")
                out_pleat = Pleat("out")
                
                in_a.set_value(a)
                in_b.set_value(b)
                
                or_gate = ORGadget("OR1", [in_a, in_b], [out_pleat])
                or_gate.evaluate()
                
                self.assertEqual(out_pleat.get_value(), expected)
    
    def test_nand_gate(self):
        """Tabla de verdad para NAND"""
        test_cases = [
            (False, False, True),
            (False, True, True),
            (True, False, True),
            (True, True, False),
            (None, True, None),
            (True, None, None)
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                in_a = Pleat("a")
                in_b = Pleat("b")
                out_pleat = Pleat("out")
                
                in_a.set_value(a)
                in_b.set_value(b)
                
                nand_gate = NANDGadget("NAND1", [in_a, in_b], [out_pleat])
                nand_gate.evaluate()
                
                self.assertEqual(out_pleat.get_value(), expected)
