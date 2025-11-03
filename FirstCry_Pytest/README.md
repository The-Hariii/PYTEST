# FirstCry Pytest Selenium Conversion

This project mirrors the Java Selenium TestNG project behavior.
Flow: Open site -> Login (OTP manual wait) -> Search -> Add to Wishlist & Cart -> Open Cart/Wishlist -> Remove item.

Run:
1. pip install -r requirements.txt
2. pytest
3. Open reports/report.html

Notes:
- testdata.xlsx must exist with headers: mobile, product
- Screenshots saved to reports/screenshots/
