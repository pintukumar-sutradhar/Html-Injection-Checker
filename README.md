# Html-Injection-Checker

A Python script for detecting HTML Injection vulnerabilities in web applications. This tool performs both GET and POST requests with a set of built-in payloads to identify potential vulnerabilities.

## Description

HTML Injection vulnerabilities occur when an application improperly handles user inputs and allows the injection of malicious HTML. This script automates the process of testing URLs for such vulnerabilities by crawling and injecting a variety of HTML payloads.

## Features

- **Crawls URLs**: Automatically explores pages to find forms and parameters.
- **Tests HTML Injection**: Uses a comprehensive set of built-in payloads to test for vulnerabilities.
- **Verbose Output**: Provides detailed information on which payloads were used and the results of each test.
- **Supports GET and POST Methods**: Tests both types of HTTP methods.

## Installation

Ensure you have Python 3 and `pip` installed. You can then install the required dependencies using:

pip install -r requirements.txt

# How to Use
1. Clone the Repository
Clone the repository to your local machine:

git clone https://github.com/pintukumar-sutradhar/Html-Injection-Checker.git

cd html-injection-checker

2. Configure and Run
You can run the script from the command line, providing a URL to test:

python3 html_injection_checker.py http://example.com

