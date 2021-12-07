import sqlite3 as db

def init():
    print("Hello! Welcome to your personal Finance Tracker.")
    conn = create_table()

    print("R to record spendings/earnings, V to view spendings/earnings, M to make recommendations")
    action = ""
    while action not in ["R", "T", "M"]:
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

def create_table():
    conn = db.connect("tracker.db")
    sql = """
        create table if not exists expenses (
            datestr string,
            expense string,
            amount number
        )
    """
    conn.cursor().execute(sql)
    # conn.commit()

    conn.cursor().execute("insert into expenses values ('07/01/2003', 'Movie Ticket', 10.00)")
    conn.commit()

    return conn

def record_spendings(conn):
    conn.cursor().execute("insert into expenses values ('07/01/2003', 'Movie Ticket', 10.00)")

init()