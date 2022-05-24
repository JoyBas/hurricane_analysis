#!/usr/bin/env python
# coding: utf-8

# In[4]:


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# Convert the value of damages to float while retaining missing data as "Damages not recorded"

conversion = {"M": 1000000,
              "B": 1000000000}
new_damages = []              
def updated_damages(damage):
  for damage in damages:
    if damage == "Damages not recorded":
      new_damages.append(damage)
    elif damage[-1] == "M":
      new_damages.append(float(damage.strip("M")) * conversion["M"])
    elif damage[-1] == "B":
      new_damages.append(float(damage.strip("B")) * conversion["B"])
  return new_damages

# test function by updating damages
updated_damages = updated_damages(damages)
# print(updated_damages)


# Create a dictionary of hurricanes with names as keys and the values are dictionaries containing a key for each piece of data.

def create_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricane = {}
  name_length = len(names)
  for i in range(name_length):
    hurricane[names[i]] = {"Name":names[i],
    "Month":months[i], "Year":years[i], "Max Sustained Wind":max_sustained_winds[i], "Areas Affected":areas_affected[i], "Damage":damages[i], "Death":deaths[i]}
  return hurricane

# Create and view the hurricanes dictionary
hurricane = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# print(hurricane)


# Organizing by Year
# create a new dictionary of hurricanes with year as keys and the values are lists containing a dictionary for each hurricane that occurred in that year.

def hurricane_by_year_dictionary(year):
  hurricanes_by_year = {}
  for name in hurricane:
    current_year = hurricane[name]["Year"]
    current_cane = hurricane[name]
    if current_year not in hurricanes_by_year:
      hurricanes_by_year[current_year] = [current_cane]
    else:
      hurricanes_by_year[current_year].append(current_cane)
  return hurricanes_by_year

# print(hurricane_by_year_dictionary(1924))


# Counting Damaged Areas
# create a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.

# first funtion to combine the sublists of areas_affected into one list 
def areas_affected_list(areas_affected):
  areas = []
  for i in areas_affected:
    areas += i
  return areas

# Passing in areas_affected_list function to most_affected_areas function

def most_affected_areas(area):
  lst2 = {}
  for area in areas_affected_list(areas_affected):
    if area in lst2:
      lst2[area] +=1
    else:
      lst2[area] =1
  return lst2

count_of_damaged_areas = most_affected_areas(areas_affected_list)

# print(count_of_damaged_areas)


# Find the area affected by the most hurricanes, and how often it was hit

def most_affected_area(hurricane):
  max_area = "Central America"
  max_area_count = 0
  for area in count_of_damaged_areas:
    if count_of_damaged_areas[area] > max_area_count:
      max_area = area
      max_area_count = count_of_damaged_areas[area]
  return max_area, max_area_count

most_affected_area = most_affected_area(count_of_damaged_areas)

# print(most_affected_area)


# Find the dealiest hurricane that caused the greatest number of deaths, and how many deaths it caused.

def deadliest_hurricane(hurricane):
  max_area = "Cuba I"
  max_death = 0
  for area in hurricane:
    if hurricane[area]["Death"] > max_death:
      max_death = hurricane[area]["Death"]
      max_area = area
  return max_area, max_death

highest_mortality = deadliest_hurricane(hurricane)

# print(highest_mortality)


# Rate hurricanes by mortality  using mortality_scale where the key is the rating and the value is the upper bound of deaths for that rating.

def mortality_scale_category(hurricane):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  mortality_lst = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}               
  for name in hurricane:
    #print(hurricane[name]["Death"])
    num_deaths = hurricane[name]["Death"]
    if num_deaths == mortality_scale[0]:
      mortality_lst[0].append(hurricane[name])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      mortality_lst[1].append(hurricane[name]["Name"])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      mortality_lst[2].append(hurricane[name])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      mortality_lst[3].append(hurricane[name])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      mortality_lst[4].append(hurricane[name])
    elif num_deaths > mortality_scale[4]:
      mortality_lst[5].append(hurricane[name])
  return mortality_lst

mortality_list = mortality_scale_category(hurricane)
# print(mortality_list)


# Find highest damage inducing hurricane and its total cost

def hurricane_greatest_damage(hurricane):
  max_area = "Cuba I"
  max_damage = 0
  for element in hurricane:
    hurricane_damage = hurricane[element]["Damage"]
    if hurricane_damage == "Damages not recorded":
      continue
    elif hurricane_damage >=  max_damage:
     max_area = hurricane[element]
     max_damage = hurricane_damage
  return max_area, max_damage

hurricane_by_damage = hurricane_greatest_damage(hurricane)
# print(hurricane_by_damage)


# categorize hurricanes in new dictionary with damage severity as key
# Rating Hurricanes by Damage
def damage_scale_category(hurricane):
  damage_scale = {0: 0,
                  1: 100000000,
                  2: 1000000000,
                  3: 10000000000,
                  4: 50000000000}
  hurricanes_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}                
  for element in hurricane:
    damage_amount = hurricane[element]["Damage"]
    if damage_amount == "Damages not recorded":
      hurricanes_by_damage[0].append(hurricane[element])
    elif damage_amount ==  damage_scale[0]:
      hurricanes_by_damage[0].append(hurricane[element])
    elif damage_amount > damage_scale[0] and damage_amount <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricane[element])
    elif damage_amount > damage_scale[1] and damage_amount <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricane[element])
    elif damage_amount > damage_scale[2] and damage_amount <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricane[element])
    elif damage_amount > damage_scale[3] and damage_amount <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricane[element])
    elif damage_amount > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricane[element])
  return hurricanes_by_damage

# print(damage_scale_category(hurricane))


