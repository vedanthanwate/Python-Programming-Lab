# 1.Panda Dataframe reading a file
import pandas as pd

# --- Step 0: Create sample data (Skip this if you already have books.csv) ---
data = {
    'title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'The Hobbit', 'Brave New World'],
    'author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'J.R.R. Tolkien', 'Aldous Huxley'],
    'edition': ['1st', '2nd', '1st', '3rd', '2nd'],
    'pub_year': [1925, 1960, 1949, 1937, 1932],
    'pub_house': ['Scribner', 'J.B. Lippincott', 'Secker & Warburg', 'George Allen', 'Chatto & Windus'],
    'price': [500, 450, 600, 800, 550]
}
pd.DataFrame(data).to_csv('books.csv', index=False)

# --- Main Application ---
df = pd.read_csv('books.csv')

# a) Print the complete report in Tabular form
print("--- Complete Book Report ---")
print(df.to_string())
print("\n")

# b) Print list of available books of a given author
author_name = 'George Orwell'
print(f"--- Books by {author_name} ---")
print(df[df['author'] == author_name])
print("\n")

# c) Print list of available books of a given publishing house
pub_house = 'Scribner'
print(f"--- Books published by {pub_house} ---")
print(df[df['pub_house'] == pub_house])
print("\n")

# d) Print the Titles of cheapest & costliest book available
cheapest = df.loc[df['price'].idxmin(), 'title']
costliest = df.loc[df['price'].idxmax(), 'title']
print(f"Cheapest Book: {cheapest}")
print(f"Costliest Book: {costliest}\n")

# e) Print the list by sorting based on the year of publication
print("--- Books Sorted by Year of Publication ---")
print(df.sort_values(by='pub_year'))


# 2. 5 states
import pandas as pd

# Creating the dataset for 5 states
state_data = {
    'State': ['Maharashtra', 'Rajasthan', 'Goa', 'Uttar Pradesh', 'Sikkim'],
    'Area': [307713, 342239, 3702, 240928, 7096],
    'Population': [112374333, 68548437, 1458545, 199812341, 610577]
}
states_df = pd.DataFrame(state_data)

# a) Print complete information
print("State Information:\n", states_df)

# b) State with largest Area
largest_area = states_df.loc[states_df['Area'].idxmax(), 'State']
print(f"\nState with largest Area: {largest_area}")

# c) State with largest Population
largest_pop = states_df.loc[states_df['Population'].idxmax(), 'State']
print(f"State with largest Population: {largest_pop}")

# d) Mechanism to calculate Population Density (Pop / Area)
states_df['Density'] = states_df['Population'] / states_df['Area']
print("\nData with Population Density:\n", states_df)

# e) State with highest population density
highest_density_state = states_df.loc[states_df['Density'].idxmax(), 'State']
print(f"\nState with highest Population Density: {highest_density_state}")