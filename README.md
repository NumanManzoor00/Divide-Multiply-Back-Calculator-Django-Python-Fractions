# Divide & Multiply-Back Calculator

A simple Django calculator that uses Python's `Fraction` module for **exact division and multiplication-back calculations** without floating-point precision errors.

### Example

```text
100 ÷ 3 = 100/3
100/3 × 3 = 100
```

## Features

* Exact calculations with `Fraction`
* Django form validation
* Division and multiplication-back verification
* Simple responsive UI
* Prevents floating-point precision errors

## Tech Stack

* Python
* Django
* HTML & CSS
* `fractions.Fraction`

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/NumanManzoor00/Divide-Multiply-Back-Calculator-Django-Python-Fractions.git
```

### 2. Open the Project

```bash
cd Divide-Multiply-Back-Calculator-Django-Python-Fractions
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

### 6. Open in Browser

```text
http://127.0.0.1:8000/
```

## How It Works

1. Enter a dividend.
2. Enter a divisor.
3. Django validates the input.
4. `Fraction` performs exact division.
5. The result is multiplied back by the divisor.
6. The application displays the final results.

## Project Structure

```text
calcsite/
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

## Why `Fraction`?

Floating-point calculations can cause precision issues:

```python
0.1 + 0.2
# 0.30000000000000004
```

`Fraction` keeps calculations mathematically exact:

```python
from fractions import Fraction

Fraction(100, 3)
# 100/3
```

## Purpose

This project demonstrates how **Django + Python `Fraction`** can be used to build an accurate calculator without floating-point precision loss.

## License

For educational and personal use.
