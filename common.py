# implement commonly used functions here

import random
import ui
import data_manager
from store import store
# Human Resources module
from hr import hr
# Tool manager module
from inventory import inventory
# Accounting module
from accounting import accounting
# Sales module
from sales import sales
# Customer Relationship Management (CRM) module
from crm import crm


SOURCECODELOADER


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


def create_module_menus(file_name, full_module_name, short_module_name):
    my_table = data_manager.get_table_from_file(file_name)
    menu = ["Show table", "Add to table", "Remove from table", "Update data"]

    while True:
        ui.print_menu(full_module_name, menu, "Exit this menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]

        if option == "1":
            print(short_module_name)
            short_module_name.show_table(my_table)
        elif option == "2":
            hr.add(my_table)
        elif option == "3":
            product_id = ui.get_inputs(["Which ID would you like to remove? "], "")
            hr.remove(my_table, product_id)
        elif option == "4":
            product_id = ui.get_inputs(["Which ID would you like to update? "], "")
            hr.update(my_table, product_id)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
