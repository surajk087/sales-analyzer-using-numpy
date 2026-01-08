
import numpy as np

months=np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])

Monthlydata = np.array([   #[sales,costs,customerCount]
    [12000, 8000, 150],
    [15000, 9000, 180],
    [11000, 8500, 140],
    [19000, 11000, 210],
    [22000, 12000, 250],
    [21000, 12500, 240],
    [25000, 14000, 300],
    [28000, 15000, 320],
    [24000, 14500, 280],
    [20000, 12000, 220],
    [30000, 16000, 350],
    [35000, 18000, 400]
]) 



def Analysis(data,month):
    print("------------Business Data Analysis Report------------\n")

    sales=Monthlydata[:,0]
    costs=Monthlydata[:,1]
    customers=Monthlydata[:,2]

    profits=sales-costs

    profitmargin=(profits/sales)*100

    totalAnnual_sales=np.sum(sales)
    avgMonthlyProfit=np.mean(profits)
    maxSalesIndex=np.argmax(sales)


    print(f"Total Annual Sales: ${totalAnnual_sales}")
    print(f"Average Monthly Profit: ${avgMonthlyProfit:.2f}")
    print(f"Best Performing Months: {month[maxSalesIndex]}\n")


    print("-"*53)

    highMargin_mask=profitmargin>45

    highMargin_Months=month[highMargin_mask]

    print(f"\nMonths With Margin>45% : {",".join(highMargin_Months)}")

    correlation=np.corrcoef(customers,sales)

    corr_Value=correlation[0,1]

    print(f"Correlation (Customers vs Sales): {corr_Value:.4f}\n")


def salesChart(month,Sales_value):
    print("-----------Sales Trend Chart-------------------------\n")

    max_val=np.max(Sales_value)
    for i,j in zip(month,Sales_value):
        barl_len=int((j/max_val)*20)
        print(f"{i}: {"█"*barl_len} ${j}\n")


Analysis(Monthlydata,months)
salesChart(months,Monthlydata[:,0])