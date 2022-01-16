import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
            (100, 'Alimente', 'Eurospin', 'comentariu')
            )
cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
            (120.45, 'Alimente', 'CTS', 'comentariu la CTS')
            )
cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
            (20.5, 'Alimente', 'Arabi', 'comentariu la Arabi')
            )

cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
            (20, 'Localuri', 'Pizza', 'am mancat pizza')
            )
cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
            (4, 'Localuri', 'cafea', 'am baut cafea')
            )

cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Alimente', '#8ed4a3'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Chiria', '#be9a4d'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Localuri', '#4dbea0'))

cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Eurospin', 'Alimente'))

cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('CTS', 'Alimente'))

cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Arabi', 'Alimente'))

connection.commit()
connection.close()
