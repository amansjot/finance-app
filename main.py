import sqlite3 as db
import sys

def init(time: int):

    if time == 0:
        print("Hello! Welcome to your personal Finance Tracker.")
        conn = db.connect("expenses.db")
        create_table(conn)

    print("R to record spendings/earnings, V to view spendings/earnings, M to make recommendations, Q to quit")
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
        view_spending(conn)
    elif action == "M":
        make_rec()
    elif action == "Q":
        sys.exit()

    get_posts(conn)

def create_table(conn):
    cursor = conn.cursor()
    sql = """
        CREATE table IF NOT EXISTS expenses (
            datestr string,
            expense string,
            amount number
        )
    """
    cursor.execute(sql)
    conn.commit()

def record_spendings(conn):
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

def view_spending(conn):
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
        amount = '$' + str('{:,.2f}'.format(expense[2]))
        print(amount + " for " + title + " on " + date)

    print("-----")

    total = 0
    for expense in data:
        amount = expense[2]
        total += amount

    print("Total Spending: $" + str(total))
    print("-----")

    init(1)


def get_posts(conn):
    cursor = conn.cursor()
    cursor.execute("select * from expenses")
    print(cursor.fetchall())


init(0)
