# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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

    while True:
        my_table = data_manager.get_table_from_file("accounting/items.csv")
        menu = ["Show table", "Add to table", "Remove from table", "Update data"]
        ui.print_menu("Accounting manager", menu, "Exit menu")
        
        inputs = ui.get_inputs(["Please choose a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(my_table)
        elif option == "2":
            add(my_table)
        elif option == "3":
            item_id = ui.get_inputs(["Which ID would you like to remove? "], "")
            remove(my_table, item_id)
        


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    datas = ["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "]
    generaged_id = common.generate_random(table)
    inputs = ui.get_inputs(datas, "")
    table.insert(0, generaged_id)
    table.append(inputs)
    data_manager.write_table_to_file("accounting/items.csv", table)
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

    # your code

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

    # your code

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
