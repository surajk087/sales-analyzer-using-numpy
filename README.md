Tools & Technologies Used

- Programming Language: Python 3.x
- Library Used: NumPy
  
  
Data

The dataset represents one financial year (12 months) is given.
[12000, 8000, 150],[15000, 9000, 180], [11000, 8500, 140],[19000, 11000, 210],
[22000, 12000, 250],[21000, 12500, 240], [25000, 14000, 300],[28000, 15000, 320],
[24000, 14500, 280], [20000, 12000, 220],[30000, 16000, 350],[35000, 18000, 400]
Each row represents a month, and columns represent sales, costs, and customers.

Methods

- Profit = Sales - Costs
- Profit Margin = (Profit / Sales) × 100
- Statistical analysis using NumPy functions
- Boolean masking to filter high-margin months
- Pearson correlation using np.corrcoef()
- Terminal-based visualization
