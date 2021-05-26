#Production by Berlin
#Telegram - @por0vos1k


# - *- coding: utf- 8 - *-
import sqlite3

def ensure_connection(func):

    def decorator(*args, **kwargs):
        with sqlite3.connect('anketi.db') as conn:
            result = func(conn, *args, **kwargs)

        return result

    return decorator


@ensure_connection
def init_db(conn, force: bool = False):

    c = conn.cursor()

    if force:
        c.execute("DROP TABLE IF EXISTS users")

    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id              INTEGER PRIMARY KEY,
        first_name                   STRING,
        last_name                    STRING,
        date                         STRING,
        user_id                     INTEGER,
        purchase         INTEGER DEFAULT 0);
    """)

    c.execute('''CREATE TABLE IF NOT EXISTS sales(
        id                  INTEGER PRIMARY KEY,
        user_id                         INTEGER,
        date                            STRING);
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS buyers(
        id                  INTEGER PRIMARY KEY,
        user_id                         INTEGER,
        first_name                      STRING);
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS settings(
    id                        NTEGER PRIMARY KEY,
    information              STRING DEFAULT text,
    hello                   STRING DEFAULT text);
    ''')

    conn.commit()


@ensure_connection
def edit_settings_inf(conn, information: str):
    c = conn.cursor()

    c.execute('UPDATE settings SET information = ?', (information,))

    conn.commit()


@ensure_connection
def edit_settings_hel(conn, hello: str):
    c = conn.cursor()

    c.execute('UPDATE settings SET hello = ?', (hello,))

    conn.commit()


@ensure_connection
def return_hello(conn):
    c = conn.cursor()

    c.execute("SELECT hello FROM settings")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_information(conn):
    c = conn.cursor()

    c.execute("SELECT information FROM settings")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def add_user(conn, first_name: str, last_name: str, date: str, user_id):
    c = conn.cursor()

    c.execute("INSERT INTO users (first_name, last_name, date, user_id) VALUES (?, ?, ?, ?)", (first_name, last_name, date, user_id))

    conn.commit()


@ensure_connection
def add_sale(conn, user_id, date: str):
    c = conn.cursor()

    c.execute("INSERT INTO sales (user_id, date) VALUES (?, ?)", (user_id, date))

    conn.commit()


@ensure_connection
def add_buyer(conn, user_id, first_name: str):
    c = conn.cursor()

    c.execute("INSERT INTO buyers (user_id, first_name) VALUES (?, ?)", (user_id, first_name))

    conn.commit()


@ensure_connection
def return_users(conn):
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM users")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_buyers(conn):
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM buyers")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_cash_1(conn):
    c = conn.cursor()

    c.execute("SELECT cash FROM cash")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_sales(conn):
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM sales")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def add_sale_user(conn, purchase, user_id):
    c = conn.cursor()

    c.execute("UPDATE users set purchase = ? WHERE user_id = ?", (purchase, user_id))

    conn.commit()


@ensure_connection
def return_user_sale(conn, user_id):
    c = conn.cursor()

    c.execute("SELECT purchase FROM users WHERE user_id = ?", (user_id,))

    all_results = c.fetchone()

    return all_results