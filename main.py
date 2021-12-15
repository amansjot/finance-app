import sqlite3 as db
import sys

def init(time: int):
    conn = db.connect("expenses.db")

    if time == 0:
        print("Hello! Welcome to your personal Finance Tracker.")
        print("-----")
        create_table(conn)

    print("R to record spendings/earnings, V to view spendings/earnings, or Q to quit")
    action = ""
    while action not in ["R", "V", "M", "Q"]:
        action = input("What action would you like to perform? ").upper()
    if action == "R":
        ans = ""
        while ans not in ["S", "E"]:
            ans = input("Spendings (S) or Earnings (E)? ").upper()
        if ans == "S":
            record_spending(conn)
        elif ans == "E":
            record_earning(conn)
    elif action == "V":
        view_finance(conn)
    elif action == "Q":
        print("QUITQ")
        sys.exit()

def create_table(conn):
    """
    Creates database tables to set up program
    :param conn: connection for databases
    :return: n/a (only creates table)
    """
    cursor = conn.cursor()
    sql_expenses = """
        CREATE table IF NOT EXISTS expenses (
            datestr string,
            expense string,
            amount number
        )
    """
    cursor.execute(sql_expenses)
    sql_earnings = """
            CREATE table IF NOT EXISTS earnings (
                datestr string,
                expense string,
                amount number
            )
        """
    cursor.execute(sql_earnings)
    conn.commit()

def to_dollar(amount: float):
    """
    Changes float to dollar currency format
    :param amount: amount in $ to convert
    :return: amount as a dollar value
    """
    dollar = '$' + str("{:,.2f}".format(amount))
    return dollar

def record_spending(conn):
    """
    A function for the user to input data about a spending
    :param conn: connection to the SQL database
    :return: n/a (prints success)
    """
    cursor = conn.cursor()

    print("-----")
    print("Record Spending")
    print("-----")

    spending = input("Date of spending: ")
    expense = input("Title of expense: ")
    amount = input("Amount: $")

    cursor.execute("insert into expenses values (?, ?, ?)", (spending, expense, amount))
    conn.commit()

    print("-----")
    print("Spending for '" + expense + "' added!")
    print("-----")

    init(1)

def record_earning(conn):
    """
    A function for the user to input data about an earning
    :param conn: connection to the SQL database
    :return: n/a (prints success)
    """
    cursor = conn.cursor()

    print("-----")
    print("Record Earning")
    print("-----")

    spending = input("Date of earning: ")
    earning = input("Title of earning: ")
    amount = input("Amount: $")

    cursor.execute("insert into earnings values (?, ?, ?)", (spending, earning, amount))
    conn.commit()

    print("-----")
    print("Earning for '" + earning + "' added!")
    print("-----")

    init(1)

def view_finance(conn):
    """
    A function for the user to see their total spending/earning
    :param conn: connection to the SQL database
    :return: n/a (prints spending data)
    """
    cursor = conn.cursor()

    print("-----")
    print("Your Spending")
    print("-----")

    cursor.execute("select * from expenses")
    data = cursor.fetchall()

    for expense in data:
        date = expense[0]
        title = expense[1]
        amount = to_dollar(expense[2])
        print(amount + " for " + title + " on " + date)

    total_spending = 0
    for expense in data:
        amount = expense[2]
        total_spending += amount

    print("-----")
    print("Your Earning")
    print("-----")

    cursor.execute("select * from earnings")
    data = cursor.fetchall()

    for earning in data:
        date = earning[0]
        title = earning[1]
        amount = to_dollar(earning[2])
        print(amount + " for " + title + " on " + date)

    print("-----")

    total_earning = 0
    for earning in data:
        amount = earning[2]
        total_earning += amount

    net = total_earning - total_spending

    total_spending = to_dollar(total_spending)
    total_earning = to_dollar(total_earning)
    print("Total Spending: " + total_spending)
    print("Total Earning: " + total_earning)

    print("Net: " + to_dollar(net))
    print("-----")

    init(1)


init(0)
