# Amazon Automation Framework

## Overview

Amazon Automation Framework is a scalable UI test automation solution built using **Python**, **Playwright**, **Pytest-BDD**, and the **Page Object Model (POM)** design pattern.

The framework automates end-to-end customer journeys on Amazon, including product search, product selection, cart management, and quantity updates. It has been designed with maintainability, reusability, and scalability in mind, following modern Quality Engineering best practices.

---

## Key Features

* Playwright-based UI automation
* Page Object Model (POM) architecture
* Behavior Driven Development (BDD) using Pytest-BDD
* Allure reporting integration
* Dockerized test execution
* Reusable and maintainable test components
* CI/CD ready framework structure
* Scalable design for future automation growth

---

## Technology Stack

| Component        | Technology              |
| ---------------- | ----------------------- |
| Language         | Python                  |
| Automation Tool  | Playwright              |
| Test Runner      | Pytest                  |
| BDD Framework    | Pytest-BDD              |
| Reporting        | Allure Reports          |
| Design Pattern   | Page Object Model (POM) |
| Containerization | Docker                  |
| Source Control   | Git                     |

---

## Framework Architecture

```text
amazonAutomationPlaywright
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── results_page.py
│   ├── cart_page.py
│   └── quantity_page.py
│
├── tests/
│   ├── features/
│   │   └── amazon.feature
│   │
│   └── steps/
│       ├── conftest.py
│       └── test_amazon_steps.py
│
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Design Approach

### Page Object Model (POM)

The framework follows the Page Object Model design pattern to separate test logic from page interactions.

Each page object is responsible for:

* Page locators
* Page actions
* Business workflows
* UI interactions

This approach improves maintainability and reduces duplication across test suites.

### Base Page

A shared Base Page provides common functionality such as:

* Navigation
* Element interaction
* Synchronization
* Wait strategies
* Assertions

All page objects inherit from the Base Page, promoting consistency across the framework.

### Behavior Driven Development (BDD)

Business requirements are implemented using Gherkin syntax, making scenarios easier to understand for both technical and non-technical stakeholders.

Example:

```gherkin
Feature: Amazon Product Shopping

Scenario: Search for a product, add to cart, view cart, and increase quantity

    Given I am on the Amazon homepage
    When I search for "Laptop Stand"
    Then I click the "Amazon Basics Laptop Stand Riser" product to view it and add to my cart
    Then I increase the quantity to "2"
```

---

## Automated Workflow

The framework currently automates the following customer journey:

1. Launch Amazon website
2. Search for a product
3. Select a product from search results
4. Add the product to the cart
5. Navigate to the shopping cart
6. Update product quantity
7. Verify successful cart update

---

## Installation

### Clone Repository

```bash
git clone https://github.com/GeneralMK/amazonAutomationPlaywright.git
cd amazonAutomationPlaywright
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

#### Windows

```bash
env\Scripts\activate
```

#### Linux / macOS

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

---

## Test Execution

### Run All Tests

```bash
pytest
```

### Run Specific Test Suite

```bash
pytest tests/steps/test_amazon_steps.py
```

### Execute with Verbose Output

```bash
pytest -v
```

---

## Allure Reporting

Generate Allure results:

```bash
pytest --alluredir=allure-results
```

Launch the report:

```bash
allure serve allure-results
```

The report provides:

* Execution summary
* Pass/fail statistics
* Detailed test results
* Failure analysis
* Historical execution trends

---

## Docker Execution

Build the Docker image:

```bash
docker build -t amazon-playwright .
```

Run the automation suite:

```bash
docker run amazon-playwright
```

Docker ensures consistent execution across different environments and supports CI/CD integration.

---

## CI/CD Readiness

The framework is designed to integrate with:

* Jenkins
* GitHub Actions
* GitLab CI/CD
* Azure DevOps

Typical pipeline flow:

```text
Checkout Source Code
        ↓
Install Dependencies
        ↓
Install Playwright Browsers
        ↓
Execute Tests
        ↓
Generate Allure Results
        ↓
Publish Reports
```

---

## Engineering Principles

The framework was developed following industry-standard Quality Engineering practices:

* Separation of concerns
* Single Responsibility Principle (SRP)
* DRY (Don't Repeat Yourself)
* Reusable test components
* Stable locator strategy
* Maintainable automation architecture
* CI/CD compatibility

---

## Future Enhancements

* Cross-browser execution
* Parallel test execution
* Data-driven testing
* API automation integration
* Environment configuration management
* Screenshot capture on failure
* Cloud execution support
* Advanced reporting dashboards

---

## Author

### Masixole Kondile


---

*"Quality is not tested into a product; it is engineered into the delivery process."*
