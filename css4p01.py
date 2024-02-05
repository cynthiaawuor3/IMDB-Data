# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:58:54 2024

@author: Cynthia
"""

import pandas as pd

# Load the dataset  # replace with the actual path
movies_df = pd.read_csv("movie_dataset.csv")
print(movies_df)
#print(movies_df['Metascore'])
print(movies_df.info())
movies_df.columns = movies_df.columns.str.replace(' ', '_')
# Handling missing values - assuming you want to drop rows with missing values
movies_df_cleaned = movies_df.dropna()

# Display information about the cleaned dataset
print(movies_df_cleaned.info())

# Perform EDA (Exploratory Data Analysis) - Example: Display summary statistics
print(movies_df_cleaned.describe())

#movies_df_cleaned.to_csv(index=False)
# Find the movie with the highest rating
highest_rated_movie = movies_df_cleaned.loc[movies_df_cleaned['Rating'].idxmax()]

# Display the details of the highest-rated movie
print("Highest Rated Movie:")
print(highest_rated_movie[['Title', 'Rating']])

# Calculate the average revenue
average_revenue = movies_df_cleaned['Revenue_(Millions)'].mean()

# Display the average revenue
print(f"Average Revenue: {average_revenue} Million")

# Determine the range based on the answer choices
if average_revenue > 200:
    print("More than 200 Million")
elif 70 <= average_revenue <= 100:
    print("Between 70 and 100 Million")
elif 120 <= average_revenue <= 140:
    print("Between 120 and 140 Million")
elif 100 <= average_revenue <= 120:
    print("Between 100 and 120 Million")
else:
    print("The average revenue does not fall within the provided ranges.")
    
# Filter movies from 2015 to 2017
filtered_movies = movies_df_cleaned[(movies_df_cleaned['Year'] >= 2015) & (movies_df_cleaned['Year'] <= 2017)]

# Calculate the average revenue for the filtered movies
average_revenue_2015_2017 = filtered_movies['Revenue_(Millions)'].mean()

# Display the average revenue
print(f"Average Revenue (2015-2017): {average_revenue_2015_2017} Million")

# Determine the range based on the answer choices
if 100 <= average_revenue_2015_2017 <= 120:
    print("Between 100 and 120 Million")
elif 50 <= average_revenue_2015_2017 <= 80:
    print("Between 50 and 80 Million")
elif average_revenue_2015_2017 > 120:
    print("More than 120 Million")
elif average_revenue_2015_2017 < 40:
    print("Less than 40 Million")
else:
    print("The average revenue does not fall within the provided ranges.")
    

# Count the number of movies released in 2016
movies_2016_count = movies_df_cleaned[movies_df_cleaned['Year'] == 2016].shape[0]

# Display the count
print(f"Number of Movies Released in 2016: {movies_2016_count}")


# Question 6: How many movies were directed by Christopher Nolan?
nolan_movies_count = movies_df_cleaned[movies_df_cleaned['Director'] == 'Christopher Nolan'].shape[0]
print(f"Number of Movies Directed by Christopher Nolan: {nolan_movies_count}")

# Question 7: How many movies in the dataset have a rating of at least 8.0?
high_rated_movies_count = movies_df_cleaned[movies_df_cleaned['Rating'] >= 8.0].shape[0]
print(f"Number of Movies with Rating at Least 8.0: {high_rated_movies_count}")

# Question 8: What is the median rating of movies directed by Christopher Nolan?
nolan_movies_median_rating = movies_df_cleaned[movies_df_cleaned['Director'] == 'Christopher Nolan']['Rating'].median()
print(f"Median Rating of Movies Directed by Christopher Nolan: {nolan_movies_median_rating}")

# Question 9: Find the year with the highest average rating
year_highest_avg_rating = movies_df_cleaned.groupby('Year')['Rating'].mean().idxmax()
print(f"Year with Highest Average Rating: {year_highest_avg_rating}")

# Question 10: What is the percentage increase in the number of movies made between 2006 and 2016?
movies_2006_count = movies_df_cleaned[movies_df_cleaned['Year'] == 2006].shape[0]
movies_2016_count = movies_df_cleaned[movies_df_cleaned['Year'] == 2016].shape[0]
percentage_increase = ((movies_2016_count - movies_2006_count) / movies_2006_count) * 100
print(f"Percentage Increase in Number of Movies (2006 to 2016): {percentage_increase}%")

# Question 11: Find the most common actor in all the movies
most_common_actor = movies_df_cleaned['Actors'].str.split(',').explode().str.strip().mode().iloc[0]
print(f"Most Common Actor in All Movies: {most_common_actor}")

# Question 12: How many unique genres are there in the dataset?
unique_genres_count = movies_df_cleaned['Genre'].str.split(',').explode().str.strip().nunique()
print(f"Number of Unique Genres: {unique_genres_count}")

# Question 13: Do a correlation of the numerical features and provide insights
correlation_matrix = movies_df_cleaned.corr()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print("Correlation Matrix:")
print(correlation_matrix)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Create a correlation plot using seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Plot of Numerical Features")
plt.show()
