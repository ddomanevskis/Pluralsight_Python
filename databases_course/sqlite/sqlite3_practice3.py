import sqlite3
import datetime

database = sqlite3.connect("portfolio.db")

cursor = database.cursor()

create_table_query = """
CREATE TABLE investments (
    coin_id TEXT,
    currency TEXT,
    sell INT,
    amount REAL,
    date TIMESTAMP
);"""

cursor.execute(create_table_query)

imvestment = ("bitcoin", "usd", True, 1.0, datetime.datetime.now())

cursor.execute("INSERT INTO investments VALUES (?, ?, ?, ?, ?)", imvestment)

database.commit()

result = cursor.execute("SELECT * FROM investments")

all_rows = result.fetchall()

first_or_only_row = result.fetchone()