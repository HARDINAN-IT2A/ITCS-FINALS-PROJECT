#List of countries
Asian_countries = ["Philippines" , "China" , "Japan" , "Taiwan" , "Malaysia"  , "South Korea"]

print("List of countries:", Asian_countries)

print("\nThe first country in the list is:", Asian_countries[0])  #First country in the list
print("The last country in the list is:", Asian_countries[-1]) #Last country in the list

#Adding a new country to the list
Asian_countries.append("Singapore")
print("\nLatest List of countries after adding South Korea:", Asian_countries)

#Removing a country from the list
Asian_countries.remove("China")
print("\nList of countries after removing China:", Asian_countries)

#Sorting the list of countries
Asian_countries.sort()
print("\nSorted List of countries:", Asian_countries)

#Length of the list (how many countries in the list)
print("\nNumber of countries in the list:", len(Asian_countries))

#Checking if a country is in the list
check_country = "Philippines"
if check_country in Asian_countries:
    print(f"\n{check_country} is in the list.")
else:
    print(f"\n{check_country} is not in the list.")