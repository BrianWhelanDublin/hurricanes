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

# write your update damages function here:
def updated_damages(lst):
  new_damages_lst=[]
  for item in lst:
    if item == "Damages not recorded":
      new_damages_lst.append(item)
    if item[-1] == "M":
      new_damages_lst.append(float(item[:-1]) * (10 ** 6))
    if item[-1] == "B":
      new_damages_lst.append(float(item[:-1])*(10**8))
  return new_damages_lst

#print(updated_damages(damages)) 
updated_damages_data = updated_damages(damages)
# write your construct hurricane dictionary function here:

def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages_data, deaths):
    hurricanes_dic={}
    number_of_hurricanes = len(names)
    for i in range(number_of_hurricanes):
        hurricanes_dic[names[i]]={"Name": names[i], 
                                 "Month": months[i], 
                                 "Year": years[i], 
                                 "Max sustained winds": max_sustained_winds[i], 
                                 "Areas affected": areas_affected[i],
                                 "Updated Damages": updated_damages_data[i],
                                 "Deaths": deaths[i]}
    return hurricanes_dic

new_hurricanes_dic= hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages_data, deaths)
#print(hurricane_dictionary(names ,months, years, max_sustained_winds, areas_affected, updated_damages_data, deaths))

# write your construct hurricane by year dictionary function here:
def create_hurricanes_by_year(hurricanes):
    hurricanes_by_year = {}
    for hur in hurricanes:
        current_year = hurricanes[hur]["Year"]
        current_cane = hurricanes[hur]
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [current_cane]
        else:
            hurricanes_by_year[current_year].append(current_cane)
    return hurricanes_by_year
#print(create_hurricanes_by_year(new_hurricanes_dic))


# write your count affected areas function here:
def count_affected_areas(hurricanes):
    affected_area_count={}
    for hurr in hurricanes:
        for area in hurricanes[hurr]["Areas affected"]:
            if area not in affected_area_count:
                affected_area_count[area] =1
            else:
                affected_area_count[area]+=1
    return affected_area_count


affected_areas = count_affected_areas(new_hurricanes_dic)

# write your find most affected area function here:
def find_worst_hit_area(areas):
    max_area= "Cuba"
    max_area_count = 0
    for area in areas:
        if areas[area]> max_area_count:
            max_area= area
            max_area_count = areas[area]
    return max_area, max_area_count   

max_area, max_area_count =find_worst_hit_area(affected_areas)
#print(max_area, max_area_count)

# write your greatest number of deaths function here:
def find_most_deaths(hurricanes):
    max_deaths_hurricane=""
    max_death_count=0
    for hurr in hurricanes:
        if hurricanes[hurr]["Deaths"]> max_death_count:
            max_deaths_hurricane = hurr
            max_death_count = hurricanes[hurr]["Deaths"]
    return max_deaths_hurricane, max_death_count
    
max_deaths_hurricane, max_death_count = find_most_deaths(new_hurricanes_dic)
#print(max_deaths_hurricane, max_death_count)

# write your catgeorize by mortality function here:
def catgeorize_by_mortality(hurricanes):
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for hurr in hurricanes:
        deaths= hurricanes[hurr]["Deaths"]
        if deaths ==0:
            hurricanes_by_mortality[0].append(hurricanes[hurr])
        elif deaths > 0 and deaths <= 100:
            hurricanes_by_mortality[1].append(hurricanes[hurr])
        elif deaths > 100 and deaths <= 500:
            hurricanes_by_mortality[2].append(hurricanes[hurr])
        elif deaths > 500 and deaths <= 1000:
            hurricanes_by_mortality[3].append(hurricanes[hurr])
        elif deaths > 1000 and deaths <= 10000:
            hurricanes_by_mortality[4].append(hurricanes[hurr])
        else:
            hurricanes_by_mortality[5].append(hurricanes[hurr])
    return hurricanes_by_mortality

#print(catgeorize_by_mortality(new_hurricanes_dic))

# write your greatest damage function here:

def find_most_damage(hurricanes):
    max_damage_hurricane=""
    max_damage_count=0
    for hurr in hurricanes:
        if hurricanes[hurr]["Updated Damages"] == "Damages not recorded":
            pass
        elif hurricanes[hurr]["Updated Damages"]> max_damage_count:
            max_damage_hurricane = hurr
            max_damage_count = hurricanes[hurr]["Updated Damages"]
    return max_damage_hurricane, max_damage_count

max_damage_hurricane, max_damage_count = find_most_damage(new_hurricanes_dic)

#print(max_damage_hurricane, max_damage_count)




# write your catgeorize by damage function here:
def catgeorize_by_damage(hurricanes):
    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for hurr in hurricanes:
        damages= hurricanes[hurr]["Updated Damages"]
        if damages == "Damages not recorded":
            hurricanes_by_damage[0].append(hurricanes[hurr])
        elif damages == 0:
            hurricanes_by_damage[0].append(hurricanes[hurr])
        elif damages <= 100000000:
            hurricanes_by_damage[1].append(hurricanes[hurr])
        elif damages > 100000000 and damages <= 1000000000:
            hurricanes_by_damage[2].append(hurricanes[hurr])
        elif damages > 1000000000 and damages <= 10000000000:
            hurricanes_by_damage[3].append(hurricanes[hurr])
        elif damages > 10000000000 and damages <= 100000000000:
            hurricanes_by_damage[4].append(hurricanes[hurr])
        else:
            hurricanes_by_damage[5].append(hurricanes[hurr])
    return hurricanes_by_damage

print(catgeorize_by_damage(new_hurricanes_dic))


