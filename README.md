# DataForge
![DataForge](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

## 🛠️ Overview
**DataForge** is a powerful test data generation framework designed for developers who need realistic and relationally consistent data for testing SQL databases. With built-in support for complex data structures, relationships, and a customizable setup, DataForge makes it easy to create data tailored to your project's specific requirements.

## ✨ Features
- **Automatic Database Structure Detection**: Detects tables and relationships, ensuring data consistency.
- **Complex Data Relationships**: Supports one-to-one, one-to-many, and many-to-many relationships.
- **Customizable Data Generation**: Control field types, ranges, regex patterns, and more.
- **Realistic Data**: Leverages `Faker` for realistic names, dates, addresses, and other essential data types.
- **CLI and API Integration**: Quickly generate data via CLI or integrate with REST API.
- **Export to CSV, JSON, or SQL**: Flexible data export options for easy integration with different systems.

## 📦 Installation
Install DataForge from GitHub (or PyPI):
```bash

git clone https://github.com/dreamerScape/DataForge.git
cd dataforge
pip install -r requirements.txt
