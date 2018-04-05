# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    data_of_module = "hr/persons.csv"
    full_module_name = "Human resources manager"
    short_module_name = "hr/hr.py"
    common.create_module_menus(data_of_module, full_module_name, hr.short_module_name)

    # my_table = data_manager.get_table_from_file("hr/persons.csv")
    # menu = ["Show table", "Add to table", "Remove from table", "Update data"]

    # while True:
    #     ui.print_menu("Human resources manager", menu, "Exit this menu")
    #     inputs = ui.get_inputs(["Please enter a number: "], "")
    #     option = inputs[0]

    #     if option == "1":
    #         show_table(my_table)
    #     elif option == "2":
    #         add(my_table)
    #     elif option == "3":
    #         product_id = ui.get_inputs(["Which ID would you like to remove? "], "")
    #         remove(my_table, product_id)
    #     elif option == "4":
    #         product_id = ui.get_inputs(["Which ID would you like to update? "], "")
    #         update(my_table, product_id)
    #     elif option == "0":
    #         break
    #     else:
    #         raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID", "Name", "Date of birth"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    inputs = ui.get_inputs(["Name: ", "Date of birth: "], "")
    generated_id = common.generate_random(table)
    inputs.insert(0, generated_id)
    table.append(inputs)
    data_manager.write_table_to_file("hr/persons.csv", table)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    for index, row in enumerate(table):
        if id_[0] in row[0]:
            del table[index]
    data_manager.write_table_to_file("hr/persons.csv", table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    inputs = ui.get_inputs(["Name: ", "Date of birth: "], "")
    for index, row in enumerate(table):
        ids = row[0]
        if id_[0] in ids:
            inputs.insert(0, id_[0])
            del table[index]
            table.insert(index, inputs)
    data_manager.write_table_to_file("hr/persons.csv", table)
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
