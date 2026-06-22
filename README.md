Amazon Automation Framework
Overview

This repository contains a scalable UI automation framework developed using Playwright (Python), Pytest-BDD, and the Page Object Model (POM) design pattern.

The framework automates an end-to-end Amazon shopping journey, including product search, product selection, cart operations, and quantity management.

The project was designed with maintainability, reusability, and scalability in mind, following modern Quality Engineering and Test Automation best practices.

Technology Stack
Component	Technology
Programming Language	Python
UI Automation	Playwright
Test Framework	Pytest
BDD Framework	pytest-bdd
Design Pattern	Page Object Model (POM)
Reporting	Allure Reports
Containerization	Docker
Version Control	Git
Framework Architecture

The framework follows a layered architecture that separates business logic from test implementation.

amazonAutomationPlaywright
│
├── pages/
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
Design Principles
Page Object Model (POM)

Each page within the application is represented by a dedicated Page Object.

Responsibilities include:

Element locators
Page interactions
Reusable business actions

Example:

class HomePage(BasePage):

    def search_field(self, product_name):
        self.page.fill(self.SEARCH_BOX, product_name)
        self.page.press(self.SEARCH_BOX, "Enter")

This approach minimizes duplication and improves maintainability when UI changes occur.

Base Page

The Base Page acts as the foundation for all page objects and centralizes common functionality such as:

Browser actions
Navigation
Waiting strategies
Element interactions
Assertions

This promotes consistency throughout the framework.

BDD Layer

Business requirements are captured using Gherkin syntax.

Example:

Feature: Amazon Product Shopping

Scenario: Search for a product, add to cart, view cart, and increase quantity

  Given I am on the Amazon homepage
  When I search for "Laptop Stand"
  Then I click the "Amazon Basics Laptop Stand Riser" product to view it and add to my cart
  Then I increase the quantity to "2"

This enables technical and non-technical stakeholders to understand automated scenarios easily.

Automation Flow

The automated workflow covers:

Navigate to Amazon
Search for a product
Validate search results
Select a product
Add product to cart
Open cart
Increase quantity
Verify successful update
Reporting

The framework integrates with Allure Reporting.

Generate report results:

pytest --alluredir=allure-results

Generate HTML report:

allure serve allure-results

Reports include:

Execution summaries
Test status
Failure details
Screenshots
Execution history
Running Tests
Install Dependencies
pip install -r requirements.txt
Install Playwright Browsers
playwright install
Execute Test Suite
pytest
Execute Specific Scenario
pytest tests/steps/test_amazon_steps.py
Docker Execution

Build Docker image:

docker build -t amazon-playwright .

Run tests:

docker run amazon-playwright

This enables consistent execution across development, QA, and CI/CD environments.

CI/CD Readiness

The framework has been structured for seamless integration with:

Jenkins
GitHub Actions
GitLab CI/CD
Azure DevOps

Typical pipeline flow:

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
Framework Benefits
Maintainability

UI changes are isolated within Page Objects.

Reusability

Common actions are centralized and reused across scenarios.

Scalability

New pages and workflows can be added without impacting existing tests.

Readability

BDD scenarios provide clear business-level documentation.

Reliability

Playwright's built-in auto-waiting mechanisms reduce flaky tests.

Future Enhancements
 - Parallel execution
 - Cross-browser testing
 - Data-driven testing
 - API integration layer
 - Environment management
 - Screenshot-on-failure hooks
 - Jenkins pipeline integration
 - Cloud execution support
   
Author
Masixole Kondile
