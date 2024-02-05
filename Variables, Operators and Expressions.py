# CONCEPTUAL EXPLANATION:
# Variables:
age = 25  
distance = 10  
# Operators:
result_addition = 5 + 3  
result_subtraction = 10 - 4  
result_multiplication = 2 * 6

is_equal = result_addition == result_subtraction
# Expressions:
total_cost = quantity * price 
# LOGICAL BREAKDOWN:
# variable naming:
num_apples = 10  
total_apples = 10 
# Operator Precedence:
result = 3 + 5 * 2  

result_with_parentheses = (3 + 5) * 2
# Expression Evaluation:
result = 3 + 5 * 2  

result_with_parentheses = (3 + 5) * 2 
# REAL LIFE PROBLEMS: 
# Task no 1
# Fitness Tracker App:
daily_steps = 8000  
distance_walked = 5.2  
calories_burned = 400  

average_steps_per_week = (7 * daily_steps) / 7
total_distance_in_month = 30 * distance_walked

print("Fitness Tracker Results:")
print("Average Steps Per Week:", average_steps_per_week)
print("Total Distance Covered in a Month (km):", total_distance_in_month)
# Task no 2
# Shopping List:
item_names = ["upper", "jacket", "hoodie", "sneakers"]  
quantities = [3, 5, 2, 1]  
prices = [1.2, 0.5, 2.0, 2.5] 
budget = 15.0 

total_cost = sum(quantity * price for quantity, price in zip(quantities, prices))

enough_budget = total_cost <= budget

print("Shopping List Results:")
print("Item Names:", item_names)
print("Quantities:", quantities)
print("Prices per Item:", prices)
print("Total Cost:", total_cost)
print("Enough Budget:", enough_budget)
# Task no 3
# Recipe Calculator:
recipe_ingredients = ["rice", "mutton", "yougurt", "biryani masala"]  
ingredient_amounts = [2.5, 1.5, 3, 2]  
number_of_servings = 4  

adjusted_quantities = [amount * number_of_servings for amount in ingredient_amounts]

print("Recipe Calculator Results:")
print("Recipe Ingredients:", recipe_ingredients)
print("Amounts per Serving:", ingredient_amounts)
print("Number of Servings:", number_of_servings)
print("Adjusted Quantities:", adjusted_quantities)
# Task no 4
# Movie Recomendation System:
user_genre_preference = "Action"  
user_rating_preference = 8.0  
user_release_year_preference = 2010  

movies = [
    {"title": "robby the robot", "genre": "Sci-Fi", "rating": 8.8, "release_year": 2010},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "release_year": 2006},
    {"title": "tare zameen per", "genre": "Action", "rating": 7.8, "release_year": 2008},
    {"title": "12th fail", "genre": "Sci-Fi", "rating": 8.6, "release_year": 2023},
]

recommended_movies = [
    movie["title"] for movie in movies
    if movie["genre"] == user_genre_preference
    and movie["rating"] >= user_rating_preference
    and movie["release_year"] >= user_release_year_preference
]

print("Movie Recommendation System Results:")
print("User Genre Preference:", user_genre_preference)
print("User Rating Preference:", user_rating_preference)
print("User Release Year Preference:", user_release_year_preference)
print("Recommended Movies:", recommended_movies)
# Task no 5
# Time Management Tool:
task_names = ["exercise", "study", "Reading", "Social Media"]  
task_durations = [2.5, 1.0, 1.5, 1.5]  

total_time_per_task = dict(zip(task_names, task_durations))

areas_for_improvement = sorted(total_time_per_task.items(), key=lambda x: x[1])

print("Time Management Tool Results:")
print("Task Names:", task_names)
print("Task Durations (hours):", task_durations)
print("Total Time Spent on Each Task:", total_time_per_task)
print("Areas for Improvement (tasks to spend more time on):", areas_for_improvement)