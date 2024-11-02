from leap_year import LeapYearValidator


class TestLeapYearValidator:
    def test_if_not_divisible_by_4_is_not_leap_year(self):
        assert LeapYearValidator().check(1997) == False