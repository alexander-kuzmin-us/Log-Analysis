# Newspaper Log Analysis Tool

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13.3-blue)
![Python](https://img.shields.io/badge/Python-3.9-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A robust Python-based log analysis tool that explores a newspaper website's database to answer key business questions through SQL queries. This project was developed as part of the [Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## 📊 Project Overview

This reporting tool uses Python with the psycopg2 module to connect to a PostgreSQL database containing newspaper website logs. It answers three critical business questions through efficient SQL queries and presents the results in an easy-to-read format.

### Key Questions Answered

1. **Article Popularity**: What are the three most popular articles of all time?
2. **Author Rankings**: Who are the most popular article authors of all time?
3. **Error Analysis**: On which days did more than 1% of user requests lead to errors?

## 🛠️ Technologies Used

- **Python 3**: Core programming language
- **PostgreSQL**: Relational database management system
- **psycopg2**: Python PostgreSQL adapter
- **SQL**: Query language for database operations
- **Git & GitHub**: Version control and code repository
- **Linux/Unix**: Development environment
- **Vagrant**: Virtual development environment management

## 🔧 Installation and Setup

### Prerequisites

Before you begin, ensure you have the following tools installed:

- [Vagrant](https://www.vagrantup.com/) (2.2.x or higher)
- [VirtualBox](https://www.virtualbox.org/) (6.1.x or higher)
- Terminal or Command Prompt

### Step-by-Step Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/newspaper-log-analysis.git
   cd newspaper-log-analysis
   ```

2. **Set up the Vagrant environment**:
   ```bash
   vagrant up
   vagrant ssh
   ```

3. **Navigate to the project directory**:
   ```bash
   cd /vagrant
   ```

4. **Download and set up the database**:
   - Download the [newsdata.sql file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
   - Extract and place it in the `/vagrant` directory
   - Load the data:
     ```bash
     psql -d news -f newsdata.sql
     ```

5. **Run the log analysis tool**:
   ```bash
   python logs_analysis.py
   ```

## 📋 Expected Results

When run successfully, the script will produce the following output:

```
TOP THREE MOST POPULAR ARTICLES OF ALL TIME:

"Candidate is jerk, alleges rival" - 338647 total views
"Bears love berries, alleges bear" - 253801 total views
"Bad things gone, say good people" - 170098 total views

TOP THREE MOST POPULAR AUTHORS OF ALL TIME:

"Ursula La Multa" - 507594 total views
"Rudolf von Treppenwitz" - 423457 total views
"Anonymous Contributor" - 170098 total views

DAYS WITH MORE THAN 1 PERCENT ERRORS:

"July 17, 2016" - 2% errors
```

## 🔍 Database Schema

The news database includes three tables:
- **articles**: Contains article information (author, title, slug, etc.)
- **authors**: Contains author details
- **log**: Contains web server log entries for the site

## 🧩 How It Works

The tool uses three carefully crafted SQL queries to analyze the database:

1. **Article Query**: Joins the articles and log tables to count article views.
2. **Author Query**: Links authors to their articles and calculates total views.
3. **Error Query**: Calculates the percentage of failed requests per day.

## 🚀 Code Improvements

The latest version includes:
- Enhanced error handling
- Improved SQL query efficiency
- Better code organization with modular functions
- Comprehensive documentation
- PEP 8 style compliance

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Alexander Kuzmin.

---

*This project was completed as part of the Udacity Full Stack Web Developer Nanodegree program.*
