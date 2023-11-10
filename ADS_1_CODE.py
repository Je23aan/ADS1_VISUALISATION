# Here imported the required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# It also uses the first column of the dataframe as the index.
df = pd.read_csv('newjob_series.csv', index_col=0)

#Function to create lineplot
def Jobseries_lineplot(line):
    sns.set_style('whitegrid')
    line.plot(x='year', y=['Austria', 'Australia', 'China', 'Japan', 'India', 
                           'Togo','Mali', 'Mexico', 'Zimbabwe', 
                           'United Kingdom'], figsize=(16, 6), marker='o')
# Adding title and labels for the plot
    plt.title('Jobseries')
    plt.xlabel('Years')
    plt.ylabel('ADR_Working age population%')
# Display legend at the top right corner
    plt.legend(loc='upper right')
# Sets the limits of the X-axis and y-axis
    plt.xlim(2006, 2017)
    plt.ylim(10, 150)
#Function to create Barplot
def jobseries_barPlot(barplot):

    barplot.plot(x='year', y=['Australia', 'Japan'], kind='bar',
                 xlabel='Years', ylabel='ADR_Working age population%', 
                 color=('green', 'red'), legend=True)
    plt.figure(figsize=(16, 6))  # Adding the figure size
    plt.title('Comparision of Australia and Japan ADR_Working age population%')
    plt.show()
#Function to create Barplot
def jobseries_piePlot(df, year, figsize=(4, 5), fontsize=10, autopct='%1.0f%%'):
    label = ['Austria', 'Australia', 'China', 'Japan', 'India',
             'Togo', 'Mali', 'Mexico', 'Zimbabwe', 'United Kingdom']

    plt.figure(figsize=figsize) # Adding the figure size
    plt.pie(df[str(year)], autopct=autopct, labels=label)
    plt.title(f'Job series in {year}', fontsize=fontsize)
    plt.show()#Showing the pieplot

df1 = df.iloc[:-7]
#code will print the shape of the DataFrame after deleting the last 7 rows

df2 = df1.dropna(axis=0, how='any')
# It shows the complete data frame after deleting the unwanted data

df3 = df2.drop(["Country Code", "Series Name", "Series Code"], axis=1)
# In this code, df3 will contain the DataFrame without the specified columns.

df4 = df3.rename(columns={'2007 [YR2007]': '2007', '2008 [YR2008]': '2008',
                          '2009 [YR2009]': '2009', '2010 [YR2010]': '2010', 
                          '2011 [YR2011]': '2011','2012 [YR2012]': '2012',
                          '2013 [YR2013]': '2013', '2014 [YR2014]': '2014',
                          '2015 [YR2015]': '2015', '2016 [YR2016]': '2016'})

df5 = df4.transpose().astype(float)

# Which will roundup the floating values of df5
df5.round(2)

df6 = df5.reset_index(drop=True)
# Create a pandas Series object called 'year' with year values
# Add a new column called 'year' to the DataFrame 'df6' with the year values
year = pd.Series([2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016])
df6['year'] = year

df7 = pd.concat([df6.iloc[:, -1:], df6.iloc[:, :-1]], axis=1)
#Changing the last coloumn year as first coloumn.

Jobseries_lineplot(df6) #Showing the lineplot

jobseries_barPlot(df6)  # Showing the barplot

jobseries_piePlot(df4, 2007) #Showing the pieplot of 2007

jobseries_piePlot(df4, 2016) #showing the pieplot of 2016

