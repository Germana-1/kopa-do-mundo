from datetime import datetime


class NegativeTitlesError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "titles cannot be negative"


class FirstCupError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "there was no world cup this year"


class TitleNumberIsImpossibleError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "impossible to have more titles than disputed cups"


def validate_data(**kwargs: dict):
    first_cup = datetime.strptime(kwargs["first_cup"], "%Y-%m-%d")
    cup_year = (first_cup.year - 1930) % 4 == 0
    titles_possible = (datetime.now().year - first_cup.year) / 4

    if kwargs["titles"] < 0:
        raise NegativeTitlesError()

    if first_cup.year < 1930 or not cup_year:
        raise FirstCupError()

    if kwargs["titles"] > titles_possible:
        raise TitleNumberIsImpossibleError
