## Property Valuation Based on Area and Price

This repository contains a Python script for estimating the valuation of a property based on its area and historical price data. The script processes a list of areas and their corresponding prices, identifies and filters outliers, and calculates the most likely price based on the given area. The program uses statistical techniques, such as mean and standard deviation, to ensure that extreme outliers do not skew the results.



## 📄 Description

The script is designed to process input data about property areas and prices and return an estimated price for a specified area. The logic works by detecting outliers in the data using statistical measures and then calculating an estimated price based on the remaining valid data.



## 📊 Code Explanation
### 1. Importing Iibraries
```python
import math
import os
import random
import re
import sys
import statistics
```



### 2. The Valuation Function

The main functionality of the program is inside the valuation() function. It processes the input data (area and price) and returns an estimated price for the given area.

```python
def valuation(reqArea, area, price):
```
- **reqArea**: The area (in square feet) for which we need to estimate the price.
- **area**: A list of property areas from the dataset.
- **price**: A list of property prices corresponding to the areas.


#### 2.1 Grouping by price
```python
area_price_list = {}

# Group all prices by their area
for a, p in zip(area, price):
    if a in area_price_list:
        area_price_list[a].append(p)
    else:
        area_price_list[a] = [p]
```

**purpose**: This section groups the property prices by area.

**Explanation**:

- We iterate over the area and price lists using the zip() function, which combines the two lists element by element.
- For each pair of area (a) and price (p), we check if the area a already exists as a key in the area_price_list dictionary:
  - If it does, we append the price p to the existing list.
  - If not, we create a new list with the price p as the first element.
    
**Example**:

- **Input: area** = [1000, 1500, 1500, 1000], price = [200000, 300000, 290000, 210000]
- **Resulting area_price_list**: {1000: [200000, 210000], 1500: [300000, 290000]}


#### 2.2 Filtering Outliers
```python
filtered_area = []
filtered_price = []

# Filter out outliers for each area
for a in sorted(area_price_list.keys()):
    prices = area_price_list[a]
    
    # If only one house with specified area, it's an outlier
    if len(prices) == 1:
        continue
    
    # Calculate mean and standard deviation
    mean_price = statistics.mean(prices)
    std_dev_price = statistics.stdev(prices) if len(prices) > 1 else 0
    
    # Filter out the prices that deviate more than three standard deviations from the mean
    for p in prices:
        if abs(p - mean_price) <= 3 * std_dev_price:
            filtered_area.append(a)
            filtered_price.append(p)
```

**Purpose**: This section identifies and filters out outlier prices based on the area. Outliers are prices that are significantly different from the mean of the group (more than 3 standard deviations away).

**Explanation**:
- Check for Single Entries: If there is only one property price for a particular area, it's automatically considered an outlier and skipped.
- Calculate Mean and Standard Deviation: For each area, the script calculates:

  - The mean price of properties for that area.
  - The standard deviation of the prices, which measures how much the prices vary from the mean. The higher the standard deviation, the        more spread out the prices are.
    
- Filter Prices: The script then filters out any price that deviates more than 3 standard deviations from the mean price, as these are considered outliers. Only valid prices are added to the filtered_area and filtered_price lists.


#### 2.3 Returning Final Valuation
```python
# Return the average price of the filtered prices as the final valuation
    if filtered_price:
        return statistics.mean(filtered_price)
    else:
        return 0
```

### Test Case 1 
```python
def test_case_1(self):
    reqArea = 1500
    area = [1000, 1500, 1500, 1000, 1500, 2000]
    price = [200000, 300000, 290000, 210000, 310000, 500000]
    expected = 262000
    result = valuation(reqArea, area, price)
    
    if result == expected:
        print(f"test_case_1 passed with result: {result}")
    else:
        print(f"test_case_1 failed: Expected {expected}, but got {result}")
    
    self.assertEqual(result, expected)
```
**Explanation**: Basic Validation with Multiple Prices for the Same Area

Input:
- **reqArea** = 1500: We are asking for an estimate for an area of 1500 square feet.
- **area** = [1000, 1500, 1500, 1000, 1500, 2000]: A list of areas for the available properties.
- **price** = [200000, 300000, 290000, 210000, 310000, 500000]: Corresponding prices for the areas listed above.

### Test Case 2
```python
def test_case_2(self):
    reqArea = 1000
    area = [1000, 1000, 1000, 1000, 1000]
    price = [150000, 150000, 150000, 150000, 150000]
    expected = 150000
    result = valuation(reqArea, area, price)
    
    if result == expected:
        print(f"test_case_2 passed with result: {result}")
    else:
        print(f"test_case_2 failed: Expected {expected}, but got {result}")
    
    self.assertEqual(result, expected)
```
**Explanation**: Consistent Prices for Identical Areas

Input:
- **reqArea** = 1000: We are asking for an estimate for an area of 1000 square feet.
- **area** = [1000, 1000, 1000, 1000, 1000]: A list of areas where every property is 1000 sq ft.
- **price** = [150000, 150000, 150000, 150000, 150000]: Corresponding prices are all the same for the properties.

### Test Case 3
```python
def test_case_3(self):
    reqArea = 2000
    area = [1500, 2000, 2000, 2000, 1500, 2000, 1500, 1500]
    price = [250000, 400000, 500000, 600000, 240000, 450000, 235000, 250000]
    expected = 365625
    result = valuation(reqArea, area, price)
    
    if result == expected:
        print(f"test_case_3 passed with result: {result}")
    else:
        print(f"test_case_3 failed: Expected {expected}, but got {result}")
    
    self.assertEqual(result, expected)
```
**Explanation**: Multiple Prices with Outliers for the Same Area

Input:
- **reqArea** = 2000: We are asking for an estimate for an area of 2000 square feet.
- **area** = [1500, 2000, 2000, 2000, 1500, 2000, 1500, 1500]: A list of areas with some properties at 2000 sq ft and others at 1500 sq ft.
- **price** = [250000, 400000, 500000, 600000, 240000, 450000, 235000, 250000]: Prices corresponding to the areas listed above.

## Explanation of Concepts

- Mean (Average): The arithmetic average of a list of numbers. In the script, the mean price for each area is calculated using the statistics.mean() function.
  
- Standard Deviation: A measure of how spread out the values in a data set are. A higher standard deviation indicates that the prices are more spread out, while a lower standard deviation suggests that prices are more consistent.

- Outlier Removal: By filtering out prices that are more than 3 standard deviations from the mean, the script ensures that extreme values don't skew the estimated price for a property. This method follows the statistical rule known as the "3-sigma rule," which is widely used for identifying outliers in data.























