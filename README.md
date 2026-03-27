# 🎮 OpenCritic PC Games Scraper

A Python-based web scraping script that extracts PC game data from OpenCritic and stores it in a structured Excel file.

---

## 📌 Overview

This project scrapes game information from the OpenCritic PC browse page and collects:

* Game Title
* Critic Rating
* Genre
* Release Date
* Platform

The extracted data is saved into an Excel file for further analysis.

---

## 🛠️ Tech Stack

* Python
* requests
* BeautifulSoup (bs4)
* openpyxl

---

## ⚙️ How It Works

1. Sends an HTTP request to the OpenCritic PC games page
2. Parses HTML using BeautifulSoup
3. Extracts:

   * Titles
   * Ratings
   * Genre, Release Date, Platform
4. Stores data in an Excel sheet using openpyxl
5. Saves the file as:

```
Games_Scraping.xlsx
```

---

## 🚀 Installation

Install required dependencies:

```bash
pip install requests beautifulsoup4 openpyxl
```

---

## ▶️ Usage

Run the script:

```bash
python your_script_name.py
```

After execution:

* Data will be printed in the console
* Excel file will be generated in the project directory

---

## 📂 Output

The Excel file contains:

| Games Names | Ratings | Genres | Release Dates | Platforms |
| ----------- | ------- | ------ | ------------- | --------- |

---

## ⚠️ Disclaimer

This project is created for educational purposes only.
All data is sourced from OpenCritic and belongs to their respective owners.

---

## ⚠️ Limitations

* Depends on OpenCritic page structure (may break if website changes)
* No error handling for request failures
* No pagination support (scrapes only visible data)

---

## 🔧 Future Improvements

* Add pagination support
* Handle request failures and retries
* Export to CSV/Database
* Add filtering and analytics

---

## 👤 Author

Mugesh
