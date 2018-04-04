# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectations:
# - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """

    char1 = str(random.choice("kjtebv"))
    char3 = str(random.choice("931"))
    char4 = str(random.choice("458"))
    char6 = str(random.choice("abcdefghijklmnopqrstvwxyz"))
    id_tag = (char1, "H", char3, char4, "J", char6, "\u0023", "\u0026")
    return "".join(id_tag)

