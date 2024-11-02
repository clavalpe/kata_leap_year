import pytest
from leap_year import LeapYearValidator


class TestLeapYearValidator:
    @pytest.mark.parametrize("year", [1997, 1995, 1991])
    def test_if_not_divisible_by_4_is_not_leap_year(self, year):
        assert LeapYearValidator().check(year) == False

    @pytest.mark.parametrize("year", [1996, 2004, 2024])
    def test_if_divisible_by_4_is_leap_year(self, year):
        assert LeapYearValidator().check(year) == True