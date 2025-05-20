# Automated Civil Citation Import to OpenGov

This Python project automates the process of importing historical civil citation data from Excel into the OpenGov permitting system. It uses Selenium WebDriver to log in, navigate the UI, fill out forms, and submit records one at a time.

---

## What is OpenGov?

[OpenGov](https://opengov.com) is a cloud-based software platform used by governments and municipalities to manage workflows, permitting, licensing, budgeting, and transparency. In this project, OpenGov was used as the permitting system where Code Enforcement staff manage civil citation workflows.

---

## Background

The City was using a deprecated Microsoft Access 2010 database to store over 7,000 civil citation records dating back to 2004. Code Enforcement staff already used OpenGov for workflow, so we chose to migrate legacy data into the same platform.

OpenGov offered a paid professional services option—but to avoid that cost, I built this script.

---

## Features

- Reads and parses Excel files using `pandas`
- Automates login and navigation in OpenGov using Selenium
- Populates fields dynamically per-record
- Handles 7,000+ records reliably with only minor restart needs
- Designed with timing and load issues in mind

---

## Tech Stack

- Python 3
- pandas
- selenium
- ChromeDriver

---

## Lessons Learned

- Script succeeded in migrating all data but occasionally broke due to timing/page load issues. If I did it again, I’d add logic to auto-refresh or recover mid-process.
- This project gave me hands-on experience with real-world browser automation.

---

## Usage

1. Install required packages:
   ```bash
   pip install pandas selenium openpyxl
