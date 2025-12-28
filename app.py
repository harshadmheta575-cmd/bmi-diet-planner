from flask import Flask, render_template, request

app = Flask(__name__)










@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    food = request.form['food']

    height = height / 100
    bmi = round(weight / (height * height), 2)

    # ---------------- BMI CATEGORY + NUTRITION ----------------
    if bmi < 18.5:
        category = "Underweight"
        nutrition = {
            "protein": "70–80 g",
            "carbs": "High",
            "fats": "Moderate",
            "fiber": "Moderate",
            "calories": "2500+ kcal"
        }
    elif bmi < 25:
        category = "Normal Weight"
        nutrition = {
            "protein": "55–65 g",
            "carbs": "Balanced",
            "fats": "Moderate",
            "fiber": "High",
            "calories": "2000 kcal"
        }
    elif bmi < 30:
        category = "Overweight"
        nutrition = {
            "protein": "45–55 g",
            "carbs": "Low",
            "fats": "Low",
            "fiber": "High",
            "calories": "1500–1700 kcal"
        }
    else:
        category = "Obese"
        nutrition = {
            "protein": "40–50 g",
            "carbs": "Very Low",
            "fats": "Very Low",
            "fiber": "Very High",
            "calories": "1200–1400 kcal"
        }

    # ---------------- BASE VEG DIET (FOR ALL) ----------------
    weekly_diet = {
        "Monday": {"Breakfast": "Oats / Fruit", "Lunch": "Dal + Rice / Roti", "Dinner": "Vegetables"},
        "Tuesday": {"Breakfast": "Fruit salad", "Lunch": "Rajma / Chickpeas", "Dinner": "Soup"},
        "Wednesday": {"Breakfast": "Sprouts", "Lunch": "Dal + Vegetables", "Dinner": "Paneer / Tofu"},
        "Thursday": {"Breakfast": "Smoothie", "Lunch": "Rice + Dal", "Dinner": "Vegetables"},
        "Friday": {"Breakfast": "Oats", "Lunch": "Quinoa + Vegetables", "Dinner": "Soup"},
        "Saturday": {"Breakfast": "Curd + Fruits", "Lunch": "Dal + Roti", "Dinner": "Vegetables"},
        "Sunday": {"Breakfast": "Fruit + Nuts", "Lunch": "Rice + Rajma", "Dinner": "Vegetables"}
    }

    # ---------------- ADD NON-VEG (CONTROLLED) ----------------
    if food == "nonveg":

        if category == "Underweight":
            weekly_diet["Monday"]["Lunch"] = "Chicken curry + Rice"
            weekly_diet["Tuesday"]["Dinner"] = "Egg omelette"
            weekly_diet["Wednesday"]["Lunch"] = "Fish curry + Rice"
            weekly_diet["Friday"]["Lunch"] = "Chicken + Roti"
            weekly_diet["Sunday"]["Dinner"] = "Boiled eggs"

        elif category == "Normal Weight":
            weekly_diet["Monday"]["Lunch"] = "Grilled chicken + Rice"
            weekly_diet["Wednesday"]["Dinner"] = "Egg omelette"
            weekly_diet["Friday"]["Lunch"] = "Fish + Rice"
            weekly_diet["Sunday"]["Dinner"] = "Boiled eggs"

        elif category == "Overweight":
            weekly_diet["Tuesday"]["Lunch"] = "Grilled fish + Salad"
            weekly_diet["Thursday"]["Dinner"] = "Egg whites"
            weekly_diet["Saturday"]["Lunch"] = "Grilled chicken + Vegetables"

        elif category == "Obese":
            weekly_diet["Wednesday"]["Lunch"] = "Egg whites + Salad"
            weekly_diet["Saturday"]["Dinner"] = "Grilled fish + Vegetables"

    # ---------------- ADVICE ----------------
    if category == "Underweight":
        advice = "Increase calorie intake and focus on strength-building exercises."
    elif category == "Normal Weight":
        advice = "Maintain a balanced diet and consistent lifestyle."
    elif category == "Overweight":
        advice = "Reduce sugar and oily foods and increase physical activity."
    else:
        advice = "Strict calorie control, high fiber intake, and regular exercise are essential."

    # ---------------- LIFESTYLE TIPS ----------------
    lifestyle_tips = [
        "Exercise at least 30 minutes daily",
        "Drink plenty of water",
        "Avoid junk and sugary food",
        "Increase fiber intake",
        "Maintain proper sleep schedule"
    ]

    # ---------------- PROTEIN SOURCES ----------------
    if food == "veg":
        protein_sources = ["Paneer", "Dal", "Chickpeas", "Soybeans", "Tofu", "Milk"]
    else:
        protein_sources = ["Eggs", "Chicken", "Fish (lean)", "Paneer", "Dal"]

    return render_template(
        "result.html",
        bmi=bmi,
        category=category,
        nutrition=nutrition,
        weekly_diet=weekly_diet,
        advice=advice,
        lifestyle_tips=lifestyle_tips,
        protein_sources=protein_sources
    )


@app.route('/team')
def team():
    return render_template('team.html')





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

    