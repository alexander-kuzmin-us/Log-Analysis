# Log Analysis Project

This is a tool for log Analysis project for [Full Stack Web Developer Nanodegree on Udacity](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## Software tools and skills used in this project

- Python
- Git
- GitHub
- Unix shell
- Relational Databases
- SQL
- PostgreSQL
- CRUD
- Vagrant


**This reporting tool is in Python written program using the psycopg2 module to connect to the database.
It's qerys would return the answers to the three questions in plain text.**

## The questions are:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Setup steps:

Installing and setting up the files:

1. Install [Vagrant](https://www.vagrantup.com/)

2. Install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)

3. Download the [vagrant setup files](https://www.vagrantup.com/downloads.html)

4. Download, unzip and put the [newsdata.sql file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) into the `<vagrant>` directory.

5. Put all files from Log_Analysis folder into the vagrant directory.

**Start the Virtual Machine:**

1. Open Terminal and `cd` into the vagrant directory.
2. Run `vagrant up` to build the VM.
3. Then run `vagrant ssh` to connect to VM.
4. `cd` into the correct project directory: cd /vagrant.
5. Load the data by using: '<psql -d news -f newsdata.sql>'
6. Run Log-Analysis.py
   Make sure you are in the vagrant directory `pwd`
   then run `python log_analysis.py`

**Expected output:**

TOP THREE MOST POPULAR ARTICLES OF ALL TIME:

"Candidate is jerk, alleges rival" - 338647 total views

"Bears love berries, alleges bear" - 253801 total views

"Bad things gone, say good people" - 170098 total views


TOP THREE MOST POPULAR AUTHORS OF ALL TIME:

"Ursula La Multa" - 507594 total views

"Rudolf von Treppenwitz" - 423457 total views

"Anonymous Contributor" - 170098 total views


DAY WITH MORE THAN 1 PERCENT ERRORS:

"July 17, 2016" - 2% errors


*Aleksandr Kuzmin* alex.kuzminn@gmal.com
