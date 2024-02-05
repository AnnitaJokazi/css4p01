import pandas as pd

df = pd.read_csv("/Users/NOMASIMPHIWE  JOKAZI/MYCHPC/movie_dataset.csv")

#Question 1: Highest rated movie

highestRated_movie = df[df['Rating'] == df['Rating'].max()]['Title'].values[0]
print(highestRated_movie)

#Question 2: Average Revenue
    
averageRevenue = df['Revenue (Millions)'].mean()
print(averageRevenue)

#Question 3: Average Revenue from 2015 to 2017 filtered

filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
averageRevenue_from_2015_to_2017 = filtered_df['Revenue (Millions)'].mean()
print(averageRevenue_from_2015_to_2017)

#Question 4: Movies Released in the year 2016

moviesReleased_in_2016 = df[df['Year'] == 2016]
numberOfMovies_in_2016 = len(moviesReleased_in_2016)
print(numberOfMovies_in_2016)

#Question 5: Number of movies directed by Christopher Nolan

moviesDirected_by_chrisnolan = df[df['Director'] == 'Christopher Nolan'].shape[0]
print(moviesDirected_by_chrisnolan)

#Question 6: Number of movies with 8.0 rating

movies_with80_rating = df[df['Rating'] >= 8.0].shape[0]
print(movies_with80_rating)

#Question 6: Median rating of movies directed by Christopher Nolan

chrisNolan_movies = df[df['Director'] == 'Christopher Nolan']
medianRating_of_moviesby_chrisNolan = chrisNolan_movies['Rating'].median()
print(medianRating_of_moviesby_chrisNolan)

#Question 8: Year with the highest average rating

yearly_average_rating = df.groupby('Year')['Rating'].mean()
year_with_highestAverage_rating = yearly_average_rating.idxmax()
print(year_with_highestAverage_rating)

#Question 9: Percentage increase in number of movies made between 2006 and 2016

numOfMoviesReleased_in_2006 = df[df['Year'] == 2006].shape[0]
numOfMoviesReleased_in_2016 = df[df['Year'] == 2016].shape[0]

percentage_increase = ((numOfMoviesReleased_in_2016 - numOfMoviesReleased_in_2006) / numOfMoviesReleased_in_2006) * 100
print(percentage_increase)

#Question 10: Most common actor
from collections import Counter

all_actors = df['Actors'].str.split(', ').sum()
actor_counts = Counter(all_actors)
most_common_actor = actor_counts.most_common(1)[0]
print(most_common_actor)


#Question 11: Unique genres

uniqueGenres = set(df['Genre'].str.split(',').explode())
numberOf_uniqueGenres =  len(uniqueGenres)
print(numberOf_uniqueGenres)

#Question 12: Correlation of the numerical
    
numeric_columns = df.select_dtypes(include='number')
correlation_matrix = numeric_columns.corr()



