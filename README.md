# 💸 Student Expense Tracker
 
A **Flask-based Student Expense Tracker Web Application** built with Python, enabling students to record, visualize, and analyze their spending habits through interactive charts and insights. Developed as a Python Programming Laboratory (22MDC27) project at **Coimbatore Institute of Technology**.
 
---
 
##  About the Project
 
Managing personal finances is a common challenge for students — without a clear overview of spending, it's easy to overspend or under-save. This web application helps students log expenses, understand spending patterns through visual analytics, and make smarter financial decisions.
 
The system uses a **CSV file** as a lightweight data source and generates rich visualizations using **Matplotlib**, all served through a clean **Flask** web interface.
 
---
 
##  Features
 
| Feature | Description |
|---|---|
| 📊 Overall Statistics | Total students, total & average expenses, gender-wise totals |
| 👫 Gender-wise Analysis | Bar charts, pie charts, and monthly trends split by gender |
| 📅 Monthly Trends | Line charts showing how spending changes over time |
| 🏷️ Category-wise Trends | Bar charts for Food, Travel, Stationery, and more |
| 🏆 Top Spenders | Identifies the top 5 highest-spending students |
| ➕ Add Expense | Web form to log new expense entries |
| 📥 Download Report | Export the entire dataset as a CSV file |
 
---
 
##  Tech Stack
 
| Technology | Purpose |
|---|---|
| **Python 3** | Core programming language |
| **Flask** | Web framework (routing, templates, form handling) |
| **Pandas** | Data loading, cleaning, and manipulation |
| **Matplotlib** | Chart and graph generation |
| **HTML / CSS** | Frontend structure and styling |
| **Jinja2** | Template engine for dynamic pages |
| **CSV** | Lightweight data storage |
 
---
 
##  Project Structure
 
```
PYTHON_Project/
└── student_expense_tracker/
    │
    ├── app.py                          # Main Flask application
    ├── dataset.csv                     # Expense data source (CSV)
    ├── Project_Report.pdf              # Project documentation
    │
    ├── static/                         # Auto-generated chart images
    │   ├── age_group_bar.png
    │   ├── age_group_expense.png
    │   ├── category_bar.png
    │   ├── category_expense_trend.png
    │   ├── category_gender_expense.png
    │   ├── female_pie.png
    │   ├── gender_bar.png
    │   ├── gender_expense.png
    │   ├── gender_total.png
    │   ├── male_pie.png
    │   └── monthly_trend.png
    │
    └── templates/                      # HTML pages (Jinja2)
        ├── home.html                   # Landing / dashboard page
        ├── overall.html                # Overall statistics page
        ├── gender_analysis.html        # Gender-wise analysis page
        ├── cat_ex.html                 # Category expense trends page
        ├── meee.html                   # Top spenders page
        ├── add_expense.html            # Add new expense form
        └── download_report.html        # Download report page
```
 
---
 
##  How to Run
 
### Prerequisites
- Python 3.x
- pip
### Installation
 
```bash
# 1. Clone the repository
git clone https://github.com/your-username/student-expense-tracker.git
 
# 2. Navigate to the project folder
cd student-expense-tracker
 
# 3. Install required dependencies
pip install flask pandas matplotlib
 
# 4. Run the Flask application
python app.py
```
 
### Access the App
Open your browser and go to:
```
http://127.0.0.1:5000
```
 
---
 
##  Application Routes
 
| Route | Description |
|---|---|
| `/` | Home Dashboard |
| `/overall` | Overall expense statistics |
| `/gender-analysis` | Gender-based visual analysis |
| `/category_expense_trends` | Category-wise expense bar charts |
| `/top-spenders` | Top 5 highest spenders |
| `/add-expense` | Form to add a new expense entry |
| `/download-report` | Download dataset as CSV |
 
---
 
##  Sample Output
 
The app displays insights such as:
- **1002 students** tracked with **₹2,69,508.19** total expenses
- **Average expense per student:** ₹268.97
- **Top spending category:** Transport
- **Top spender:** Student ID 8902 with ₹499.89
---
 
##  Visualizations Generated
 
- Category-wise expense bar chart by gender
- Male & Female expense distribution pie charts
- Average expense by age group (18–20, 21–23, 24–26, 27–29)
- Total expense comparison by gender
- Monthly expense trend line chart by gender
- Category-wise overall expense trend bar chart
---
 
##  Future Enhancements
 
- 🔐 User Authentication & personal profiles
- 🔍 Dashboard filters (date range, category, month)
- 📱 Mobile-responsive UI with Bootstrap/Tailwind CSS
- 🔔 Budget alerts when spending limits are exceeded
- 🤖 ML-based expense prediction from past patterns
- 📄 Export reports in PDF and Excel formats
- 🔁 Recurring expense auto-logging (rent, subscriptions)
---
