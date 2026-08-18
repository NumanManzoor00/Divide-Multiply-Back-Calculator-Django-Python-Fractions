# Divide & Multiply-Back Calculator

A simple Django calculator that uses Python's built-in `Fraction` module to perform **exact division and multiplication-back calculations** without floating-point precision errors.

### Example

```text
100 ÷ 3 = 100/3
100/3 × 3 = 100
```

## Features

* Exact arithmetic using `fractions.Fraction`
* Django form validation
* Division and multiplication-back verification
* Responsive and simple user interface
* Handles division without floating-point precision loss
* Clear display of the original input, quotient, and multiplication-back result

## Tech Stack

* **Python**
* **Django**
* **HTML & CSS**
* **fractions.Fraction**

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/NumanManzoor00/Divide-Multiply-Back-Calculator-Django-Python-Fractions.git
```

### 2. Open the Project

```bash
cd Divide-Multiply-Back-Calculator-Django-Python-Fractions
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

### 7. Open in Browser

Visit:

```text
http://127.0.0.1:8000/
```

## How It Works

1. Enter a **dividend**.
2. Enter a **divisor**.
3. Django validates the submitted values.
4. Python's `Fraction` performs the division exactly.
5. The quotient is multiplied back by the divisor.
6. The application displays the exact division and multiplication-back results.

### Calculation Flow

```text
Dividend ÷ Divisor
        ↓
Exact Fraction
        ↓
Quotient × Divisor
        ↓
Original Dividend
```

## Project Structure

```text
Divide-Multiply-Back-Calculator-Django-Python-Fractions/
├── calculator/
│   ├── logic.py
│   ├── forms.py
│   ├── views.py
│   └── templates/
│       └── calculator/
│           └── calculator.html
├── calcsite/
├── manage.py
├── requirements.txt
└── README.md
```

## Why Use `Fraction`?

Floating-point numbers can produce unexpected precision results:

```python
0.1 + 0.2
# 0.30000000000000004
```

Python's `Fraction` class represents numbers as exact rational values:

```python
from fractions import Fraction

result = Fraction(100, 3)

print(result)
# 100/3
```

The calculation can then be multiplied back exactly:

```python
result * 3
# 100
```

This makes `Fraction` useful when exact mathematical results are more important than floating-point approximations.

## Purpose

This project demonstrates how **Django and Python's `Fraction` module** can be combined to build a simple calculator that performs accurate division and verifies the result through multiplication-back calculations.

It is also a practical example of:

* Django forms
* Django views
* Python modules
* Exact arithmetic
* Input validation
* Basic frontend integration

## License

For educational and personal use.
