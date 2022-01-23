import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from datetime import datetime
import calendar
import requests


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfasdfasdf'

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


@app.route('/')
def index():
    conn = get_db_connection()
    this_month_expenses = conn.execute(
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
    ).fetchall()

    sum_this_month = conn.execute(
        "SELECT "
        "SUM(sum) as amount "
        "FROM expenses "
        "WHERE strftime('%Y', date) = strftime('%Y', date('now')) AND strftime('%m', date) = strftime('%m', date('now')) "
    ).fetchall()
    sum_incomes_this_month = conn.execute(
        "SELECT "
        "SUM(amount) as amount "
        "FROM incomes "
        "WHERE strftime('%Y', date) = strftime('%Y', date('now')) AND strftime('%m', date) = strftime('%m', date('now')) "
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
        "SELECT  SUM(sum), categories.name "
        "FROM expenses  "
        "LEFT JOIN categories on categories.id = expenses.category "
        "WHERE strftime('%Y', date) = strftime('%Y', date('now')) AND strftime('%m', date) = strftime('%m', date('now')) "
        "GROUP BY category "
        "ORDER BY SUM(sum) DESC  ").fetchall()
    #
    # category_sum_all_month = conn.execute(
    #     "SELECT  SUM(sum),  strftime('%m/%Y', date) as month, strftime('%Y', date) as year "
    #     "FROM expenses  "
    #     "INNER JOIN categories ON categories.name = expenses.category "
    #     "GROUP BY month "
    #     "ORDER BY year DESC  ").fetchall()
    #
    # category_sum_all_years = conn.execute(
    #     "SELECT  SUM(sum),  strftime('%Y', date) as year "
    #     "FROM expenses  "
    #     "INNER JOIN categories ON categories.name = expenses.category "
    #     "GROUP BY year "
    #     "ORDER BY year DESC  ").fetchall()
    #
    # category_sum_all_years_cat = conn.execute(
    #     "SELECT  SUM(sum), category,  strftime('%m', date) as month, strftime('%Y', date) as year FROM expenses INNER JOIN categories ON categories.name = expenses.category GROUP BY category, month ORDER BY year DESC").fetchall()
    #
    # exepnses_this_month = conn.execute(
    #     "SELECT  sum, category, subcategory, comment, strftime('%d/%m/%Y', date) as date "
    #     "FROM expenses  "
    #     "WHERE strftime('%m.%Y', date) = strftime('%m.%Y','now') "
    #     "ORDER BY date DESC  ").fetchall()

    # years = conn.execute("SELECT strftime('%Y', date) as year FROM expenses GROUP BY year").fetchall()
    # months = conn.execute("SELECT strftime('%m', date) as month FROM expenses GROUP BY month").fetchall()

    # all = conn.execute(
    #     "SELECT strftime('%Y', date) as year, "
    #     "strftime('%m', date) as month, "
    #     "strftime('%d', date) as day, "
    #     "categories.name as category, "
    #     "subcategories.name as subcategory, "
    #     "sum, "
    #     "comment "
    #     "FROM expenses "
    #     "LEFT JOIN categories on categories.id = expenses.category "
    #     "LEFT JOIN subcategories on subcategories.id = expenses.subcategory"
    #     "").fetchall()

    conn.close()

    return render_template('index.html', title='My Finance Tracker', gradient='text-gradient-blue',
                           this_month_expenses=this_month_expenses, sum_this_month=sum_this_month,
                           sum_incomes_this_month=sum_incomes_this_month, category_sum_total=category_sum_total,
                           this_year=this_year, this_month=this_month)


@app.route('/all-expenses')
def all_expenses():
    conn = get_db_connection()
    all_expenses = conn.execute(
        'SELECT expenses.id,  strftime("%d.%m.%Y", date) as date_s, sum, categories.name as category, categories.color as color, subcategories.name as subcategory, comment FROM expenses LEFT JOIN categories on categories.id = expenses.category LEFT JOIN subcategories on subcategories.id = expenses.subcategory  ORDER BY date DESC').fetchall()
    conn.close()

    return render_template('all_expenses.html', title='All Expenses', gradient='text-gradient-red',
                           all_expenses=all_expenses)


