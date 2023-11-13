# Julie Zhu
# Nov. 6, 2023
# Homework 2

# QUESTION 1
# What is the user's year of birth
user_year_of_birth = int(input("What is your year of birth?"))

# Calculate the user's current age
current_year = 2023
user_age = current_year - user_year_of_birth
print("You were born in the year," (user_year_of_birth))
print("You are," (user_age), "years old.")

# QUESTION 2
# How many times the user's heart has beaten
average_beat_of_human= 75  # beats per minute
user_heartbeats = user_age * 365 * 24 * 60 * (average_beat_of_human)
print ("The user's heart has beaten", round (user_heartbeats, 2), "times")

# QUESTION 3
# How many times a blue whale's heart has beaten
average_beat_of_blue_whale = 33 #beats per minute
blue_whale_heartbeats = age * 365 * 24 * 60 * (average_beat_of_blue_whale)
print ("The blue whale's heart has beaten", round (blue_whale_heartbeats, 2), "times")

# QUESTION 4
# How many times a rabbit's heart has beaten
average_beat_of_rabbit = 180 #beats per minute
rabbit_heartbeats = age * 365 * 24 * 60 * (average_beat_of_rabbit)

# Check if rabbit heartbeats are more than a billion
if rabbit_heartbeats > 1_000_000_000:
    print ("A rabbit's heart has beaten", round (rabbit_heartbeats / 1_000_000_000, 2), "billion times")
else:
    print ("A rabbit's heart has beaten", round (rabbit_heartbeats, 2), "times")

# QUESTION 5
# How many times a rabbit's heart has beaten
rabbit_heart_rate = 180  # Beats per minute
rabbit_heartbeats = age * 365 * 24 * 60 * (rabbit_heart_rate)

# Check if rabbit heartbeats are more than a billion with f-string
if rabbit_heartbeats > 1_000_000_000:
    rabbit_heartbeats_fstring= f"{rabbit_heartbeats / 1_000_000_000:.1f} billion"
else:
    rabbit_heartbeats_fstring = f"{rabbit_heartbeats:,}"
print(f"In that time, a rabbit's heart has beaten {rabbit_heartbeats_fstring} times.")

# Pros and cons of using f-string
# Pros: 1) F-string is generally more concise, readable, and clear. I can directly embed variebles and functions in it. 
#       2) F-string allows for various format specifiers to give users a great control of how they want data to be presented.
# Cons: 1) F-string is not available/compatible in/with old Python versions. 

# Pros and cons of using commas
# Pros: 1) Commas are compatible with both old and new Python versions.
#       2) I think it is easy to learn/understand for new beginners of coding. 
# Cons: 1) Commas doesn't allow users to easily specify formatting like decimal decisions or other options. 
#       2) Using multiple commas to show large numbers would make the numbers less readable. 

# Note: I used Google and ChatGPT for a more complete answer in terms of the pros and cons question (because I haven't got enough personal experiences yet). 

# QUESTION 6
# What is the user's year of birth
user_year_of_birth = int(input("What is your year of birth?"))

# What is my year of bith
my_year_of_birth = 2001

# Calculate the user's and my age
current_year = 2023
user_age = current_year - user_year_of_birth
my_age = current_year - my_year_of_birth

# Compare the user's age with mine
if user_age == my_age:
    print ("You and the user are at the same age")
elif user_age > my_age:
    print ("The user is", (user_age - my_age), "years older than you")
else:
    print ("The user is", (my_age - user_age), "years younger than you")

# Determine if the user was born in a odd or even year
if user_age % 2 == 0:
    print ("The user was born in an even year")
else:
    print ("The user was born in a odd year")

# QUESTION 7
# When is the user's year of birth
user_year_of_birth = int(input("What is your year of birth?"))

# US Presidents since 1980 and their party affiliation
US_presidents_since_1980 = {
    1980: "Democratic",  # Jimmy Carter
    1981: "Republican",  # Ronald Reagan
    1989: "Republican",  # George H.W. Bush
    1993: "Democratic",  # Bill Clinton
    2001: "Republican",  # George W. Bush
    2009: "Democratic",  # Barack Obama
    2017: "Republican",  # Donald Trump
    2021: "Democratic",  # Joe Biden
}

# The number of times a Democratic President has been in office since the user's birth
democratic_presidents_count = sum(1 for year, party in US_presidents_since_1980.items() if year >= user_year_of_birth and party == "Democratic")
print ("There were", (democratic_presidents_count), "times a Democratic President has been in office since your birth")

# QUESTION 8
# Mapping years to U.S. Presidents from 1980 onward
presidents_since_1980 = {
    1980: "Jimmy Carter",
    1981: "Ronald Reagan",
    1989: "George H.W. Bush",
    1993: "Bill Clinton",
    2001: "George W. Bush",
    2009: "Barack Obama",
    2017: "Donald Trump",
    2021: "Joe Biden",
}

# What is the user's year of birth
user_year_of_birth = int(input("What is your year of birth?"))

# Check if the user's birth year is in the dictionary
if user_year_of_birth in presidents_since_1980:
    president_in_office = presidents_since_1980[user_year_of_birth] #the "key" to retrieve President's name from the dictionary
    print ("The U.S. President in office when you were born in", (user_year_of_birth), "was", (president_in_office))
else:
    # Find the closest previous year with a President in office
    previous_years = [year for year in presidents_since_1980.keys() if year <= user_year_of_birth]
    closest_year = max(previous_years)  # Find the largest year that is less than or equal to the user's birth year
    president_in_office = presidents_since_1980[closest_year]
    print ("The U.S. President in office closest to your birth year was", (president_in_office))

# QUESTION 9
# Honestly, I didn't find another way to do questions 7 and 8. 
# I was trying to use the if statements and the count function to find out the solutions for these two questions.
# I was trying something like "if year >= user_year_of_birth and party == 'Democratic':" then using count. But I didn't make it.
# So I googled and asked ChatGPT some questions to figure out the solutions (and now I understand the codes).

# QUESTION 10
current_year = 2023
user_year_of_birth = int(input("What is your year of birth?"))
if user_year_of_birth <= current_year:
    break  # If the year is not in the future, then exiting the loop
else:
    print ("You can't be born in a future year. Please enter a valid year of birth.")


