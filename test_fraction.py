from fraction import Fraction

def test_fraction_equality():
    one_half = Fraction(1,2)
    other_half = Fraction(1,2)
    assert one_half == other_half

def test_fraction_normalization():
    one_half = Fraction(1,2)
    two_fourths = Fraction(2,4)
    assert one_half == two_fourths