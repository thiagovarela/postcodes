import re

from postcodes.uk.exceptions import InvalidPostCode


UK_PATTERN = r'(([G][I][R] {0,}0[A]{2})|' \
             r'((([A-PR-UWYZ][A-HK-Y]?[0-9][0-9]?)|' \
             r'(([A-PR-UWYZ][0-9][A-HJKSTUW])|' \
             r'([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRV-Y]))) ' \
             r'{0,}[0-9][ABD-HJLNP-UW-Z]{2}))$'
uk_pattern = re.compile(UK_PATTERN, re.IGNORECASE)


def validate(postcode, raise_exception=True):
    """Validates a postcode against UK postcode pattern

        :type postcode: str
        :type raise_exception: bool
        :rtype: bool
        :raises TypeError: if the postcode is not a string
        :raises InvalidPostCode: if the postcode is invalid and the argument raise_exception is True

    """

    if not isinstance(postcode, str):
        raise TypeError
    if not uk_pattern.match(postcode):
        if raise_exception:
            raise InvalidPostCode
        else:
            return False
    else:
        return True