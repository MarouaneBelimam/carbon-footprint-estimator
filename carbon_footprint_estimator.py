# Carbon Footprint Estimator (Weekly)
# Author: [Marouane Belimam]
# Description: Estimates weekly CO2 emissions from  driving, flights, meals, and package deliveries


CAR_EMISSION_PER_KM = 0.2         # kg CO2 per km
FLIGHT_EMISSION = 250             # kg CO2 per short flight
MEAT_MEAL_EMISSION = 7.0          # kg CO2 per meat meal
VEG_MEAL_EMISSION = 1.7           # kg CO2 per veg meal
PACKAGE_EMISSION = 0.5            # kg CO2 per delivery

dis1 = input("Please enter how many kilometers did you drive this week:")
dis2 = input("Please enter how many short flight (<3hours) this week:")
meal1 = input("Please enter how many meat-based meals did you eat this week:")
meal2 = input("Please enter how many vegetarian meals did you eat this week:")
deli = input("Please enter how many packages did you receive this week:")
try:
    dis_1 = float(dis1)
    dis_2 = float(dis2)
    meal_1 = float(meal1)
    meal_2 = float(meal2)
    deli_ = float(deli)

    tot1 = dis_1*CAR_EMISSION_PER_KM 
    tot2 = dis_2*FLIGHT_EMISSION
    tot3 = meal_1*MEAT_MEAL_EMISSION
    tot4 = meal_2*VEG_MEAL_EMISSION
    tot5 = deli_*PACKAGE_EMISSION
    tot = tot1 + tot2 + tot3 + tot4 + tot5

    print(f"The total carbon emissions is {tot} kg CO2e")
    if tot <= 50:
        rating = "Low footprint - Well done!"
        print("Low footprint - Well done!")
    elif tot <= 100:
        rating = "Medium footprint - room for improvement"
        print("Medium footprint - room for improvement")
    else:
       rating = "High footprint - try to reduce your emissions"
       print("High footprint - try to reduce your emissions")
        
    with open("Carbon_emissions_results.txt", "w") as f:
        f.write("   Personal Carbon Footprint Report (Weekly)\n")
        f.write(f"Distance driven: {dis_1}km\n")
        f.write(f"Short flights: {dis_2}\n")
        f.write(f"Meat-based meals: {meal_1}\n")
        f.write(f"Vegetarian meals: {meal_2}\n")
        f.write(f"Packages received: {deli_}\n")
        f.write("\n")
        f.write("  -------------------------   \n")
        f.write("\n")
        f.write(f"Your total carbon emissions are: {tot} kg CO2e")
        f.write(f"\n{rating}\n")

except: 
    print("Please enter a valid number")
    quit()
    
    

print("All Done Thank You!")
     


