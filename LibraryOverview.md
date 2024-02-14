1.  Pandas for Python

2.  As a simple explanation: It's a library that's used for data manipulation, wrangling and analysis. It structures tables in "data frames" for the storage of data. It's flexible in that it allows the ability to import data via csv, excel, and json files using functions like read_csv(), read_excel() and read_json.

    After using "import pandas as pd" at the top of your program, you're able to create data frames (tables) that has defined names (columns) and data (rows). 
    
3.  This is an example of converting a dictionary to a data frame:

    data = {'Team':['Raptors','Lakers','Celtics','Knicks'],
            'City':['Toronto','Los Angeles','Boston','New York']
            }
    df = pd.DataFrame(data) #pd is from the importing of pandas

    With this you can print the data frame:
    print(df)

    Add a new column:
    df['# of Championships'] = [1,17,17,2]

    Filter the data frame:
    print(df[df['# of Championships'] > 1])

    And export it to a file
    df.to_csv('example.csv')

    There are more intermediary uses with the library such as joining two data frames:
    merged = pd.merge(df1,df2,on="id", how="inner")

    And locating values by specific columns or rows:
    located = df.iloc[:,1]  #returns second column values

    The program in this exploration activity uses the basic functionality of the library.

4.  Pandas was created in 2008 by AQR Capital Management.

5.  I selected it because I have an interest in data analysis. I've taken courses on MySQL in the past, and believed that it would be a smooth transition between MySQL and Python. I also wanted to select a library that I can combine with my own personal interests in (film) so that I felt more commited and attached to the development of the program, rather than a "have to do" assignment. A stake in the game, so to speak.

6.  It led me to use functions more. I don't usually use functions unless I need to in Python. But using more functions to do the data wrangling made it easier to read, code and manage. It also allowed me more creativity for the resulting outputs, whether to sort it by 'x' or sort it by 'y' to give a more appropriate program response for the user.

7.  It was a easy library to understand the basic functions, even some of the more complex functions look to be easy to remember/implement upon repetition; it's an easy library to take in. 

    I'd recommend it to someone that wants to make a program to analyze data (obviously), but it also helps that it's easy to adopt. You can make a program that would hold a database for people to access easily, search easily, and add records to fairly easily as well.

    I'd continue to use it if I was doing any analysis. Especially if I was going to be a Data Analyst, Data Scientist, Business Analyst etc. Especially with Python being a very comfortable and easy-to-adopt programming language in combination with Pandas.