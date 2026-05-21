# 🛒 Advanced E-commerce Data Cleaning Pipeline

## 📌 Project Description
This project demonstrates an advanced **Data Cleaning and Preprocessing Pipeline** using Python and Pandas on a simulated messy e-commerce transactions dataset (100 rows). The dataset contained complex real-world anomalies such as mixed date formats, structural missing fields, currency symbols blocking numeric logic, and negative transaction quantities.

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy
- **IDE:** VS Code

## ⚙️ Implemented Cleaning Steps & Advanced Techniques
1. **Data Exploration:** Diagnosed data integrity, types, and logical anomalies using `.info()` and `.describe()`.
2. **Text Standardization:** Unified `Customer email` to lowercase, stripped extra whitespaces, and formatted `Product name` with proper capitalization.
3. **Advanced Numeric Handling:** 
   - Converted negative quantities to absolute positive values using `.abs()`.
   - Cleaned the `Item price` column by stripping the currency symbol (`" $"`), removing structural string fields (`"missing"`, `"nan"`), and forcing correct numeric conversion.
4. **Date Standardization:** Fixed mixed and broken date formats (slashes, hyphens, and invalid strings like `"unknown"`) by parsing them through `pd.to_datetime()` with strict error handling, setting a baseline default for tracking.
5. **Deduplication:** Eliminated complete row duplicates to ensure unique transaction records.

## 📈 Final Deliverable
The raw, broken data was successfully transformed into a reliable, structured numeric database, fully prepared for further revenue analysis, forecasting, or reporting.
