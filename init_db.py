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

cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Medici', 'gradient_9'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Magazine', 'gradient_2'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Alimente', 'gradient_3'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Telefon', 'gradient_21'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Distractie', 'gradient_23'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Genti Moldova', 'gradient_12'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Tehnica', 'gradient_11'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('China', 'gradient_14'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Cadouri', 'gradient_15'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Scoala Ema', 'gradient_16'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Medicamente', 'gradient_17'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Haine', 'gradient_18'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Chiria', 'gradient_19'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Comunale', 'gradient_20'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Transport', 'gradient_21'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Calatorii', 'gradient_22'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Altele', 'gradient_25'))
cur.execute("INSERT INTO categories (name, color) VALUES (?, ?)", ('Localuri', 'gradient_26'))

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
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-04-28  00:00:00', 15, '', '22.7', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-04-28  00:00:00', 12, 7, '19.99', 'geaca Natasa'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-04-28  00:00:00', 18, '', '3.4', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-04-28  00:00:00', 10, '', '18', 'excursie'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-04-28  00:00:00', 4, '', '14', 'Yolka'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-04-29  00:00:00', 9, '', '3.35', 'Ptr Botez'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-04-30  00:00:00', 9, '', '14', 'Lefties, 12 ptr Botez'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-01  00:00:00', 12, 8, '16', 'Ghete Oleg, Lefties'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-02  00:00:00', 3, '', '13', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-03  00:00:00', 3, '', '5.75', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-04  00:00:00', 17, '', '6.5', 'de la chineji'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-04  00:00:00', 3, '', '10.45', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-04  00:00:00', 14, '', '124', 'internet 20, apa 94'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-04  00:00:00', 9, '', '10', 'flori ptr crisma'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-04  00:00:00', 9, '', '7.5', 'jucarii Alberto'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-04  00:00:00', 10, '', '27.8', 'Menjador'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 9, '', '52', 'cutia cu stergare ptr Alberto'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '10', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '5', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '18', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '51', 'Mercadona'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 18, '', '11', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 17, '', '46', 'Psiholog Natasa'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 10, '', '28', 'Menjador'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 17, '', '40', 'ochelari Oleg'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '30', 'Lidl'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 18, '', '10', 'Kebab'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '21', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '14', 'Lidl'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '22', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '5', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 17, '', '9', 'Husa 4 Natasa'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '9', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '10', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '9.16', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 9, '', '40', '20 ptr parinte si 20 ptr cantaret la botez'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 9, '', '280', 'Bani ptr Alberto la botez'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 9, '', '5', 'bacsis la local la botez'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 17, '', '140', 'Psiholog Natasa'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '12', 'Lidl'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '13', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '39', 'Lidl'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 18, '', '15', 'Mc''donalds'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '15', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '4.5', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 18, '', '20', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '9', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '10', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 3, '', '9', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 13, '', '700', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-06  00:00:00', 14, '', '20', 'internet'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-07  00:00:00', 3, '', '4.2', 'magazin Romanesc'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-07  00:00:00', 3, '', '3.93', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-08  00:00:00', 3, '', '9.55', 'Lidl'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-08  00:00:00', 3, '', '8.82', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-08  00:00:00', 3, '', '3.59', 'Arabi'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-10  00:00:00', 3, '', '3.7', 'Mercado la mare'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-10  00:00:00', 18, '', '15', 'kebab la mare'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-11  00:00:00', 3, '', '3.37', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-12  00:00:00', 3, '', '0.69', 'Condis'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-12  00:00:00', 3, '', '9.32', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-12  00:00:00', 3, '', '1.37', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-14  00:00:00', 3, '', '2.36', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-14  00:00:00', 3, '', '6.68', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-16  00:00:00', 3, '', '5.22', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-16  00:00:00', 3, '', '4.57', 'Fructe si Legume'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-16  00:00:00', 3, '', '37.31', 'Mercadona'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-16  00:00:00', 3, '', '6.69', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-24  00:00:00', 3, '', '2', 'Magazin Romanesc'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-24  00:00:00', 3, '', '0.78', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-24  00:00:00', 3, '', '8.44', 'Mercadona'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-24  00:00:00', 3, '', '4.69', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-24  00:00:00', 3, '', '5.78', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-24  00:00:00', 3, '', '4.51', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-24  00:00:00', 3, '', '8.41', 'Lidl'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-24  00:00:00', 3, '', '1.15', 'Fructe, legume arabi'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-25  00:00:00', 3, '', '4.09', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-25  00:00:00', 18, '', '3.4', 'cafea'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-25  00:00:00', 18, '', '8', 'Arabi'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-26  00:00:00', 10, '', '6.96', 'Menjador'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-26  00:00:00', 10, '', '23', 'Excursie'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-26  00:00:00', 3, '', '4.2', 'Fructe Arabi'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-26  00:00:00', 3, '', '18', 'Lidl'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-26  00:00:00', 3, '', '1', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-29  00:00:00', 3, '', '6.55', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-29  00:00:00', 3, '', '12.6', 'Barceloneta'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-29  00:00:00', 3, '', '3.6', 'Barceloneta'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-29  00:00:00', 3, '', '3.4', 'Barceloneta'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-29  00:00:00', 18, '', '44.3', 'Barceloneta'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-29  00:00:00', 18, '', '10', 'Kebab'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-29  00:00:00', 3, '', '5.5', 'Fructe Arabi'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-05-29  00:00:00', 14, '', '14', 'Yolka'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-08  00:00:00', 3, '', '10.65', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-08  00:00:00', 17, '', '2.5', 'Farmacie, Ibuprofen Ema'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-08  00:00:00', 3, '', '20', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-08  00:00:00', 3, '', '6.5', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 13, '', '700', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 14, '', '250', 'Lumina'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 14, '', '20', 'Internet'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 5, '', '7', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 3, '', '9.25', 'chinezi'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 3, '', '5.75', 'dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 18, '', '3.4', 'cafea'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 5, '', '215', 'casuta de odihna'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 18, '', '9', 'kebab'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 3, '', '46', 'mercadona'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 3, '', '4', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 3, '', '4', 'dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 15, '', '24', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 18, '', '14', 'burgher king'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 18, '', '12', 'kebab si bere'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-15  00:00:00', 18, '', '6', 'croasant si suc'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-16  00:00:00', 3, '', '7.63', 'dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-16  00:00:00', 3, '', '7.4', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-17  00:00:00', 3, '', '1.7', 'dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-18  00:00:00', 3, '', '5.4', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-19  00:00:00', 3, '', '10', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-19  00:00:00', 3, '', '26', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-21  00:00:00', 18, '', '14', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-21  00:00:00', 3, '', '4.6', 'Dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-21  00:00:00', 3, '', '5.26', 'dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-21  00:00:00', 3, '', '5', 'inghetata'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-22  00:00:00', 17, '', '45', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-26  00:00:00', 3, '', '6', 'dia'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-26  00:00:00', 17, '', '8', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-26  00:00:00', 5, '', '59', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-26  00:00:00', 15, '', '27', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-28  00:00:00', 3, '', '10', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-06-28  00:00:00', 18, '', '20', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-01  00:00:00', 3, '', '77', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-01  00:00:00', 18, '', '40', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-01  00:00:00', 13, '', '500', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-05  00:00:00', 18, '', '13', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-05  00:00:00', 8, '', '38', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-05  00:00:00', 6, '', '20', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-11  00:00:00', 5, '', '50', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-11  00:00:00', 3, '', '14.41', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-11  00:00:00', 10, '', '80', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-11  00:00:00', 15, '', '17', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-12  00:00:00', 3, '', '74', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-12  00:00:00', 18, '', '5.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-13  00:00:00', 8, '', '16.7', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-16  00:00:00', 10, '', '27.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-16  00:00:00', 8, '', '10', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-16  00:00:00', 18, '', '2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-18  00:00:00', 18, '', '3', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-18  00:00:00', 3, '', '30', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-20  00:00:00', 9, '', '100', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-23  00:00:00', 10, '', '5', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-26  00:00:00', 3, '', '41', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-28  00:00:00', 10, '', '14', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-29  00:00:00', 14, '', '40', 'butelie de gaz'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-29  00:00:00', 14, '', '75.85', 'lumina'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-30  00:00:00', 17, '', '6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-30  00:00:00', 17, '', '14', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-30  00:00:00', 18, '', '17', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-30  00:00:00', 16, '', '15', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-09-30  00:00:00', 18, '', '5.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-01  00:00:00', 13, '', '500', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-05  00:00:00', 8, '', '4.3', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-05  00:00:00', 18, '', '1.7', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-05  00:00:00', 15, '', '3.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-08  00:00:00', 9, '', '100', 'Mihai'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-08  00:00:00', 7, '', '20', 'Camin'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-08  00:00:00', 18, '', '4.4', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-09  00:00:00', 15, '', '1.8', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-09  00:00:00', 18, '', '3.8', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-10  00:00:00', 3, '', '4.4', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-10  00:00:00', 15, '', '1.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-11  00:00:00', 15, '', '1.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-11  00:00:00', 18, '', '2.1', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-12  00:00:00', 18, '', '4', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-13  00:00:00', 18, '', '8.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-13  00:00:00', 3, '', '8.5', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-13  00:00:00', 10, '', '103', 'Mancarea'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-14  00:00:00', 3, '', '63', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-14  00:00:00', 6, '', '10', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-15  00:00:00', 15, '', '5.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-15  00:00:00', 18, '', '1', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-17  00:00:00', 18, '', '16', 'kebab'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-17  00:00:00', 3, '', '10.81', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-17  00:00:00', 18, '', '1.8', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-17  00:00:00', 10, '', '12', 'Cadou'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-17  00:00:00', 10, '', '6', 'Asigurare pe un an'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-18  00:00:00', 15, '', '5.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-19  00:00:00', 15, '', '1.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-19  00:00:00', 18, '', '9.5', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-19  00:00:00', 3, '', '7', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-20  00:00:00', 18, '', '17.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-20  00:00:00', 14, 10, '40', 'Gaz'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-20  00:00:00', 14, '', '25', 'Peleti'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-20  00:00:00', 15, '', '5.4', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-21  00:00:00', 3, '', '4.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-21  00:00:00', 15, '', '3.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-21  00:00:00', 12, '', '33', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-21  00:00:00', 9, '', '20', 'Rodina zina, max'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-21  00:00:00', 14, 12, '71', 'lumina'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-22  00:00:00', 9, '', '30', 'Alberto'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-22  00:00:00', 8, '', '8.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-23  00:00:00', 18, '', '2.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-24  00:00:00', 15, '', '4.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-24  00:00:00', 8, '', '13', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-24  00:00:00', 17, '', '20', 'radiografie dinti'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-24  00:00:00', 18, '', '1.8', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-24  00:00:00', 18, '', '3.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-28  00:00:00', 3, 3, '111', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-29  00:00:00', 9, '', '11', 'Magneti'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-30  00:00:00', 3, 5, '87', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-30  00:00:00', 18, '', '24', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-30  00:00:00', 17, '', '720', 'am dat datoriile'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-30  00:00:00', 14, '', '35', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-11-30  00:00:00', 15, '', '7.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-01  00:00:00', 18, 16, '3.1', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-02  00:00:00', 17, '', '7', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-02  00:00:00', 18, '', '2.2', 'mancare natasa'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-02  00:00:00', 16, 14, '185', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-02  00:00:00', 15, '', '18', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-02  00:00:00', 16, '', '85', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-05  00:00:00', 18, 16, '3.3', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-05  00:00:00', 18, 16, '2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-05  00:00:00', 17, '', '66', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-05  00:00:00', 18, 18, '16', 'teste antigen'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-05  00:00:00', 15, '', '5.4', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-05  00:00:00', 15, '', '6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-05  00:00:00', 15, '', '2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-05  00:00:00', 3, '', '3.5', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-05  00:00:00', 18, 17, '17.5', 'magazin ucrainesc'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-06  00:00:00', 14, 11, '43.5', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-06  00:00:00', 17, '', '0.6', '3 foi la printer'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-07  00:00:00', 3, '', '6.87', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 11, '', '30', 'Teste'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 17, '', '15', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 18, '', '16', 'notar'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 15, '', '24.5', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 15, '', '6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 18, '', '9', 'taxi'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 17, '', '6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 18, '', '4', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 15, '', '5', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 3, '', '1.5', 'taxi'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 15, '', '6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 18, 16, '6.1', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 17, '', '2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 18, '', '18.9', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 18, '', '13.35', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 15, '', '3.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 12, 6, '4.65', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 18, '', '9', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 13, '', '500', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-08  00:00:00', 15, '', '6.06', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-09  00:00:00', 18, '', '12', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-09  00:00:00', 17, '', '6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-09  00:00:00', 12, 8, '17', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-09  00:00:00', 3, '', '5', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-09  00:00:00', 12, 7, '16', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-09  00:00:00', 3, '', '10', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-10  00:00:00', 11, '', '15', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-10  00:00:00', 15, '', '9', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-10  00:00:00', 3, '', '21', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-10  00:00:00', 12, 6, '24', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-11  00:00:00', 17, '', '9', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-11  00:00:00', 15, '', '11', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-11  00:00:00', 18, '', '16', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-11  00:00:00', 18, '', '10', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-11  00:00:00', 3, '', '13', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-12  00:00:00', 18, '', '6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-12  00:00:00', 15, '', '7', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-12  00:00:00', 11, '', '43', 'Teste'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-12  00:00:00', 18, '', '8', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-13  00:00:00', 16, 15, '36', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-13  00:00:00', 16, 14, '140', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-13  00:00:00', 3, '', '26', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-13  00:00:00', 18, '', '10', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-13  00:00:00', 18, '', '12', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-13  00:00:00', 15, '', '11', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-17  00:00:00', 9, '', '33.5', 'cadou Natasa, parfum'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-17  00:00:00', 9, '', '48.48', 'cadou Sofia, Patricia, albume'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-17  00:00:00', 10, '', '100', 'Mancare'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-17  00:00:00', 9, '', '30', 'cadou Ema, lego'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-17  00:00:00', 9, '', '43', 'cadou Oleg, parfum'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-18  00:00:00', 11, '', '22', 'Teste'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-18  00:00:00', 3, 4, '5.7', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-18  00:00:00', 18, 16, '3', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-19  00:00:00', 2, 2, '20', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-19  00:00:00', 12, '', '6.5', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-19  00:00:00', 3, 3, '67.45', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-19  00:00:00', 3, 5, '20.14', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-19  00:00:00', 18, 19, '2.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-21  00:00:00', 15, '', '1.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-21  00:00:00', 2, 20, '5', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-22  00:00:00', 18, 19, '2.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-22  00:00:00', 9, '', '15', 'Cadou Ema, carti pokemon'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-24  00:00:00', 3, 3, '14', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-24  00:00:00', 14, 9, '20', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-27  00:00:00', 14, 10, '45', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-27  00:00:00', 14, 9, '30', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-27  00:00:00', 3, 3, '2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-29  00:00:00', 8, '', '7.1', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2021-12-29  00:00:00', 18, 16, '5.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-01  00:00:00', 3, 4, '11.17', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-01  00:00:00', 15, '', '4.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-01  00:00:00', 18, 18, '15.67', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-01  00:00:00', 18, 16, '2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-01  00:00:00', 3, 4, '6.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-03  00:00:00', 17, '', '21', 'Etsy Marketing'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-04  00:00:00', 18, 16, '4.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-04  00:00:00', 15, '', '4.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-04  00:00:00', 1, 1, '300', 'Stomatolog Natasa'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-04  00:00:00', 3, 5, '101', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-04  00:00:00', 18, 17, '10', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-05  00:00:00', 4, '', '10', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-06  00:00:00', 13, '', '500', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-06  00:00:00', 17, '', '25', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-08  00:00:00', 17, '', '6', 'Comision la bancimat ptr scoatere'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-08  00:00:00', 3, 3, '34.37', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-08  00:00:00', 14, 9, '36', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-09  00:00:00', 18, 18, '16.25', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-09  00:00:00', 15, '', '6.8', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-09  00:00:00', 18, 16, '6.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-10  00:00:00', 18, 19, '2.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-10  00:00:00', 18, 16, '3', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-10  00:00:00', 3, 4, '4.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-12  00:00:00', 15, '', '3.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-12  00:00:00', 18, 17, '2.2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-12  00:00:00', 17, '', '99', 'Curs despre sex Natalia Pavalachi'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-14  00:00:00', 3, 3, '34.31', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-14  00:00:00', 14, 9, '63.92', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-14  00:00:00', 18, 21, '9', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-14  00:00:00', 15, '', '1.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-15  00:00:00', 14, 9, '30', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-18  00:00:00', 16, 14, '117', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-19  00:00:00', 11, '', '2.34', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-19  00:00:00', 15, '', '1.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-19  00:00:00', 18, 16, '3', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-19  00:00:00', 12, 6, '2', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-19  00:00:00', 3, 5, '54.43', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-20  00:00:00', 14, 10, '45', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-22  00:00:00', 15, '', '1.6', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-22  00:00:00', 17, '', '25', 'Mandarine la cigirleni'))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-22  00:00:00', 3, 4, '12.17', ''))
cur.execute("INSERT INTO expenses(date,category,subcategory,sum,comment) VALUES(?, ?, ?, ?, ?)",
            ('2022-01-22  00:00:00', 11, '', '9.9', 'Test covid'))

connection.commit()
connection.close()