@app.route('/years')
def years():
    conn = get_db_connection()
    all = conn.execute(
        "SELECT strftime('%Y', date) as year, "
        "strftime('%m', date) as month, "
        "strftime('%d', date) as day, "
        "categories.name as category, "
        "subcategories.name as subcategory, "
        "sum, "
        "comment "
        "FROM expenses "
        "LEFT JOIN categories on categories.id = expenses.category "
        "LEFT JOIN subcategories on subcategories.id = expenses.subcategory"
        "").fetchall()

    conn.close()

    return render_template('years.html', title='Expenses by Year', gradient='text-gradient-red', all=all)


@app.route('/add', methods=('GET', 'POST'))
def add():
    conn = get_db_connection()
    categories = conn.execute(
        "SELECT id, name, color as color, categories.state FROM categories WHERE categories.state is not 'true'").fetchall()
    subcategories = conn.execute(
        "SELECT subcategories.id as id, subcategories.name as name, categories.name as category FROM subcategories LEFT JOIN categories on categories.id = subcategories.category_id WHERE subcategories.state is not 'true'").fetchall()
    conn.close()
    if request.method == 'POST':
        sum = request.form['sum']
        category = request.form.get("category", False)
        subcategory = request.form.get("subcategory", False)
        comment = request.form['comment']

        if (not sum) or (not category):
            flash('Sum or category is required!', category='alert-warning')

        else:
            conn = get_db_connection()
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
            flash('Sum, date and category is required!', category='alert-warning')
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

    return render_template('edit_category.html', title='Edit Category', gradient='text-gradient-red', category=category)


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

    return render_template('edit_subcategory.html', title='Edit Category', gradient='text-gradient-red',
                           subcategory=subcategory)


@app.route('/category-delete/<int:id>', methods=('GET', 'POST'))
def cat_delete(id):
    category = get_category(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM categories WHERE id = ?', (id,))
    conn.execute('DELETE FROM subcategories WHERE category_id = ?', (id,))
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

        if 'cat' in request.form:
            category = request.form['category']
            color = request.form['color']

            if not category:
                flash('Category name is required', category='alert-warning')

            else:
                conn.execute("INSERT INTO categories (name, color) VALUES (?, ?)", (category, color))
                conn.commit()
                flash('Category was created', category='alert-success')
                return redirect(request.referrer)

        if 'subcat' in request.form:
            category_id = request.form['category_id']
            subcategory = request.form['subcategory']
            if not subcategory or category_id is None:
                flash('Subcategory and Category ID is required!', category='alert-warning')
            else:
                conn.execute("INSERT INTO subcategories (name, category_id) VALUES (?,?)", (subcategory, category_id))
                conn.commit()
                flash('Subategoria a fost creata', category='alert-success')
                return redirect(request.referrer)

    # conn = get_db_connection()
    categories = conn.execute('SELECT id, name, color as color, state FROM categories ORDER BY state').fetchall()
    categories_active = conn.execute(
        "SELECT id, name, color as color, state FROM categories WHERE state is not 'true'").fetchall()
    subcategories = conn.execute('SELECT id, name, state FROM subcategories ORDER BY state').fetchall()

    conn.close()
    return render_template('categories.html', title='Categories and Subcategories', gradient='text-gradient-red',
                           categories=categories,
                           subcategories=subcategories, categories_active=categories_active)


@app.route('/categories_income', methods=('GET', 'POST'))
def categories_income():
    conn = get_db_connection()
    if request.method == 'POST':
        category_income = request.form['category_income']
        primordial = request.form.get('primordial')

        if not category_income:
            flash('need a income category', category='alert-warning')

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
    categories_income = conn.execute("SELECT id, name  FROM categories_income WHERE state is not 'true'").fetchall()
    conn.close()
    if request.method == 'POST':
        amount = request.form['amount']
        category_income = request.form.get("category_income", False)
        comment = request.form['comment']

        if (not amount) or (not category_income):
            flash('Amount or Category is required!', category='alert-warning')

        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO incomes (amount, category, comment) VALUES (?, ?, ?)',
                         (amount, category_income, comment))
            conn.commit()
            conn.close()
            flash('Income was succesful added', category='alert-success')
            return redirect(request.referrer)

    return render_template('add_income.html', title='Add Income', gradient='text-gradient-green',
                           categories_income=categories_income)


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
            flash('Amount, Date and Category is required!', category='alert-warning')
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
    return render_template('incomes.html', title='Incomes', gradient='text-gradient-green', incomes=incomes)


@app.route('/<int:id>/delete_income', methods=('POST',))
def delete_income(id):
    incomes = get_incomes(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM incomes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Income was successfully deleted!', category='alert-success')
    return redirect(url_for('incomes'))
