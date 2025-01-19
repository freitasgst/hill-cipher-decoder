import unittest
from decoder import message_setup, multiply_matrices, request_key, calculate_invertible, convert_message, convert_dec


class TestDecoder(unittest.TestCase):
    def test_request_key(self):
        result = request_key(3)
        self.assertEqual(len(result), 3)
        # assert todas as len(list) dentro do Vetor == parâmetro
        # assert all integers | float
    
    def test_calculate_invertible(self):
        result = calculate_invertible([[1, 0, 0], [1, 3, 1], [1, 2, 0]])
        self.assertEqual(result, [[1, 0, 0], [-0.5, 0, 0.5], [0.5, 1, -1.5]])
        m_identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(calculate_invertible(m_identity), m_identity)
    
    def test_request_message():
        # assert is str
        pass

    def test_convert_message(self):
        self.assertEqual(convert_message('a'), [97])
        self.assertEqual(convert_message('A'), [65])
        self.assertEqual(convert_message('SŢÕVŝØOƙóMŢÏEŰá'), [83, 354, 213, 86, 349, 216, 79, 409, 243, 77, 354, 207, 69, 368, 225])
    
    def test_message_setup(self):
        message = [83, 354, 213, 86, 349, 216, 79, 409, 243, 77, 354, 207, 69, 368, 225]
        order = 3
        result = message_setup(message, order)
        self.assertEqual(result, [[83, 354, 213], [86, 349, 216], [79, 409, 243], [77, 354, 207], [69, 368, 225]])
        self.assertEqual(len(result), len(message)/order)
        # assert parâmetros message % order == 0

    def test_multiply_matrices(self):
        invertible = [[1, 0, 0], [-0.5, 0, 0.5], [0.5, 1, -1.5]]
        message = [[83, 354, 213], [86, 349, 216], [79, 409, 243], [77, 354, 207], [69, 368, 225]]
        expected = [83, 65, 76, 86, 65, 68, 79, 82, 84, 77, 65, 82, 69, 78, 65]
        self.assertEqual(multiply_matrices(invertible, message), expected)

    def test_convert_dec(self):
        result = convert_dec([83, 65, 76, 86, 65, 68, 79, 82, 84, 77, 65, 82, 69, 78, 65])
        self.assertEqual(result, "SALVADORTMARENA")