import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
            (100, '1', '1', 'comentariu'))
cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
            (120.45, '1', '2', 'comentariu la CTS'))
cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
            (20.5, '1', '3', 'comentariu la Arabi')
            )

cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
            (20, '3', '0', 'am mancat pizza')
            )
cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
            (4, '3', '0', 'am baut cafea')
            )

cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Alimente', 'gradient_9'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Chiria', 'gradient_2'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Localuri', 'gradient_23'))

cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Eurospin', '1'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('CTS', '1'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Arabi', '1'))

cur.execute("INSERT INTO categories_income (name, primordial) VALUES (?, ?)", ('Upwork', ''))
cur.execute("INSERT INTO categories_income (name, primordial) VALUES (?, ?)", ('Salariu Oleg', 'true'))
cur.execute("INSERT INTO categories_income (name, primordial) VALUES (?, ?)", ('Salariu Natasa', 'true'))

cur.execute("INSERT INTO incomes (amount, category, comment) VALUES (?, ?, ?)", ('1600', '1', ''))
cur.execute("INSERT INTO incomes (amount, category, comment) VALUES (?, ?, ?)", ('600', '2', ''))

connection.commit()
connection.close()
