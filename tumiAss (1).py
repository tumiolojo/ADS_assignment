
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(r"/Users/mac/Downloads/International_Breweries.csv")

df.head()

month_map = {
    'January':'01', 
    'February':'02', 
    'March':'03', 
    'April':'04', 
    'May':'05', 
    'June':'06',
    'July':'07',
    'August':'08',
    'September':'09',
    'October':'10',
    'November':'11',
    'December':'12'
}

df['MONTH_NO'] = df['MONTHS'].map(month_map)
df.head()
df['DATE'] = '01-'+df['MONTH_NO']+ '-' + df['YEARS'].astype(str)
df['DATE'].dtypes
df['DATE'].unique()
df['DATE'] =  pd.to_datetime(df['DATE'])
df.rename(columns = {'REGION ':'REGION'}, inplace = True)


profit_trend = df.groupby(['YEARS','BRANDS']).sum().unstack().loc[:,'PROFIT']
print(profit_trend)



profit_trend.plot()
plt.legend(loc='upper right')
plt.xlabel('Date')
plt.ylabel('Profit')
plt.title('Line Plot showing the total profit over time')
plt.savefig("lINE PLOT.png")
plt.show()






def plot_profit_trends(df, date, profit):
    '''
        Takes in a dataframe contains a profit column and date column and displays lineplot of the profit trend over time
        
        Args:
            df => pandas.dataframe
            date => str, representing the name of date column in dataframe
            profit => str, representing the name of date column in dataframe
        Returns:
            grapgh => lineplot
    '''
    brands = df['BRANDS'].unique()
    profit_trend = df.groupby([date, 'BRANDS']).sum()[profit].unstack().reset_index()

    
    plt.figure(figsize = (20,10)) # set size of line plot
    for brand in brands:
        
     
        plt.plot(profit_trend['YEARS'], profit_trend[brand])
    plt.xlabel('Date')
    plt.ylabel('Profit')
    plt.title('Line Plot showing the total profit over time')
    
    plt.show()
    
    
    
plot_profit_trends(df, 'YEARS', 'PROFIT')

df.groupby('REGION').sum()['QUANTITY']


def plot_quantity_by_region(df, region, quantity):
    """
    

    Takes in a dataframe containimg a quantity column and region column and displays pie chat of quantity sold in each region
    
    Args:
        df => pandas.dataframe
        region => str, representing the name of region column in dataframe
        quantity => str, representing the name of quantity column in dataframe
    Returns:
        graph => piechart

    """
    
    
    unit_sold_by_region =  df.groupby(region).sum()[quantity]
    region = unit_sold_by_region.index
    quantity = unit_sold_by_region.to_list()
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'grey', 'orange']
    labels = ['west','south east','north central','north east','northwest','southsouth']
    
    #plt.figure(figsize = (20,10)) # set size of line plot
    plt.pie(quantity, colors=colors, autopct='%1.1f%%')
    
    plt.axis('equal')
    plt.legend(labels)
    plt.show()
    
plot_quantity_by_region(df, 'REGION', 'QUANTITY')


def plot_profit_by_sales_rep(df, sales_rep, profit):
    '''
        Takes in a dataframe containimg a profit column and sales_rep column and displays bar chat of profit made by each sales rep
        
        Args:
            df => pandas.dataframe
            sales_rep => str, representing the name of sales_rep column in dataframe
            profit => str, representing the name of profit column in dataframe
        Returns:
            grapgh => barchart
    '''
    
    profit_by_sales_rep =  df.groupby(sales_rep).sum()[profit].sort_values(ascending=False)
    sales_rep = profit_by_sales_rep.index
    profit = profit_by_sales_rep.to_list()
    
    y_pos = np.arange(len(sales_rep))
    
    
    plt.figure(figsize = (20,10)) # set size of line plot
    plt.bar(y_pos, profit, alpha=0.7)
    plt.xticks(y_pos, sales_rep)
    plt.ylabel('Profit')
    plt.title('Profit made by Sales Representative')
    
    plt.show()
    
plot_profit_by_sales_rep(df, 'SALES_REP', 'PROFIT') 
    
    
    
    
    
    
    
    