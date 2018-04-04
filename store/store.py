# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

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
        my_table = data_manager.get_table_from_file("store/games.csv")
        menu = ["Show table", "Add to table", "Remove from table", "Update data", "How Many Manufacturer"]
        ui.print_menu("Store Manager", menu, "Exit this menu")

        inputs = ui.get_inputs(["Please choose a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(my_table)
        elif option == "2":
            add(my_table)
        elif option == "3":
            product_id = ui.get_inputs(["Which ID would you like to remove? "], "")
            remove(my_table, product_id)
        elif option == "4":
            product_id = ui.get_inputs(["Which ID would you like to update? "], "")
            update(my_table, product_id)
        elif option == "5":
            get_counts_by_manufacturers(my_table)
        elif option == "0":
            break


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["ID", "Game Title", "Manufacturer", "Price", "In Stock"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    game_details = ["Game Title: ", "Manufacturer: ", "Price: ", "In Stock: "]
    generaged_id = common.generate_random(table)
    inputs = ui.get_inputs(game_details, "")
    inputs.insert(0, generaged_id)
    table.append(inputs)
    data_manager.write_table_to_file("store/games.csv", table)
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
            table.pop(index)
    data_manager.write_table_to_file("store/games.csv", table)
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

    inputs = ui.get_inputs(["Game Title: ", "Manufacturer: ", "Price: ", "In Stock: "], "")
    for index, row in enumerate(table):
        ids = row[0]
        if id_[0] in ids:
            inputs.insert(0, id_[0])
            table.pop(index)
            table.insert(index, inputs)
    data_manager.write_table_to_file("store/games.csv", table)
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    table = data_manager.get_table_from_file(table)
    for row in table:
        all_manufacturers = row[2]
        kind_of_games = {manufacturer: all_manufacturers.count(manufacturer) for manufacturer in all_manufacturers}
    return kind_of_games


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
