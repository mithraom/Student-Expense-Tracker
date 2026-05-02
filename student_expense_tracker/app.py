from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import pandas as pd
import os
import tempfile
import shutil
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend to avoid GUI errors
import matplotlib.pyplot as plt
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Set dataset path
DATA_PATH = r"C:\SEM II PROJECTS\PYTHON_Project\student_expense_tracker\dataset.csv"

# Ensure image directory exists
os.makedirs("static/images", exist_ok=True)

# Function to safely load the dataset
def load_data():
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date'])
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
        df = df.dropna(subset=['Age'])

        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
        df = df.dropna(subset=['Amount'])

        df['Category'] = df['Category'].str.strip().str.title()
        return df
    return pd.DataFrame()


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/overall')
def overall():
    df = load_data()
    if df.empty:
        flash("No data available.", 'danger')
        return redirect(url_for('home'))

    return render_template("overall.html",
                           total_students=df['StudentID'].nunique(),
                           total_expense=df['Amount'].sum(),
                           avg_expense=round(df['Amount'].mean(), 2),
                           male_expense=df[df['Gender'] == 'Male']['Amount'].sum(),
                           female_expense=df[df['Gender'] == 'Female']['Amount'].sum())

@app.route('/gender-analysis')
def gender_analysis():
    df = load_data()
    if df.empty:
        flash("No data available for analysis.", 'danger')
        return redirect(url_for('home'))

    # Category-wise bar chart
    category_expense = df.groupby(['Gender', 'Category'])['Amount'].sum().unstack().fillna(0)
    category_expense.T.plot(kind='bar', figsize=(10, 6))
    plt.title('Category-wise Expense by Gender')
    plt.ylabel('Total Expense')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/images/category_bar.png")
    plt.close()

    # Pie charts
    for gender in ['Male', 'Female']:
        cat_data = df[df['Gender'] == gender].groupby('Category')['Amount'].sum()
        plt.figure(figsize=(6, 6))
        plt.pie(cat_data, labels=cat_data.index, autopct='%1.1f%%', startangle=140)
        plt.title(f'{gender} Expense Distribution')
        plt.tight_layout()
        plt.savefig(f"static/images/{gender.lower()}_pie.png")
        plt.close()

    # Age group vs avg expense
    df['AgeGroup'] = pd.cut(df['Age'], bins=[17, 20, 23, 26, 29], labels=["18-20", "21-23", "24-26", "27-29"])
    age_avg_expense = df.groupby(['AgeGroup', 'Gender'])['Amount'].mean().unstack().fillna(0)
    age_avg_expense.plot(kind='bar', figsize=(10, 6))
    plt.title('Avg Expense by Age Group and Gender')
    plt.ylabel('Average Expense')
    plt.tight_layout()
    plt.savefig("static/images/age_group_bar.png")
    plt.close()

    # Gender total bar
    gender_total = df.groupby('Gender')['Amount'].sum()
    gender_total.plot(kind='bar', color=['skyblue', 'lightpink'])
    plt.title('Total Expense by Gender')
    plt.ylabel('Total Expense')
    plt.tight_layout()
    plt.savefig("static/images/gender_total.png")
    plt.close()

    # Monthly trend
    df['Month'] = df['Date'].dt.to_period('M')
    monthly = df.groupby(['Month', 'Gender'])['Amount'].sum().unstack().fillna(0)
    monthly.plot(figsize=(10, 6))
    plt.title('Monthly Expense Trend by Gender')
    plt.ylabel('Total Expense')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/images/monthly_trend.png")
    plt.close()

    return render_template("gender_analysis.html")

@app.route('/category_expense_trends')
def category_expense_trends():
    df = load_data()
    if df.empty:
        flash("No data available for trend analysis.", 'danger')
        return redirect(url_for('home'))

    category_expense_data = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    category_expense_data.plot(kind='bar', color='mediumseagreen')
    plt.title('Category-wise Expense Trends')
    plt.xlabel('Category')
    plt.ylabel('Total Expense')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/category_expense_trend.png')
    plt.close()

    return render_template('cat_ex.html')

@app.route('/top-spenders')
def top_spenders():
    # Read dataset
    df = pd.read_csv('dataset.csv')

    # Group by StudentID and sum Amount
    grouped = df.groupby('StudentID')['Amount'].sum().reset_index()

    # Sort in descending order and get top 5
    top_spenders_list = grouped.sort_values(by='Amount', ascending=False).head(5).values.tolist()

    return render_template('meee.html', top_spenders=top_spenders_list)

@app.route('/add-expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        student_id = request.form['student_id']
        gender = request.form['gender']
        age = request.form['age']
        category = request.form['category']
        amount = request.form['amount']
        date = request.form['date']

        try:
            new_entry = pd.DataFrame({
                'StudentID': [student_id],
                'Gender': [gender],
                'Age': [float(age)],
                'Category': [category.strip().title()],  # Normalize new entry category
                'Amount': [float(amount)],
                'Date': [pd.to_datetime(date)]
            })

            df = load_data()
            df = pd.concat([df, new_entry], ignore_index=True)

            # Save using a temp file to avoid overwrite errors
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp:
                df.to_csv(tmp.name, index=False)
                shutil.move(tmp.name, DATA_PATH)

            flash("Expense added successfully!", 'success')
        except Exception as e:
            flash(f"Error adding expense: {e}", 'danger')

        return redirect(url_for('add_expense'))

    return render_template("add_expense.html")

@app.route('/download-report')
def download_report():
    if os.path.exists(DATA_PATH):
        return send_file(DATA_PATH, as_attachment=True)
    else:
        flash("No report available for download.", 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
