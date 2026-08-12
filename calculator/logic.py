"""
Core math for the "divide then multiply back" calculator.

The trick: floats (and even naive Decimal division) lose precision, so
100 / 3 * 3 == 99.99999999999999 in plain Python. To guarantee the
round trip always lands back on the exact original number, every
computation is done with fractions.Fraction, which stores numbers as
exact ratios (numerator/denominator) instead of approximations.

Only at the very end, when we need something to show on screen, do we
convert to a rounded decimal string.
"""
from decimal import Decimal
from fractions import Fraction


DISPLAY_DECIMAL_PLACES = 6


def to_fraction(value: Decimal) -> Fraction:
    """Convert a Decimal (from a form field) into an exact Fraction."""
    return Fraction(value)


def fraction_to_display_string(value: Fraction, places: int = DISPLAY_DECIMAL_PLACES) -> str:
    """
    Render a Fraction as a human-friendly decimal string, rounded to
    `places` decimal digits, with trailing zeros trimmed.
    This is for DISPLAY ONLY -- the underlying Fraction used in later
    calculations keeps full precision regardless of how it is shown.
    """
    quantum = Fraction(1, 10 ** places)
    rounded = (value / quantum).__round__() * quantum  # round-half-to-even on the fraction
    decimal_value = Decimal(rounded.numerator) / Decimal(rounded.denominator)
    text = format(decimal_value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text if text not in ("", "-") else "0"


def compute(dividend: Decimal, divisor: Decimal) -> dict:
    """
    Given dividend and divisor (both Decimal from the form), compute:
      - division_result: dividend / divisor, exact
      - multiplied_back: division_result * divisor, exact (== dividend)
    Returns display strings plus the raw Fractions for anyone who
    wants full precision.
    """
    dividend_f = to_fraction(dividend)
    divisor_f = to_fraction(divisor)

    division_result_f = dividend_f / divisor_f
    multiplied_back_f = division_result_f * divisor_f

    return {
        "dividend_display": fraction_to_display_string(dividend_f),
        "divisor_display": fraction_to_display_string(divisor_f),
        "division_result_exact": division_result_f,
        "division_result_display": fraction_to_display_string(division_result_f),
        "multiplied_back_exact": multiplied_back_f,
        "multiplied_back_display": fraction_to_display_string(multiplied_back_f),
        "round_trip_matches": multiplied_back_f == dividend_f,
    }
