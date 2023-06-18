# Invsto Screening Task
As a next step of your application, please submit the assignment listed below:

 

1. Data is listed below for one ticker symbol. Create a table in a database (Postgres or MySQL). Use Python to insert data into the database.
2. Use Python to analyze data and create an investing/trading strategy of your choice. If you are not aware of any strategy: use simple moving average crossover
Submit the result of how your strategy is performing.

 

 

Test Case:
Check if input data is valid ( Open High Low Close need to be decimals), volume needs to be integer, instrument needs to be String, datetime needs to be datetime

Bonus: Try improving the assignment with backtesting libraries, metrics, parameter optimization or any custom analysis.


## Task 1

The first task was to add data in a relational table. For this, I have used MySQL table. The output can be seen in table.jpg. 

### Explaination

The python module pymysql is used to connect to a database. First a new database is created, then a new table is created. The data to this is added by converting the .xlsx file into a dataframe and then added row wise to the table. In addition to this, the existence of table and database is checked, hence only by changing the .xlsx file name, a new file can be added to the table without any other intervention. 

[Link](https://github.com/akankshsinhaa/invsto_screening_task/blob/main/invsto%20addToTable.ipynb)

## Task 2

### Explaination

The python module matplotlib is used to plot the graph for the prices provided in the dataset. It shows that the data is in an uptrend. This information would be valuable later. For the strategy part, a simple SMA Crossover Strategy is used of 10 days and 20 days time frame. When the 10 days line crosses over the 20 days line, buy signal is generated. If 10 days line goes below the 20 days line, a sell signal is generated. It gives around 13% returns.

[Link](https://github.com/akankshsinhaa/invsto_screening_task/blob/main/invsto%20analysis%20and%20strategy.ipynb)

## Test Cases

### Explaination

Each object in the data frame is checked if it is the required object. If it does not match, test case fails. The unittest module is used for the same.

[Link](https://github.com/akankshsinhaa/invsto_screening_task/blob/main/unittests_invsto.py)

## Bonus

### Explaination

A bolinger bands strategy is used in this. When the price crosses the lower band, a buy signal is generated. If it goes below the upper band a sell signal is generated. Module used is  <u>backtrader</u>. The cash is set to 100000. By changing the dev factor and period, I was able to get returns of 12%. A stop loss of 20% is also implemented.

[Link](https://github.com/akankshsinhaa/invsto_screening_task/blob/main/bonus.ipynb)
