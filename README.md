# Technolife Scrapper 🛒

A Python web scraper that searches [Technolife.com](https://www.technolife.com) for products and saves the results to a CSV file.

## Features

- Search any product by name
- Extracts product name, price, and link
- Saves results to CSV (Excel-compatible with Persian text)
- Returns top 10 results

## Installation

1. Clone the repository:
```bash
git clone https://github.com/alirezaeidzadeh/technolife-scrapper.git
cd technolife-scrapper
```

2. Install dependencies:
```bash
pip install -r requierments.txt
```

## Usage

Run the script and enter the product name when prompted:

```bash
python main.py
```

Example:
```
Enter product name: لپتاپ
```

Output CSV file will be saved in the `output/` folder.

## Project Structure

```
technolife-scrapper/
├── main.py            # Entry point
├── scrapper.py        # Fetching and parsing product data
├── csv_exporter.py    # Saving results to CSV
├── requierments.txt   # Dependencies
└── output/            # CSV output files (ignored by git)
```

## Dependencies

- requests
- beautifulsoup4
- pandas
