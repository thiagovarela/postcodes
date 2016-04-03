import re

from exceptions import InvalidPostCode


UK_PATTERN = (r'(([G][I][R] {0,}0[A]{2})|'
              '((([A-PR-UWYZ][A-HK-Y]?[0-9][0-9]?)|'
              '(([A-PR-UWYZ][0-9][A-HJKSTUW])|'
              '([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRV-Y]))) '
              '{0,}[0-9][ABD-HJLNP-UW-Z]{2}))$')
uk_pattern_compiled = re.compile(UK_PATTERN, re.IGNORECASE)


def validate(postcode, raise_exception=True):
    """Validates and formats a postcode against UK postcode pattern

        :type postcode: str
        :type raise_exception: bool
        :rtype: str | bool
        :raises TypeError: if the postcode is not a string
        :raises InvalidPostCode: if the postcode is invalid and the argument raise_exception is True

    """

    if not isinstance(postcode, str):
        raise TypeError
    if not uk_pattern_compiled.match(postcode):
        if raise_exception:
            raise InvalidPostCode
        else:
            return False
    else:
        postcode = postcode.upper().replace(' ', '')
        outward = postcode[:-3]
        inward = postcode[-3:]
        return '%s %s' % (outward, inward)
