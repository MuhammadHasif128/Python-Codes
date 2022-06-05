try:
    height = float(input("Please Enter Your Height: "))
    height2 = height**2
    min_bmi = 18.5
    normal_bmi = 20.7
    max_bmi = 22.9
    recommended_min_weight = min_bmi*height2
    recommended_normal_weight = normal_bmi*height2
    recommended_max_weight = max_bmi*height2
    print(f"Your ideal weight range is between {recommended_min_weight:.2f}kg-"f"{recommended_max_weight:.2f}kg")
except ValueError as str:
    print("Error")
