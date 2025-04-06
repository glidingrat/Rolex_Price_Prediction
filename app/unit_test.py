import unittest
from .models import predict_price

class TestPredictPrice(unittest.TestCase):

    def test_invalid_size_type(self):
        with self.assertRaises(ValueError) as context:
            predict_price(
                size="forty",  # Neplatný hodnota
                material="Gold",
                bezel="Fluted",
                bracelet="Oyster",
                dial="Black",
                papers="Yes"
            )
        self.assertEqual(str(context.exception), "Neplatná hodnota pro Size: forty")

    def test_invalid_material_type(self):
        with self.assertRaises(ValueError) as context:
            predict_price(
                size="36",
                material=123,  # Neplatný typ
                bezel="Fluted",
                bracelet="Oyster",
                dial="Black",
                papers="Yes"
            )
        self.assertEqual(str(context.exception), "Material musí být typu str, zadaná hodnota: 123")

    def test_invalid_material_value(self):
        with self.assertRaises(ValueError) as context:
            predict_price(
                size="36",
                material="Plastic",  # Neplatná hodnota
                bezel="Fluted",
                bracelet="Oyster",
                dial="Black",
                papers="Yes"
            )
        self.assertEqual(str(context.exception), "Neplatná hodnota pro Material: Plastic")

    def test_invalid_bezel_type(self):
        with self.assertRaises(ValueError) as context:
            predict_price(
                size="36",
                material="Gold",
                bezel=5,  # Neplatný typ
                bracelet="Oyster",
                dial="Black",
                papers="Yes"
            )
        self.assertEqual(str(context.exception), "Bezel musí být typu str, zadaná hodnota: 5")

    def test_invalid_bezel_value(self):
        with self.assertRaises(ValueError) as context:
            predict_price(
                size="36",
                material="Gold",
                bezel="Round",  # Neplatná hodnota
                bracelet="Oyster",
                dial="Black",
                papers="Yes"
            )
        self.assertEqual(str(context.exception), "Neplatná hodnota pro Bezel: Round")

    def test_invalid_bracelet_type(self):
        with self.assertRaises(ValueError) as context:
            predict_price(
                size="36",
                material="Gold",
                bezel="Fluted",
                bracelet=100,  # Neplatný typ
                dial="Black",
                papers="Yes"
            )
        self.assertEqual(str(context.exception), "Bracelet musí být typu str, zadaná hodnota: 100")

    def test_invalid_bracelet_value(self):
        with self.assertRaises(ValueError) as context:
            predict_price(
                size="36",
                material="Gold",
                bezel="Fluted",
                bracelet="Leather",  # Neplatná hodnota
                dial="Black",
                papers="Yes"
            )
        self.assertEqual(str(context.exception), "Neplatná hodnota pro Bracelet: Leather")

    def test_invalid_dial_type(self):
        with self.assertRaises(ValueError) as context:
            predict_price(
                size="36",
                material="Gold",
                bezel="Fluted",
                bracelet="Oyster",
                dial=123,  # Neplatný typ
                papers="Yes"
            )
        self.assertEqual(str(context.exception), "Dial musí být typu str, zadaná hodnota: 123")

    def test_invalid_dial_value(self):
        with self.assertRaises(ValueError) as context:
            predict_price(
                size="36",
                material="Gold",
                bezel="Fluted",
                bracelet="Oyster",
                dial="Purple",  # Neplatná hodnota
                papers="Yes"
            )
        self.assertEqual(str(context.exception), "Neplatná hodnota pro Dial: Purple")

    def test_invalid_papers_type(self):
        with self.assertRaises(ValueError) as context:
            predict_price(
                size="36",
                material="Gold",
                bezel="Fluted",
                bracelet="Oyster",
                dial="Black",
                papers=1  # Neplatný typ
            )
        self.assertEqual(str(context.exception), "Papers musí být typu str, zadaná hodnota: 1")

    def test_invalid_papers_value(self):
        with self.assertRaises(ValueError) as context:
            predict_price(
                size="36",
                material="Gold",
                bezel="Fluted",
                bracelet="Oyster",
                dial="Black",
                papers="Maybe"  # Neplatná hodnota
            )
        self.assertEqual(str(context.exception), "Neplatná hodnota pro Papers: Maybe")
