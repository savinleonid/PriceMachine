
# PriceMachine

## Overview  
**PriceMachine** is a Python script designed to process, analyze, and search price lists in CSV format. It provides functionality for:  
- Loading and parsing price lists from files.  
- Searching for products by name.  
- Exporting results to an HTML file.  

The script is especially useful for working with product price lists, including calculating price per kilogram and organizing data for better analysis.  

---

## Features  
- **Load Price Lists**: Automatically scans a folder for CSV files containing "price" in their name and extracts relevant columns (product name, price, weight).  
- **Search Products**: Find products by text search within product names. Results are sorted by price per kilogram.  
- **Export to HTML**: Save search results or all loaded data to an HTML file.  
- **Console Interface**: Interactive command-line tool for ease of use.  

---

## Requirements  
- Python 3.6 or higher.  

No external dependencies are required as the script uses Python's standard library.  

---

## Installation  
1. Clone or download the script to your local machine.  
2. Ensure you have Python installed on your system.  

---

## How to Use  

### 1. Prepare Price Lists  
Ensure your price list files:  
- Are in **CSV format**.  
- Contain columns for **product name**, **price**, and **weight** (column names can be in Russian or other predefined mappings).  
- Have "price" in their filenames (case-insensitive).  

### 2. Run the Script  
Execute the script:  
```bash
python project.py
```

### 3. Commands in Console Interface  
- **Search for Products**:  
  Enter the text you want to search in product names. The script will display a table of matching products.  

- **Export Data**:  
  Type `export` to save the search results or all loaded data (if no search results) to an HTML file.  

- **Exit the Script**:  
  Type `exit` to close the console interface.  

---

## Key Functionalities  

### `load_prices`  
Loads price lists from the specified folder (default is the current directory). Extracts product names, prices, weights, and calculates the price per kilogram.  

### `find_text`  
Searches for products with names containing the specified text and sorts them by price per kilogram.  

### `export_to_html`  
Exports product data to an HTML table for easy sharing or review.  

---

## Example Usage  
### Loading Price Lists  
Place CSV files with "price" in the name in the script's folder, then run the script.  

### Searching for Products  
Example search:  
```  
Enter text for product search: apple  
```
Results:  
```  
Found products:  
   Name                  Price   Weight   File           Price per kg  
1. Apple Red            5.00    1.00     price1.csv       5.00  
2. Apple Green          4.50    1.00     price2.csv       4.50  
```

### Exporting to HTML  
```  
Enter text for product search: apple  
Found products:  
...  
Type 'export' to save results to an HTML file.  

Enter file name for export: apple_products.html  
Data successfully exported to apple_products.html  
```  

---

## Author  
**Contact**:  
- **Telegram**: [https://t.me/savinleonid](https://t.me/savinleonid)  
- **GitHub**: [https://github.com/savinleonid](https://github.com/savinleonid)  

Feel free to reach out for questions or suggestions!  
