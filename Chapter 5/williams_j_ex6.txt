def calculateCaloriesFromFat(fatGrams):
    caloriesFromFat = fatGrams * 9
    return caloriesFromFat

def calculateCaloriesFromCarbs(carbGrams):
    caloriesFromCarbs = carbGrams * 4
    return caloriesFromCarbs

def main():
    userFatGrams = float(input("Enter fat grams: "))
    userCarbGrams = float(input("Enter carbohydrates grams: "))

    caloriesFromFat = calculateCaloriesFromFat(userFatGrams)
    caloriesFromCarbs = calculateCaloriesFromCarbs(userCarbGrams)

    print("\nCalories from Fat: " + format(caloriesFromFat, ".2f") + \
          "calories", "Calories from Carbs: " + \
          format(caloriesFromCarbs, ".2f") + "calories", sep="\n")

main()
