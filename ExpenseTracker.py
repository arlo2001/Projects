# Arlo Theis
# Final Project: Expense Tracker/Planner program as described in project proposal

import statistics as stats
import matplotlib.pyplot as plt

def new_user(user_id):
    """Creates a file for a first time user"""
    # add user_id to master list
    with open('users.txt', 'a') as f:
        f.write(user_id)
        f.write('\n')
    # create new file for user
    print(f"Welcome {user_id}.")
    print("Please enter data for the first month you would like to record.")
    # obtain income, handling invalid inputs
    income = -1
    try:
        income = float(input("What was your total income during this month? "))
        while income < 0:
            income = float(input("Invalid entry. What was your total income during this month? "))
    except Exception:
        while income < 0:
            try:
                income = float(input("Invalid entry. What was your total income during this month? "))
            except Exception:
                pass
    # obtain spending, handling invalid inputs
    spending = -1
    try:
        spending = float(input("What was your total spending for this month? "))
        while spending < 0:
            spending = float(input("Invalid entry. What was your total spending for this month? "))
    except Exception:
        while spending < 0:
            try:
                spending = float(input("Invalid entry. What was your total spending for this month? "))
            except Exception:
                pass
    # write info to files to be retrieved in the future
    with open(f'{user_id}_income.txt', 'x') as f:
        f.write(str(income))
        f.write('\n')
    with open(f'{user_id}_spending.txt', 'x') as f:
        f.write(str(spending))
        f.write('\n')
    # Print confirmation
    print("Info recorded. Re-run the program to enter or view data.")


def get_info(user_id):
    """Obtains new data from an existing user"""
    # obtain income, handling invalid inputs
    income = -1
    try:
        income = float(input("What was your total income during this month? "))
        while income < 0:
            income = float(input("Invalid entry. What was your total income during this month? "))
    except Exception:
        while income < 0:
            try:
                income = float(input("Invalid entry. What was your total income during this month? "))
            except Exception:
                pass
    # obtain spending, handling invalid inputs
    spending = -1
    try:
        spending = float(input("What was your total spending for this month? "))
        while spending < 0:
            spending = float(input("Invalid entry. What was your total spending for this month? "))
    except Exception:
        while spending < 0:
            try:
                spending = float(input("Invalid entry. What was your total spending for this month? "))
            except Exception:
                pass
    with open(f'{user_id}_income.txt', 'a') as f:
        f.write(str(income))
        f.write('\n')
    with open(f'{user_id}_spending.txt', 'a') as f:
        f.write(str(spending))
        f.write('\n')
    # Print confirmation
    print("Info recorded. Re-run the program to enter or view data.")


def desc_stat(user_id):
    """Calculates and displays descrtiptive statistics"""
    print("--------------")
    # Read in income data
    with open(f"{user_id}_income.txt") as f:
        income = []
        for line in f:
            income.append(float(line.rstrip()))
    # Calculate and display stats for income
    print(f"Average income: {stats.mean(income):.2f}")
    print(f"Standard deviation of income: {stats.stdev(income):.2f}")
    # Read in spending data
    with open(f"{user_id}_spending.txt") as f:
        spending = []
        for line in f:
            spending.append(float(line.rstrip()))
    # Calculate and display stats for spending
    print(f"Average spending: {stats.mean(spending):.2f}")
    print(f"Standard deviation of spending: {stats.stdev(spending):.2f}")
    # Give number of months data is for
    print(f"*Stats above are calculated from the user's {len(spending)} months of data.")


def graph_data(user_id):
    """Graphs pre-existing user data"""
    # Ask which data to graph to graph
    print("Which dataset would you like to graph?")
    print("    1: Income")
    print("    2: Spending")
    # Get input, handling invalid entries
    choice = 0
    try:
        choice = int(input("Enter choice: "))
        while choice < 1 or choice > 2:
            choice = int(input("Invalid, please enter a valid choice from the menu: "))
    except Exception:
        while choice < 1 or choice > 2:
            try:
                choice = int(input("Invalid, please enter a valid choice from the menu: "))
            except Exception:
                pass
    # If income chosen
    if choice == 1:
        # Read in income data
        with open(f"{user_id}_income.txt") as f:
            income = []
            for line in f:
                income.append(float(line.rstrip()))
        # Graph data
        plt.plot(income, marker = 'o')
        plt.title("Income")
        plt.xlabel("Month")
        plt.ylabel("Income ($)")
        plt.show()
    # If spending chosen
    else:
        # Read in spending data
        with open(f"{user_id}_spending.txt") as f:
            spending = []
            for line in f:
                spending.append(float(line.rstrip()))
        # Graph data
        plt.plot(spending, marker = 'o')
        plt.title("Spending")
        plt.xlabel("Month")
        plt.ylabel("Spending ($)")
        plt.show()


def display_menu(user_id):
    """Displays a menu of options for an existing user and returns user's choice"""
    print(f"Welcome back {user_id}, what you like to do?")
    print("    1: Enter new monthly data")
    print("    2: View monthly spending statistics")
    print("    3: Graph income or spending trends")
    print("    4: Quit")
    # Request input, handling invalid entries
    choice = 0
    try:
        choice = int(input("Enter choice: "))
        while choice < 1 or choice > 4:
            choice = int(input("Invalid, please enter a valid choice from the menu: "))
    except Exception:
        while choice < 1 or choice > 4:
            try:
                choice = int(input("Invalid, please enter a valid choice from the menu: "))
            except Exception:
                pass
    return choice


def main():
    # Ask for user ID
    user_id = input("Welcome, enter your name: ")
    # check if new user from existing list
    try:
        with open('users.txt') as f:
            users = []
            for line in f:
                users.append(line.rstrip())
    # create user list if none found
    except FileNotFoundError:
        new_file = open('users.txt', 'x')
        new_file.close()
        users = []
    # if returning user:
    if user_id in users:
        # display menu and run requested function (or quit)
        choice = display_menu(user_id)
        # Enter new data
        if choice == 1:
            get_info(user_id)
        # Or view descriptive statistics
        elif choice == 2:
            desc_stat(user_id)
        # Or graph data
        elif choice == 3:
            graph_data(user_id)
        # Or quit
        else:
            quit
    # if new user:
    if user_id not in users:
        # offer option to create new user or quit
        print("User does not exist. Create new user with this name?")
        print("    1: Yes")
        print("    2: Quit")
        choice = 0
        try:
            choice = int(input("Enter choice: "))
            while choice < 1 or choice > 2:
                choice = int(input("Invalid, please enter a valid choice from the menu: "))
        except Exception:
            while choice < 1 or choice > 2:
                try:
                    choice = int(input("Invalid, please enter a valid choice from the menu: "))
                except Exception:
                    pass
        if choice == 1:
            # create new user
            new_user(user_id)
        else:
            quit


main()
