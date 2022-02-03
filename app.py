import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, render_template_string
from werkzeug.exceptions import abort
from datetime import datetime, timedelta
import calendar
import requests
import xmltodict


def get_db_connection():
    conn = sqlite3.connect('static/database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfaawefawfewfawegfargeravetyko5sdfasdf'

now = datetime.now()


@app.template_filter('month_name')
def month_name(month_number):
    return calendar.month_name[month_number]


@app.template_filter('month_abbr')
def month_abbr(month_number):
    return calendar.month_abbr[month_number]


app.jinja_env.filters['month_name'] = month_name
app.jinja_env.filters['month_abbr'] = month_abbr


def get_expenses(expense_id):
    conn = get_db_connection()
    expense = conn.execute('SELECT *, strftime("%d-%m-%Y %H:%M:%S", date) as date_s FROM expenses WHERE id = ?',
                           (expense_id,)).fetchone()
    conn.close()
    if expense is None:
        abort(404)
    return expense


def get_incomes(income_id):
    conn = get_db_connection()
    income = conn.execute('SELECT * FROM incomes WHERE id = ?', (income_id,)).fetchone()
    conn.close()
    if income is None:
        abort(404)
    return income


def get_budgets(budget_id):
    conn = get_db_connection()
    budget = conn.execute('SELECT * FROM budget WHERE id = ?', (budget_id,)).fetchone()
    conn.close()
    if budget is None:
        abort(404)
    return budget


def get_category(category_id):
    conn = get_db_connection()
    category = conn.execute('SELECT * FROM categories WHERE id = ?', (category_id,)).fetchone()
    conn.close()
    if category is None:
        abort(404)
    return category


def get_category_income(category_id):
    conn = get_db_connection()
    category = conn.execute('SELECT * FROM categories_income WHERE id = ?', (category_id,)).fetchone()
    conn.close()
    if category is None:
        abort(404)
    return category


def get_subcategory(subcategory_id):
    conn = get_db_connection()
    subcategory = conn.execute('SELECT * FROM subcategories WHERE id = ?', (subcategory_id,)).fetchone()
    conn.close()
    if subcategory is None:
        abort(404)
    return subcategory


# ///Exchange
# today = datetime.today().strftime("%d.%m.%Y")
today = datetime.now()
today = today.strftime('%d.%m.%Y')
# print(today)
url = 'https://www.bnm.md/en/official_exchange_rates?get_xml=1&date='
response = requests.get(url + today)

data = xmltodict.parse(response.content)

usd_id = '44'
eur_id = '47'
ron_id = '35'

for item in data['ValCurs']['Valute']:
    if item['@ID'] == usd_id:
        valute_rate_usd = float(item['Value'])
    if item['@ID'] == eur_id:
        valute_rate_eur = float(item['Value'])
    if item['@ID'] == ron_id:
        valute_rate_ron = float(item['Value'])


def get_usdmdl(amount):
    currency = valute_rate_usd * amount
    return round(currency, 2)


def get_mdleur(amount):
    currency = amount / valute_rate_eur
    return round(currency, 2)


def get_usdeur(amount):
    currency = (valute_rate_usd * amount) / valute_rate_eur
    return round(currency, 2)


def get_roneur(amount):
    currency = (valute_rate_ron * amount) / valute_rate_eur
    return round(currency, 2)


# print(get_usdmdl(1850))
# print(get_mdleur(33375))
# print(get_usdeur(1850))
# print(get_roneur(8093))


@app.route('/')
def index():
    conn = get_db_connection()
    this_month_transactions = conn.execute(
        "SELECT expenses.id, "
        "strftime('%Y', date) as year, "
        "strftime('%m', date) as month, "
        "strftime('%d', date) as day, "
        "categories.name as category, "
        "categories.color as color, "
        "subcategories.name as subcategory, "
        "sum, "
        "comment "
        "FROM expenses "
        "LEFT JOIN categories on categories.id = expenses.category "
        "LEFT JOIN subcategories on subcategories.id = expenses.subcategory "
        "WHERE strftime('%Y', date) = strftime('%Y', date('now')) AND strftime('%m', date) = strftime('%m', date('now')) "

        "UNION ALL "
        "SELECT incomes.id, "
        "strftime('%Y', date) as year, "
        "strftime('%m', date) as month, "
        "strftime('%d', date) as day, "
        "categories_income.name as category, "
        "NULL as color, "
        "NULL as subcategory, "
        "amount, "
        "comment "
        "FROM incomes "
        "LEFT JOIN categories_income on categories_income.id = incomes.category "
        # "LEFT JOIN subcategories on subcategories.id = incomes.subcategory "
        "WHERE strftime('%Y', date) = strftime('%Y', date('now')) AND strftime('%m', date) = strftime('%m', date('now')) "
        "ORDER BY day DESC "
    ).fetchall()

    sum_months = conn.execute(
        "SELECT "
        "sum, strftime('%m', date) as month, strftime('%Y', date) as year "
        "FROM expenses "
    ).fetchall()

    sum_months_income = conn.execute(
        "SELECT "
        "amount, strftime('%m', date) as month, strftime('%Y', date) as year "
        "FROM incomes "
    ).fetchall()

    budgets = conn.execute(
        "SELECT SUM(sum) as su, "
        "categories.name as categor, "
        "budget.amount as amount "
        "FROM  expenses "
        "LEFT JOIN categories on categories.id = expenses.category "
        "LEFT JOIN budget on categories.id = budget.category "
        "WHERE strftime('%m.%Y', date) = strftime('%m.%Y','now') "
        "GROUP BY expenses.category "
        "LIMIT 5"
    ).fetchall()

    # this month
    # WHERE strftime('%Y', entry_date) = strftime('%Y', date('now')) AND strftime('%m', entry_date) = strftime('%m', date('now'))
    this_year = datetime.now().year
    this_month = datetime.now().month
    # this_month = now.strftime("%m, %Y")
    # category_sum_month = conn.execute(
    #     "SELECT  SUM(sum), expenses.category "
    #     "FROM expenses  "
    #     "INNER JOIN categories ON categories.name = expenses.category "
    #     "WHERE strftime('%m.%Y', date) = strftime('%m.%Y','now') "
    #     "GROUP BY category "
    #     "ORDER BY SUM(sum) DESC  ").fetchall()

    # category_sum_prev = conn.execute(
    #     "SELECT  SUM(sum), expenses.category, strftime('%m/%Y', date) "
    #     "FROM expenses  "
    #     "INNER JOIN categories ON categories.name = expenses.category "
    #     "WHERE strftime('%m.%Y', date) = strftime('%m.%Y','now', '-1 month') "
    #     "GROUP BY category "
    #     "ORDER BY SUM(sum) DESC  ").fetchall()

    category_sum_total = conn.execute(
        "SELECT  sum, categories.name as category, strftime('%m', date) as month, strftime('%Y', date) as year "
        "FROM expenses  "
        "LEFT JOIN categories on categories.id = expenses.category "

    ).fetchall()

    budgets2 = conn.execute(
        "SELECT SUM(sum) as su, "
        "budget.id as bid, "
        "categories.name as categor, "
        "categories.color as color, "
        "budget.amount as amount "
        "FROM  expenses "
        "LEFT JOIN categories on categories.id = expenses.category "
        "LEFT JOIN budget on categories.id = budget.category "
        "WHERE strftime('%m.%Y', date) = strftime('%m.%Y','now') and amount != '' "
        "GROUP BY bid "
        "LIMIT 3"
    ).fetchall()

    conn.close()
    now = datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    current_day = datetime.now().day

    return render_template('index.html', title='My Finance Tracker', gradient='text-gradient-blue',
                           this_month_transactions=this_month_transactions, sum_months=sum_months,
                           sum_months_income=sum_months_income, category_sum_total=category_sum_total,
                           this_year=this_year, this_month=this_month, budgets2=budgets2, days_in_month=days_in_month,
                           current_day=current_day)


@app.route('/stats')
def stats():
    conn = get_db_connection()
    this_month_transactions = conn.execute(
        "SELECT expenses.id, "
        "strftime('%Y', date) as year, "
        "strftime('%m', date) as month, "
        "strftime('%d', date) as day, "
        "categories.name as category, "
        "categories.color as color, "
        "subcategories.name as subcategory, "
        "sum, "
        "comment "
        "FROM expenses "
        "LEFT JOIN categories on categories.id = expenses.category "
        "LEFT JOIN subcategories on subcategories.id = expenses.subcategory "
        "WHERE strftime('%Y', date) = strftime('%Y', date('now')) AND strftime('%m', date) = strftime('%m', date('now')) "

        "UNION ALL "
        "SELECT incomes.id, "
        "strftime('%Y', date) as year, "
        "strftime('%m', date) as month, "
        "strftime('%d', date) as day, "
        "categories_income.name as category, "
        "NULL as color, "
        "NULL as subcategory, "
        "amount, "
        "comment "
        "FROM incomes "
        "LEFT JOIN categories_income on categories_income.id = incomes.category "
        # "LEFT JOIN subcategories on subcategories.id = incomes.subcategory "
        "WHERE strftime('%Y', date) = strftime('%Y', date('now')) AND strftime('%m', date) = strftime('%m', date('now')) "
        "ORDER BY day DESC "
    ).fetchall()

    sum_months = conn.execute(
        "SELECT "
        "sum, strftime('%m', date) as month, strftime('%Y', date) as year "
        "FROM expenses "
    ).fetchall()

    sum_months_income = conn.execute(
        "SELECT "
        "amount, strftime('%m', date) as month, strftime('%Y', date) as year "
        "FROM incomes "
    ).fetchall()

    category_sum_total = conn.execute(
        "SELECT  sum, categories.name as category, strftime('%m', date) as month, strftime('%Y', date) as year "
        "FROM expenses  "
        "LEFT JOIN categories on categories.id = expenses.category "

    ).fetchall()

    date = datetime.now()
    return render_template('stats.html', title='Statistics', gradient='text-gradient-blue',
                           this_month_transactions=this_month_transactions, sum_months=sum_months,
                           sum_months_income=sum_months_income, category_sum_total=category_sum_total,
                           date=date)


@app.route('/all-expenses')
def all_expenses():
    conn = get_db_connection()
    all_expenses = conn.execute(
        'SELECT sum, expenses.id as id, '
        'strftime("%d", date) as day, strftime("%m", date) as month, strftime("%Y", date) as year, '
        'categories.name as category, '
        'categories.color as color, '
        'subcategories.name as subcategory, '
        'comment '
        'FROM expenses '
        'LEFT JOIN categories on categories.id = expenses.category '
        'LEFT JOIN subcategories on subcategories.id = expenses.subcategory  '
        'ORDER BY date DESC').fetchall()
    conn.close()

    return render_template('all_expenses.html', title='All Expenses', gradient='text-gradient-red',
                           all_expenses=all_expenses)


@app.route('/add', methods=('GET', 'POST'))
def add():
    conn = get_db_connection()
    categories = conn.execute(
        "SELECT categories.id as cid, categories.name as name, color as color, categories.state, count(expenses.sum) as count "
        "FROM categories "
        "LEFT JOIN expenses on categories.id = expenses.category "
        "WHERE categories.state is not 'true' "
        "GROUP BY name "
        "ORDER BY count DESC"
    ).fetchall()

    subcategories = conn.execute(
        "SELECT subcategories.id as id, subcategories.name as name, categories.name as category FROM subcategories LEFT JOIN categories on categories.id = subcategories.category_id WHERE subcategories.state is not 'true'").fetchall()
    conn.close()

    if request.method == 'POST':
        sum = request.form['sum']
        category = request.form.get("category", False)
        subcategory = request.form.get("subcategory", False)
        currency = request.form.get("currency", False)
        comment = request.form['comment']

        if (not sum) or (not category):
            flash('Amount and category is required!', category='alert-error')

        else:
            conn = get_db_connection()
            if currency == 'usd':
                sum = get_usdeur(float(sum))
            elif currency == 'mdl':
                sum = get_mdleur(float(sum))
            elif currency == 'ron':
                sum = get_roneur(float(sum))

            conn.execute('INSERT INTO expenses (sum, category, subcategory, comment) VALUES (?, ?, ?, ?)',
                         (sum, category, subcategory, comment))
            conn.commit()
            conn.close()
            flash('Expense was added successful', category='alert-success')
            return redirect(request.referrer)

    return render_template('add.html', title='Add expense', gradient='text-gradient-red', categories=categories,
                           subcategories=subcategories)


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    expense = get_expenses(id)
    conn = get_db_connection()
    categories = conn.execute(
        "SELECT id, name, color as color, state FROM categories WHERE state is not 'true'").fetchall()
    subcategories = conn.execute('SELECT id, name FROM subcategories').fetchall()
    conn.close()
    if request.method == 'POST':
        sum = request.form['sum']
        date = request.form['date']
        category = request.form.get("category", False)
        subcategory = request.form.get("subcategory", False)
        comment = request.form['comment']

        if (not sum) or (not category) or (not date):
            flash('Sum, date and category is required!', category='alert-error')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE expenses SET sum = ?, date = ?, category = ?, subcategory = ?, comment= ?'
                         ' WHERE id = ?',
                         (sum, date, category, subcategory, comment, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit_expense.html', title='Edit Expense', gradient='text-gradient-red', expense=expense,
                           categories=categories,
                           subcategories=subcategories)


@app.route('/edit-category/<int:id>', methods=('GET', 'POST'))
def edit_category(id):
    category = get_category(id)
    subcategory = get_subcategory(id)
    conn = get_db_connection()
    if request.method == 'POST':
        if 'cat' in request.form:
            name = request.form['category']
            color = request.form.get('color')
            state = request.form.get('state')
            # print(state)
            conn = get_db_connection()
            conn.execute('UPDATE categories SET name = ?, color = ?, state = ? WHERE id = ?', (name, color, state, id))
            conn.commit()
            conn.close()
            flash('"{}" was successfully changed!'.format(category['name']), category='alert-success')
            return redirect(url_for('categories'))
        if 'subcat' in request.form:
            category_id = request.form['category_id']
            subcategory = request.form['subcategory']
            if not subcategory or category_id is None:
                flash('Subcategory and Category ID is required!', category='alert-warning')
            else:
                conn.execute("INSERT INTO subcategories (name, category_id) VALUES (?,?)", (subcategory, category_id))
                conn.commit()
                flash('Subategory was succesful created', category='alert-success')
                return redirect(request.referrer)

    subcategories = \
        conn.execute(''
                     'SELECT subcategories.id as sub_id, '
                     'subcategories.name sub_name, '
                     'subcategories.state as sub_state, '
                     'subcategories.category_id as sub_cat_id, '
                     'categories.id as cat_id '
                     'FROM subcategories '
                     'LEFT JOIN categories ON cat_id = sub_cat_id '
                     'WHERE cat_id = sub_cat_id '
                     'ORDER BY sub_state '

                     ).fetchall()

    return render_template('edit_category.html', title='Edit Category', gradient='text-gradient-red', category=category,
                           subcategories=subcategories, subcategory=subcategory)


@app.route('/edit-subcategory/<int:id>', methods=('GET', 'POST'))
def edit_subcategory(id):
    subcategory = get_subcategory(id)
    conn = get_db_connection()
    if request.method == 'POST':
        if 'subcat' in request.form:
            name = request.form['subcategory']
            state = request.form.get('state')
            conn = get_db_connection()
            conn.execute('UPDATE subcategories SET name = ?, state = ? WHERE id = ?', (name, state, id))
            conn.commit()
            conn.close()
            flash('"{}" was successfully changed!'.format(subcategory['name']), category='alert-success')
            return redirect(url_for('categories'))

    return render_template('edit_subcategory.html', title='Edit Subcategory', gradient='text-gradient-red',
                           subcategory=subcategory)


@app.route('/category-delete/<int:id>', methods=('GET', 'POST'))
def cat_delete(id):
    category = get_category(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM categories WHERE id = ?', (id,))
    # conn.execute('DELETE FROM subcategories WHERE category_id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(category['name']), category='alert-success')
    return redirect(url_for('categories'))


@app.route('/subcategory-delete/<int:id>', methods=('GET', 'POST'))
def subcat_delete(id):
    subcategory = get_subcategory(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM subcategories WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(subcategory['name']), category='alert-success')
    return redirect(url_for('categories'))


@app.route('/delete-expense/<int:id>', methods=('POST',))
def delete(id):
    # print(request.url)
    expense = get_expenses(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(expense['sum']), category='alert-success')
    if 'to-all' in request.form:
        return redirect(url_for('all_expenses'))
    else:
        return redirect(url_for('index'))


@app.route('/categories', methods=('GET', 'POST'))
def categories():
    conn = get_db_connection()
    if request.method == 'POST':
        category = request.form['category']
        color = request.form.get('color')

        if (not category) or (not color):
            flash('Category name and color is required', category='alert-error')

        else:
            conn.execute("INSERT INTO categories (name, color) VALUES (?, ?)", (category, color))
            conn.commit()
            flash('Category was created', category='alert-success')
            return redirect(request.referrer)

        # if 'subcat' in request.form:
        #     category_id = request.form['category_id']
        #     subcategory = request.form['subcategory']
        #     if not subcategory or category_id is None:
        #         flash('Subcategory and Category ID is required!', category='alert-warning')
        #     else:
        #         conn.execute("INSERT INTO subcategories (name, category_id) VALUES (?,?)", (subcategory, category_id))
        #         conn.commit()
        #         flash('Subategoria a fost creata', category='alert-success')
        #         return redirect(request.referrer)

    # conn = get_db_connection()
    categories = conn.execute(
        "SELECT categories.id as cid, categories.name as name, color as color, categories.state, count(expenses.sum) as count "
        "FROM categories "
        "LEFT JOIN expenses on categories.id = expenses.category "
        # "WHERE categories.state is not 'true' "
        "GROUP BY name "
        "ORDER BY categories.state , count DESC"
    ).fetchall()
    # categories_active = conn.execute(
    #     "SELECT id, name, color as color, state FROM categories WHERE state is not 'true'").fetchall()
    # subcategories = conn.execute('SELECT id, name, state FROM subcategories ORDER BY state').fetchall()

    conn.close()
    return render_template('categories.html', title='Categories', gradient='text-gradient-red',
                           categories=categories)


@app.route('/categories_income', methods=('GET', 'POST'))
def categories_income():
    conn = get_db_connection()
    if request.method == 'POST':
        category_income = request.form['category_income']
        primordial = request.form.get('primordial')

        if not category_income:
            flash('Category Name is required!', category='alert-error')

        else:
            conn.execute("INSERT INTO categories_income (name, primordial) VALUES (?, ?)",
                         (category_income, primordial))

            conn.commit()
            flash('Income category was succesful creted', category='alert-success')
            return redirect(request.referrer)

    categories_income = conn.execute(
        'SELECT id, name, primordial, state FROM categories_income WHERE primordial = "true" ORDER BY state ').fetchall()

    categories_income_second = conn.execute(
        "SELECT id, name, primordial, state FROM categories_income  WHERE primordial IS NULL OR primordial = '' ORDER BY state ").fetchall()

    conn.close()
    return render_template('categories_income.html', title='Incomes categories', gradient='text-gradient-green',
                           categories_income=categories_income, categories_income_second=categories_income_second)


@app.route('/edit-category-income/<int:id>', methods=('GET', 'POST'))
def edit_category_income(id):
    category = get_category_income(id)
    conn = get_db_connection()
    if request.method == 'POST':
        if 'cat' in request.form:
            name = request.form['category']
            primordial = request.form.get('primordial')
            state = request.form.get('state')
            conn = get_db_connection()
            conn.execute('UPDATE categories_income SET name = ?, primordial = ?, state = ? WHERE id = ?',
                         (name, primordial, state, id))
            conn.commit()
            conn.close()
            flash('"{}" was successfully changed!'.format(category['name']), category='alert-success')
            return redirect(url_for('categories_income'))

    return render_template('edit_category_income.html', title='Edit Category Income', gradient='text-gradient-green',
                           category=category)


@app.route('/category-income-delete/<int:id>', methods=('GET', 'POST'))
def cat_income_delete(id):
    category = get_category_income(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM categories_income WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(category['name']), category='alert-success')
    return redirect(url_for('categories_income'))


@app.route('/add_income', methods=('GET', 'POST'))
def add_income():
    conn = get_db_connection()
    categories_income = conn.execute(
        "SELECT id, name  FROM categories_income WHERE state is not 'true' and primordial is 'true'").fetchall()
    categories_income_second = conn.execute(
        "SELECT id, name  FROM categories_income WHERE state is not 'true' and primordial is NULL").fetchall()
    conn.close()
    if request.method == 'POST':
        amount = request.form['amount']
        category_income = request.form.get("category_income", False)
        comment = request.form['comment']
        currency = request.form.get("currency", False)

        if (not amount) or (not category_income):
            flash('Amount or Category is required!', category='alert-error')

        else:
            conn = get_db_connection()
            if currency == 'usd':
                amount = get_usdeur(float(amount))
            elif currency == 'mdl':
                amount = get_mdleur(float(amount))
            elif currency == 'ron':
                amount = get_roneur(float(amount))
            conn.execute('INSERT INTO incomes (amount, category, comment) VALUES (?, ?, ?)',
                         (amount, category_income, comment))
            conn.commit()
            conn.close()
            flash('Income was succesful added', category='alert-success')
            return redirect(request.referrer)

    return render_template('add_income.html', title='Add Income', gradient='text-gradient-green',
                           categories_income=categories_income, categories_income_second=categories_income_second)


@app.route('/income-edit/<int:id>', methods=('GET', 'POST'))
def edit_income(id):
    income = get_incomes(id)
    conn = get_db_connection()
    categories = conn.execute('SELECT id, name FROM categories_income').fetchall()
    conn.close()
    if request.method == 'POST':
        amount = request.form['amount']
        date = request.form['date']
        category = request.form.get("category", False)
        comment = request.form['comment']

        if (not amount) or (not category) or (not date):
            flash('Amount, Date and Category is required!', category='alert-error')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE incomes SET amount = ?, date = ?, category = ?,  comment= ?'
                         ' WHERE id = ?',
                         (amount, date, category, comment, id))
            conn.commit()
            conn.close()
            return redirect(url_for('incomes'))

    return render_template('edit_income.html', title='Edit Income', gradient='text-gradient-green', income=income,
                           categories=categories)


@app.route('/incomes')
def incomes():
    conn = get_db_connection()
    incomes = conn.execute(
        'SELECT incomes.id, strftime("%m", date) as month, strftime("%Y", date) as year, amount, categories_income.name as category, comment  FROM incomes LEFT JOIN categories_income on categories_income.id = incomes.category').fetchall()

    conn.close()
    return render_template('incomes.html', title='All incomes', gradient='text-gradient-green', incomes=incomes)


@app.route('/<int:id>/delete_income', methods=('POST',))
def delete_income(id):
    incomes = get_incomes(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM incomes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Income was successfully deleted!', category='alert-success')
    return redirect(url_for('incomes'))


# Budget
@app.route('/budgets')
def budgets():
    conn = get_db_connection()
    budgets2 = conn.execute(
        "SELECT SUM(sum) as su, "
        "budget.id as bid, "
        "categories.name as categor, "
        "categories.color as color, "
        "budget.amount as amount, "
        "COUNT(sum) as cnt "
        "FROM  expenses "
        "LEFT JOIN categories on categories.id = expenses.category "
        "LEFT JOIN budget on categories.id = budget.category "
        "WHERE strftime('%m.%Y', date) = strftime('%m.%Y','now') and amount != '' "
        "GROUP BY bid"
    ).fetchall()

    conn.close()
    now = datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    current_day = datetime.now().day
    return render_template('budgets.html', title='Budgets', budgets2=budgets2,
                           gradient='text-gradient-blue', days_in_month=days_in_month, current_day=current_day)


@app.route('/delete-budget/<int:id>', methods=('POST',))
def delete_budget(id):
    budgets = get_budgets(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM budget WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Budget was successfully deleted!', category='alert-success')
    return redirect(url_for('budgets'))


@app.route('/add_budget', methods=('GET', 'POST'))
def add_budget():
    conn = get_db_connection()
    categories = conn.execute(
        "SELECT categories.id as cid, categories.name as name, color as color, categories.state, count(expenses.sum) as count, budget.category as budget_category "
        "FROM categories "
        "LEFT JOIN expenses on categories.id = expenses.category "
        "LEFT JOIN budget on categories.id = budget.category "
        # "WHERE budget_category != expenses.category "
        "WHERE categories.state is not 'true' "
        "GROUP BY name "
        "ORDER BY count DESC"
    ).fetchall()

    conn.close()
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form.get("category", False)
        if (not amount) or (not category):
            flash('Amount or Category is required!', category='alert-warning')

        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO budget (amount, category) VALUES (?, ?)',
                         (amount, category))
            conn.commit()
            conn.close()
            flash('Budget was succesful added', category='alert-success')
            return redirect(request.referrer)

    return render_template('add_budget.html', title='Add Budget', gradient='text-gradient-blue',
                           categories=categories)


@app.route('/edit_budget/<int:id>', methods=('GET', 'POST'))
def edit_budget(id):
    budget = get_budgets(id)
    conn = get_db_connection()
    categories = conn.execute(
        "SELECT categories.id as cid, categories.name as name, color as color, categories.state, count(expenses.sum) as count, budget.category as budget_category "
        "FROM categories "
        "LEFT JOIN expenses on categories.id = expenses.category "
        "LEFT JOIN budget on categories.id = budget.category "
        # "WHERE budget_category != expenses.category "
        "WHERE categories.state is not 'true' "
        "GROUP BY name "
        "ORDER BY count DESC"
    ).fetchall()

    conn.close()
    if request.method == 'POST':
        amount = request.form.get('amount')
        category = request.form.get("category", False)
        # category = request.form.get("bid")
        if (not amount) or (not category):
            flash('Amount or Category is required!', category='alert-warning')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE budget SET amount = ?, category = ?  WHERE id = ?',
                         (amount, category, id))

            # conn.execute('UPDATE incomes SET amount = ?, date = ?, category = ?,  comment= ?'
            #              ' WHERE id = ?',
            #              (amount, date, category, comment, id))

            conn.commit()
            conn.close()
            flash('Budget was succesful changed', category='alert-success')
            return redirect(url_for('budgets'))

    return render_template('edit_budget.html', title='Edit Budget', gradient='text-gradient-blue',
                           categories=categories, budget=budget)


@app.route('/test')
def test():
    return render_template_string('''
<video id="video" width="640" height="480" autoplay style="background-color: grey"></video>
<button id="send">Take & Send Photo</button>
<canvas id="canvas" width="640" height="480" style="background-color: grey"></canvas>

<script>

// Elements for taking the snapshot
var video = document.getElementById('video');
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream;
        video.play();
    });
}

// Trigger photo take
document.getElementById("send").addEventListener("click", function() {
    context.drawImage(video, 0, 0, 640, 480); // copy frame from <video>
    canvas.toBlob(upload, "image/jpeg");  // convert to file and execute function `upload`
});

function upload(file) {
    // create form and append file
    var formdata =  new FormData();
    formdata.append("snap", file);

    // create AJAX requests POST with file
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "{{ url_for('upload') }}", true);
    xhr.onload = function() {
        if(this.status = 200) {
            console.log(this.response);
        } else {
            console.error(xhr);
        }
        alert(this.response);
    };
    xhr.send(formdata);
}

</script>
''')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # fs = request.files['snap'] # it raise error when there is no `snap` in form
        fs = request.files.get('snap')
        if fs:
            print('FileStorage:', fs)
            print('filename:', fs.filename)
            fs.save('image.jpg')
            return 'Got Snap!'
        else:
            return 'You forgot Snap!'

    return 'Hello World!'
