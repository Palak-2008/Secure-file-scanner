
# Secure File Scanner

Secure File Scanner is a Python-based cybersecurity project that scans text files for potential sensitive-data patterns using regular expressions.

## Features

- Detects email address patterns
- Detects phone number patterns
- Assigns illustrative severity levels
- Displays scan results in a Streamlit dashboard
- Filters results by severity
- Exports scan reports as CSV files
- Supports text files up to 1 MB each

## Technologies Used

- Python
- Streamlit
- Pandas
- Regular Expressions (Regex)

## How It Works

1. Upload sample text files.
2. Scan the files for configured email and phone number patterns.
3. Review detected categories and severity levels.
4. View the results in the dashboard.
5. Download the scan report as a CSV file.

## Project Structure

```text
Securefile Scanner/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── sample_files/
    ├── normal.txt
    ├── customer_data.txt
    └── confidential.txt
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/secure-file-scanner.git
cd secure-file-scanner
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## Testing

This project is intended for educational use and should be tested using sample text files containing fictional data.

## Limitations

- Detection is limited to configured email and phone number patterns.
- Severity levels are illustrative and may require analyst review.
- The application does not block data transfers or confirm actual data leaks.
- This prototype is not a replacement for an enterprise Data Loss Prevention (DLP) solution.

## Author

Palak Parmar
