import unittest

import uk
from uk.exceptions import InvalidPostCode


class TestUKPostCodes(unittest.TestCase):

    def test_should_raise_invalid_postcode(self):
        self.assertRaises(InvalidPostCode, uk.validate, 'XX10 Y###')
        self.assertRaises(InvalidPostCode, uk.validate, 'EC1A 1BBBBBBB')
        self.assertRaises(InvalidPostCode, uk.validate, 'EC1AX1BBBBBBB')
        self.assertRaises(InvalidPostCode, uk.validate, 'EC1AXBBBBBBB')
        self.assertRaises(TypeError, uk.validate, 123456)

    def test_should_return_false_invalid_postcode(self):
        self.assertFalse(uk.validate('XXX10 Y###', raise_exception=False))

    def test_should_validate_postcode(self):
        self.assertEquals(uk.validate('EC1A 1BB'), 'EC1A 1BB')
        self.assertEquals(uk.validate('ec1a1hq'), 'EC1A 1HQ')

    def test_should_raise_invalid_postcode_qvx_first_pos(self):
        self.assertRaises(InvalidPostCode, uk.validate, 'QC1A 1GB')
        self.assertRaises(InvalidPostCode, uk.validate, 'VY1 2AA')
        self.assertRaises(InvalidPostCode, uk.validate, 'XY1 1BP')

    def test_should_raise_invalid_postcode_ijz_second_pos(self):
        self.assertRaises(InvalidPostCode, uk.validate, 'EI1A 1BB')
        self.assertRaises(InvalidPostCode, uk.validate, 'SJ1 2AA')
        self.assertRaises(InvalidPostCode, uk.validate, 'SZ1 1BP')

    def test_should_raise_invalid_postcode_cikmov_final_letters(self):
        self.assertRaises(InvalidPostCode, uk.validate, 'SY1 1ZC')
        self.assertRaises(InvalidPostCode, uk.validate, 'SY1 1ZI')
        self.assertRaises(InvalidPostCode, uk.validate, 'SY1 1ZK')
        self.assertRaises(InvalidPostCode, uk.validate, 'N10AM')
        self.assertRaises(InvalidPostCode, uk.validate, 'N10AO')
        self.assertRaises(InvalidPostCode, uk.validate, 'N10AV')


if __name__ == '__main__':
    unittest.main()
