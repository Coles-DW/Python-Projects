##Background
The Nobel Prize has been among the most prestigious international awards since 1901. Each year, awards are bestowed in chemistry, literature, physics, physiology or medicine, economics, and peace. In addition to the honor, prestige, and substantial prize money, the recipient also gets a gold medal with an image of Alfred Nobel (1833 - 1896), who established the prize.



The Nobel Foundation has made a dataset available of all prize winners from the outset of the awards from 1901 to 2023. The dataset used in this project is from the Nobel Prize API and is available in the nobel.csv file in the data folder.

In this project, you'll get a chance to explore and answer several questions related to this prizewinning data. And we encourage you then to explore further questions that you're interested in!

##Questions
Analyze Nobel Prize winner data and identify patterns by answering the following questions:

What is the most commonly awarded gender and birth country?

Store your answers as string variables top_gender and top_country.
Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?

Store this as an integer called max_decade_usa.
Which decade and Nobel Prize category combination had the highest proportion of female laureates?

Store this as a dictionary called max_female_dict where the decade is the key and the category is the value. There should only be one key:value pair.
Who was the first woman to receive a Nobel Prize, and in what category?

Save your string answers as first_woman_name and first_woman_category.
Which individuals or organizations have won more than one Nobel Prize throughout the years?

Store the full names in a list named repeat_list.

##Solution
# Step 1 — Load the data
# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Load dataset
nobel = pd.read_csv("data/nobel.csv")

# Quick inspection (optional)
nobel.head()

#Step 2 — Most commonly awarded gender and birth country
# Most common gender
top_gender = nobel["sex"].value_counts().idxmax()

# Most common birth country
top_country = nobel["birth_country"].value_counts().idxmax()

top_gender, top_country

('Male', 'United States of America')

#Step 3 — Decade with highest ratio of US-born winners
# Create decade column
nobel["decade"] = (nobel["year"] // 10) * 10

# Identify US-born laureates
nobel["usa_born"] = nobel["birth_country"] == "United States of America"

# Compute ratio per decade
usa_ratio = nobel.groupby("decade")["usa_born"].mean()

# Find decade with highest ratio
max_decade_usa = int(usa_ratio.idxmax())

max_decade_usa

(2000)

#Step 4 — Decade & category with highest proportion of female laureates
# Indicator for female
nobel["female"] = nobel["sex"] == "Female"

# Proportion of females by decade and category
female_ratio = (nobel.groupby(["decade", "category"])["female"].mean())

# Find max combinations
max_index = female_ratio.idxmax()

# Store as dictionary with decade as the key and the category as the value
max_female_dict = {int(max_index[0]): max_index[1]}

max_female_dict

{2020: 'Literature'}

#Step 5 — First woman to receive a Nobel Prize
# Filter to female laureates and sort by year
first_woman = (nobel[nobel["sex"] == "Female"].sort_values("year")).iloc[0]

first_woman_name = first_woman["full_name"]
first_woman_category = first_woman["category"]

first_woman_name, first_woman_category 
('Marie Curie, née Sklodowska', 'Physics')

#Step 6 — Individuals / organizations who won more than once
# Count prizes per full name
name_counts = nobel["full_name"].value_counts()

# Names appearing more than once
repeat_list = name_counts[name_counts > 1].index.tolist()

repeat_list
['Comité international de la Croix Rouge (International Committee of the Red Cross)',
 'Linus Carl Pauling',
 'John Bardeen',
 'Frederick Sanger',
 'Marie Curie, née Sklodowska',
 'Office of the United Nations High Commissioner for Refugees (UNHCR)']
