import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from datetime import datetime


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfasdfasdf'


def get_expenses(expense_id):
    conn = get_db_connection()
    expense = conn.execute('SELECT * FROM expenses WHERE id = ?', (expense_id,)).fetchone()
    conn.close()
    if expense is None:
        abort(404)
    return expense


def get_category(category_id):
    conn = get_db_connection()
    category = conn.execute('SELECT * FROM categories WHERE id = ?', (category_id,)).fetchone()
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
    expenses = conn.execute(
        'SELECT *, expenses.category, strftime("%d.%m.%Y", date) as date_s FROM expenses ORDER BY date DESC').fetchall()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    subcategories = conn.execute('SELECT * FROM subcategories').fetchall()

    now = datetime.now()
    this_month = now.strftime("%B, %Y")
    category_sum_month = conn.execute(
        "SELECT  SUM(sum), expenses.category "
        "FROM expenses  "
        "INNER JOIN categories ON categories.name = expenses.category "
        "WHERE strftime('%m.%Y', date) = strftime('%m.%Y','now') "
        "GROUP BY category "
        "ORDER BY SUM(sum) DESC  ").fetchall()

    # category_sum_prev = conn.execute(
    #     "SELECT  SUM(sum), expenses.category, strftime('%m/%Y', date) "
    #     "FROM expenses  "
    #     "INNER JOIN categories ON categories.name = expenses.category "
    #     "WHERE strftime('%m.%Y', date) = strftime('%m.%Y','now', '-1 month') "
    #     "GROUP BY category "
    #     "ORDER BY SUM(sum) DESC  ").fetchall()

    category_sum_total = conn.execute(
        "SELECT  SUM(sum), expenses.category "
        "FROM expenses  "
        "INNER JOIN categories ON categories.name = expenses.category "
        "GROUP BY category "
        "ORDER BY SUM(sum) DESC  ").fetchall()

    category_sum_all_month = conn.execute(
        "SELECT  SUM(sum),  strftime('%m/%Y', date) as month, strftime('%Y', date) as year "
        "FROM expenses  "
        "INNER JOIN categories ON categories.name = expenses.category "
        "GROUP BY month "
        "ORDER BY year DESC  ").fetchall()

    category_sum_all_years = conn.execute(
        "SELECT  SUM(sum),  strftime('%Y', date) as year "
        "FROM expenses  "
        "INNER JOIN categories ON categories.name = expenses.category "
        "GROUP BY year "
        "ORDER BY year DESC  ").fetchall()

    category_sum_all_years_cat = conn.execute(
        "SELECT  SUM(sum), category,  strftime('%m', date) as month, strftime('%Y', date) as year FROM expenses INNER JOIN categories ON categories.name = expenses.category GROUP BY category, month ORDER BY year DESC").fetchall()

    exepnses_this_month = conn.execute(
        "SELECT  sum, category, subcategory, comment, strftime('%d/%m/%Y', date) as date "
        "FROM expenses  "
        "WHERE strftime('%m.%Y', date) = strftime('%m.%Y','now') "
        "ORDER BY date DESC  ").fetchall()

    conn.close()

    return render_template('index.html', title='My budget', expenses=expenses, categories=categories,
                           subcategories=subcategories, category_sum_month=category_sum_month,
                           category_sum_total=category_sum_total,
                           this_month=this_month, category_sum_all_month=category_sum_all_month,
                           category_sum_all_years=category_sum_all_years, exepnses_this_month=exepnses_this_month,
                           category_sum_all_years_cat=category_sum_all_years_cat)


# def index():
#     return render_template('index.html')


@app.route('/add', methods=('GET', 'POST'))
def add():
    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    subcategories = conn.execute('SELECT * FROM subcategories').fetchall()
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
            flash('Form Submitted', category='alert-success')
            return redirect(request.referrer)

    return render_template('add.html', title='Add expense', categories=categories, subcategories=subcategories)


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    expense = get_expenses(id)
    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    subcategories = conn.execute('SELECT * FROM subcategories').fetchall()
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

    return render_template('edit_expense.html', expense=expense, categories=categories, subcategories=subcategories)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    expense = get_expenses(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(expense['sum']), category='alert-success')
    return redirect(url_for('index'))


@app.route('/categorii', methods=('GET', 'POST'))
def categorii():
    conn = get_db_connection()
    if request.method == 'POST':

        if 'cat' in request.form:
            category = request.form['category']
            color = request.form['color']

            if not category:
                flash('scrie ceva acolo', category='alert-warning')

            else:
                conn.execute("INSERT INTO categories (name, color) VALUES (?, ?)", (category, color))
                conn.commit()
                flash('Categoria a fost creata', category='alert-success')
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

    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    subcategories = conn.execute('SELECT * FROM subcategories').fetchall()

    conn.close()
    return render_template('categorii.html', title='Categorii si Subcategorii', categories=categories,
                           subcategories=subcategories)


@app.route('/<int:id>/cat_delete', methods=('POST',))
def cat_delete(id):
    category = get_category(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM categories WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(category['name']), category='alert-success')
    return redirect(request.referrer)


@app.route('/<int:id>/subcat_delete', methods=('POST',))
def subcat_delete(id):
    subcategory = get_subcategory(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM subcategories WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(subcategory['name']), category='alert-success')
    return redirect(request.referrer)
