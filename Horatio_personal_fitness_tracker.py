def calories_per_minute(calories: float, duration: float) -> float:
    if duration <= 0:
        raise ValueError("Duration must be greater than 0")
    return round(calories / duration, 1)


def get_intensity(rate: float) -> str:
    if rate < 5.0:
        return "Low"
    elif rate < 10.0:
        return "Medium"
    else:
        return "High"


# main code area
workout_information = []

print("\nGood day, this is a simple personal fitness tracker app. "
      "It will collect information about your workout and display calories burned.")

for i in range(3):
    i+=1
    print(f"-----------------------------------------Workout{i}-------------------------------------")
    workout = input("\nPlease enter the workout name: ")
    duration = float(input("Please enter workout duration in minutes: "))
    calories = float(input("Please enter total calories burned: "))
    rate = calories_per_minute(calories, duration)
    intensity = get_intensity(rate)

    workout_information.append({
        "workout": workout,
        "duration": duration,
        "calories": calories,
        "rate": rate,
        "intensity": intensity,
    })

    print(f"\nResult: {workout} | {duration} min | {calories} cal | "
          f"{rate} cal/min | Intensity: {intensity}\n")