# Selenium Automation Framework (Python + PyTest)

## Overview
This automation suite is developed as part of the Alpha26 interview assignment (Task 3.2).
It validates the login functionality of the demo website:
https://the-internet.herokuapp.com/login

The framework is implemented using:
- Selenium WebDriver (Python)
- PyTest Framework
- Page Object Model (POM)
- Explicit Waits (No hardcoded sleeps)

---

## Project Structure

automation/
│
├── pages/
│   ├── login_page.py
│   └── secure_page.py
│
├── tests/
│   └── test_login.py
│
├── conftest.py
├── requirements.txt
└── README.md

---

## Test Scenarios Covered

### 1. Valid Login and Logout Test
- Navigate to login page
- Login using valid credentials
- Verify Secure Area heading is displayed
- Logout successfully
- Verify redirect back to login page
- Validate logout success message

### 2. Invalid Login Test
- Navigate to login page
- Login using invalid credentials
- Verify error message is displayed

---

## Tools & Libraries Used
- Python 3.x
- Selenium WebDriver
- PyTest
- WebDriver Manager (Auto ChromeDriver handling)

---

## Setup Instructions

### 1. Prerequisites
Make sure the following are installed:
- Python 3.x
- Google Chrome Browser

Check Python version:
```bash
python --version
