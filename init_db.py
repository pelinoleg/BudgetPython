import sqlite3

connection = sqlite3.connect('static/database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
#             (100, '1', '1', 'comentariu'))
# cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
#             (120.45, '1', '2', 'comentariu la CTS'))
# cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
#             (20.5, '1', '3', 'comentariu la Arabi')
#             )
#
# cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
#             (20, '3', '0', 'am mancat pizza')
#             )
# cur.execute("INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)",
#             (4, '3', '0', 'am baut cafea')
#             )

cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Medici', 'gradient_0'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Magazine', 'gradient_1'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Alimente', 'gradient_2'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Telefon', 'gradient_3'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Distractie', 'gradient_4'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Genti Moldova', 'gradient_5'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Tehnica', 'gradient_6'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('China', 'gradient_7'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Cadouri', 'gradient_8'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Scoala Ema', 'gradient_9'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Medicamente', 'gradient_10'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Haine', 'gradient_11'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Chiria', 'gradient_12'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Comunale', 'gradient_13'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Transport', 'gradient_14'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Calatorii', 'gradient_15'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Altele', 'gradient_16'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Localuri', 'gradient_17'))

cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Stomatolog', '1'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Risparmio casa', '2'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Eurospin', '3'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Arabi', '3'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('CTS', '3'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Haine Ema', '12'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Haine Natasa', '12'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Haine Oleg', '12'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Peleti', '14'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Gaz', '14'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Internet', '14'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Lumina', '14'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Apa', '14'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Hotel', '16'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Avia Bilete', '16'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Teste', '11'))

cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Cafea', '18'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Pizza', '18'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Mcdonalds', '18'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('Tramezzino', '18'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('chineji', '18'))
cur.execute("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", ('kebab', '18'))

cur.execute("INSERT INTO categories_income (name, primordial) VALUES (?, ?)", ('Upwork', ''))
cur.execute("INSERT INTO categories_income (name, primordial) VALUES (?, ?)", ('Salariu Oleg', 'true'))
cur.execute("INSERT INTO categories_income (name, primordial) VALUES (?, ?)", ('Salariu Natasa', 'true'))

cur.execute("INSERT INTO incomes (amount, category, comment) VALUES (?, ?, ?)", ('1600', '1', ''))
cur.execute("INSERT INTO incomes (amount, category, comment) VALUES (?, ?, ?)", ('600', '2', ''))

cur.execute("INSERT INTO budget (amount, category) VALUES (?, ?)", ('300', '3'))
cur.execute("INSERT INTO budget (amount, category) VALUES (?, ?)", ('70', '18'))
cur.execute("INSERT INTO budget (amount, category) VALUES (?, ?)", ('500', '13'))

cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-04-28  00:00:00', 9, '', '92', 'Kiabi, 12 botez Alberto'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-04-28  00:00:00', 9, '', '4.99', 'Papion ptr Botez'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-04-28  00:00:00', 13, '', '700', ''))

connection.commit()
connection.close()
