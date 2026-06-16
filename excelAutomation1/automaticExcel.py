import openpyxl as xl
from openpyxl import load_workbook, Workbook
from openpyxl.utils import get_column_letter
import sys
from pathlib import Path




"""
Scenario : 

A mid-sized retail brand runs both online and physical store sales across Pakistan. Every month, the operations manager gets two separate Excel files from the e-commerce team and the store billing team. Each file is full of raw transaction data, but the manager still has to manually build a summary report showing:

total sales by product category
monthly sales trends
top-performing sales reps
revenue and profit by region

Because the source files change every week, the same reporting work has to be repeated from scratch each month. They want a Python automation solution that can take the raw data and generate a clean summary report automatically.

Your task

Use Python with openpyxl to create an automated reporting workflow that:

reads both raw data sheets,
combines and cleans the data,
builds pivot-style summaries,
formats the output into a professional report sheet,
highlights top categories and top performers,
keeps the process reusable when new data is added.

The workbook includes 2 filled data sheets with lots of realistic sales records, so it is ready to use as the source file for that automation exercise.

"""

### real implementation starts from here 

def     populate_Lists(category_total_sales, monthly_sales_trends, top_sales_reps, region_revenue, region_profit, work_sheet_online, work_sheet_store ):

    row = 2
    col = 1

    

    for row in range(2, work_sheet_online.max_row + 1):
        for col in range(1, work_sheet_online.max_column +  1):
            char = get_column_letter(col)

            if work_sheet_online[char + str(row)] in 

            





def excel_Automation( path ):

    if path == None:
        print("Please enter the path ")
        sys.exit(1)
    
    
    file = Path(path)

    if(file.exists()):
        print(" file exists ")
    else:
        print("file doesn't exis ")
        sys.exit(1)
    
    work_book = xl.load_workbook(path)

    try:
        work_sheet_online = work_book["Online_Orders"]
    except Exception as e:
        print(e)
    
    try:
        work_sheet_store = work_book("Store_Orders")
    except Exception as e:
        print(e)
    

    ## data list creation 

    category_total_sales = [[]] 
    monthly_sales_trends = [[]]
    top_sales_reps = [[]]
    region_revenue = [[]]
    region_profit = [[]]
    

    populate_Lists(
        category_total_sales, monthly_sales_trends, top_sales_reps,
        region_revenue, region_profit, work_sheet_online, work_sheet_store
    )



if __name__ == "__main__":
    excel_Automation(sys.argv[1])


