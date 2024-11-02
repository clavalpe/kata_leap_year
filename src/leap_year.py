class LeapYearValidator:
    def check(self, year: int) ->  bool:
        return  year % 4 == 0