import unittest
from convert import convert_time_to_text


class ConvertTest(unittest.TestCase):
    def test_convert_time_1(self):
        # GIVEN
        expected_time = 'Twenty nine to two'
        # WHEN
        output_time = convert_time_to_text('13:31')

        # THEN
        self.assertEqual(output_time, expected_time)

    def test_convert_time_2(self):
        # GIVEN
        expected_time = 'Half past one'
        # WHEN
        output_time = convert_time_to_text('13:30')

        # THEN
        self.assertEqual(output_time, expected_time)

    def test_convert_time_3(self):
        # GIVEN
        expected_time = 'Quarter to two'
        # WHEN
        output_time = convert_time_to_text('13:45')

        # THEN
        self.assertEqual(output_time, expected_time)

    def test_convert_time_4(self):
        # GIVEN
        expected_time = 'Quarter past one'
        # WHEN
        output_time = convert_time_to_text('13:15')

        # THEN
        self.assertEqual(output_time, expected_time)

    def test_convert_time_5(self):
        # GIVEN
        expected_time = "One o'clock"
        # WHEN
        output_time = convert_time_to_text('13:00')

        # THEN
        self.assertEqual(output_time, expected_time)

    def test_convert_time_6(self):
        # GIVEN
        expected_time = 'Time is not in a valid format'
        # WHEN
        output_time = convert_time_to_text('13r:ty')

        # THEN
        self.assertEqual(output_time, expected_time)

    def test_convert_time_7(self):
        # GIVEN
        expected_time = 'Time is not in a valid format'
        # WHEN
        output_time = convert_time_to_text('')

        # THEN
        self.assertEqual(output_time, expected_time)
