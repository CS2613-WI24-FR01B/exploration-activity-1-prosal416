import pandas as pd

def convert2List(x):
    if isinstance(x, str) and '[' in x:
        return x.strip('[]').split(',')
    else:
        return x

def getMoviesByDirector(df, director):
    dfC = df.copy()
    return dfC[dfC['Director']==director].sort_values(by='Year',ascending=False)
def getMoviesByLeadActor(df, name):
    dfC=df.copy()
    return dfC[dfC['Lead Actor'].apply(lambda x: name in x if isinstance(x,list) else x == name)].sort_values(by='Year',ascending=False)
def getMoviesByGenre(df, genre):
    dfC=df.copy()
    return dfC[dfC['Genre'].apply(lambda x: genre in x if isinstance(x,list) else x == genre)].sort_values(by='Year',ascending=False)
def filterMoviesByYear(choice, df, val):
    dfC = df.copy()
    if choice == 1:
        sendDF = dfC[dfC['Year']<val].sort_values(by='Year',ascending=False)
    elif choice == 2:
        sendDF = dfC[dfC['Year']==val].sort_values(by='Year',ascending=False)
    else:
        sendDF = dfC[dfC['Year']>val].sort_values(by='Year',ascending=False)
    return sendDF
    
def filterMoviesByRating(choice, df, val):
    if choice == 1:
        return df[df['Letterboxd Rating']<val].sort_values(by='Letterboxd Rating',ascending=False)
    elif choice == 2:
        return df[df['Letterboxd Rating']==val].sort_values(by='Letterboxd Rating',ascending=False)
    else:
        return df[df['Letterboxd Rating']>val].sort_values(by='Letterboxd Rating',ascending=False)
    
def recommendMovies(df,genre,rating):
    dfC=df.copy()
    genreDF= dfC[dfC['Genre'].apply(lambda x: genre in x if isinstance(x,list) else x == genre)]
    return filterMoviesByRating(3,genreDF,rating)

with open('movieData.txt', 'r') as file:
    col = file.readline().strip().split(';')

df = pd.read_csv('movieData.txt', sep=';',skiprows=[0],names=col)

df['Year']=df['Year'].astype(int)
df['Letterboxd Rating']=pd.to_numeric(df['Letterboxd Rating'],errors='coerce')
df['Lead Actor']=df['Lead Actor'].apply(convert2List)
df['Genre']=df['Genre'].apply(convert2List)
df.sort_values(by='Name',inplace=True)
df.reset_index(drop=True)

while True:
    print("Choose an option:\n")
    print("1. Recommend a list of movies")
    print("2. Get a list of movies by director")
    print("3. Get a list of movies by lead actor")
    print("4. Get a list of movies by year")
    print("5. Get a list of movies by Letterboxd rating")
    print("6. Get a list of movies by genre")
    print("7. Give me the list of all the movies in the database\n")
    print("Enter anything to leave")
    choice=input("Enter your choice: ")
    
    if choice=='1':
        genre = input("Enter a genre (ex. Drama, Sci-Fi or Romance): ")
        rating = float(input("Enter a rating (max 5.0): "))
        print("\n")
        print(recommendMovies(df,genre,rating).to_string(index=False))
    elif choice=='2':
        name = input("Enter a director's name (include first and last name): ")
        print("\n")
        print(getMoviesByDirector(df,name).to_string(index=False))
    elif choice=='3':
        name = input("Enter an actors's name (include first and last name): ")
        print("\n")
        print(getMoviesByLeadActor(df,name).to_string(index=False))
    elif choice=='4':
        year = int(input("Enter a year: "))
        choice = int(input("Enter a choice (1. Before, 2. Current, 3. After): "))
        print("\n")
        print(filterMoviesByYear(choice,df,year).to_string(index=False))
    elif choice=='5':
        rating = float(input("Enter a rating (max 5.0): "))
        choice = int(input("Enter a choice (1. Less than, 2. Equals to, 3. Greater than): "))
        print("\n")
        print(filterMoviesByRating(choice,df,rating).to_string(index=False))
    elif choice=='6':
        name = input("Enter a genre (ex. Drama, Sci-Fi or Romance): ")
        print("\n")
        print(getMoviesByGenre(df,name).to_string(index=False))
    elif choice=='7':
        print("\n")
        print(df.to_string(index=False))
    else:
        break
    
