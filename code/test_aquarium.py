import unittest
from code.aquarium import Aquarium
from mock import patch


def simple_water_change(gallons):
    if gallons > 60:
        return 'Splish splash'
    else:
        return 'A tall white fountain'


class TestCalls(unittest.TestCase):

    @patch('aquarium.Aquarium.water_change')
    def test_water_change_was_called_patched(self, spy):
        spy.water_change(70)
        spy.water_change.assert_called_with(70)

    def test_water_change_rejects_too_much_water(self):
        test_aquarium = Aquarium()
        self.assertRaises(OverflowError, lambda: test_aquarium.water_change(70))

    def test_water_change_accepts_enough_water(self):
        test_aquarium = Aquarium()
        self.assertEqual('Copacetic', test_aquarium.water_change(42))

    @patch('aquarium.Aquarium.water_change', side_effect=simple_water_change)
    def test_water_change_rejects_too_much_water_patched(self, mocky_mock):
        result = mocky_mock(70)
        self.assertEqual('Splish splash', result)

    def test_water_change_rejects_too_much_water_context(self):
        with patch('aquarium.Aquarium.water_change', side_effect=simple_water_change) as mocky_mock:
            result = mocky_mock(70)
        self.assertEqual('Splish splash', result)

    @patch('aquarium.Aquarium.water_change', side_effect=simple_water_change)
    def test_water_change_accepts_enough_water_patched(self, mocky_mock):
        result = mocky_mock(42)
        self.assertEqual('A tall white fountain', result)

    def test_water_change_accepts_enough_water_context(self):
        with patch('aquarium.Aquarium.water_change', side_effect=simple_water_change) as mocky_mock:
            result = mocky_mock(42)
        self.assertEqual('A tall white fountain', result)