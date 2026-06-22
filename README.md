# Amazon Automation Framework

A scalable and maintainable UI automation framework built using **Playwright (Python)** and the **Page Object Model (POM)** design pattern.

The framework is designed with enterprise-level automation practices, focusing on maintainability, reusability, reliability, and ease of integration into CI/CD pipelines.

---

## Overview

This project automates key Amazon user journeys such as:

- Product search
- Search result validation
- Product selection
- Cart operations
- End-to-end customer workflows

The framework follows industry-standard automation engineering principles to support long-term scalability and team collaboration.

---

## Architecture

The framework adopts the **Page Object Model (POM)** design pattern.

### Design Goals

- Separation of concerns
- Reusable page components
- Reduced test maintenance
- Improved readability
- Easier onboarding of new automation engineers

### High-Level Structure

```text
amazonAutomationPlaywright/
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_results_page.py
│   └── product_page.py
│
├── tests/
│   ├── test_product_search.py
│   └── test_add_to_cart.py
│
├── utilities/
│   ├── config.py
│   ├── logger.py
│   └── test_data.py
│
├── reports/
│
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
