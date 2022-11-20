from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class UnicodeMobileNumberValidator(validators.RegexValidator):
    regex = r'09(\d{9})$'
    message = 'Enter a valid mobile number. This value may contain only numbers.'
    flags = 0
