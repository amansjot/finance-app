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
        action = input("What action would you like to perform? ")
    if action == "R":
        ans = ""
        while ans not in ["S", "E"]:
            ans = input("Spendings (S) or Earnings (E)? ")
        if ans == "S":
            record_spendings(conn)
        elif ans == "E":
            record_earnings()
    elif action == "V":
        view_spendings()
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
    cursor = conn.cursor()

    print("-----")
    print("Record Spending")
    print("-----")

    spending = input("Date of spending: ")
    expense = input("Title of expense: ")
    amount = input("Amount in $: ")

    cursor.execute("insert into expenses values (?, ?, ?)", (spending, expense, amount))
    conn.commit()

    print("-----")
    print("Spending for '" + expense + "' added!")
    print("-----")

    init(1)

def get_posts(conn):
    cursor = conn.cursor()
    cursor.execute("select * from expenses")
    print(cursor.fetchall())

init(0)
