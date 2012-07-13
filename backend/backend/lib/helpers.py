"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password

import string
import random


def randomStr(charsCount, lowercase=False):
    if lowercase:
        chars = string.ascii_lowercase + string.digits
    else:
        chars = string.ascii_letters + string.digits
    result = ''
    for i in range(charsCount):
        result = result + random.choice(chars)
    return result