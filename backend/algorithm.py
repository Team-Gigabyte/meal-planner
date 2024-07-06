from dataclasses import dataclass 

@dataclass 
class DailyLimits:
    calories: float = 2500.0  # change this, then change everything else proportionally
    saturated_fat: float = 20.0
    trans_fat: float = 2.2 
    unsaturated_fat: float = float("NaN")
    cholesterol: float = 300.0 
    sodium: float = 2300.0 
    carbs: float = 275.0
    fiber: float = float("NaN")
    sugar: float = 25.0
    protein: float = 175.0

@dataclass 
class NutritionFacts:
    calories: float 
    saturated_fat: float
    trans_fat: float 
    unsaturated_fat: float 
    cholesterol: float 
    sodium: float 
    carbs: float  # does not include fiber
    fiber: float 
    sugar: float 
    protein: float 
    # vitamins: list[float]
    # minerals: list[float]

    def score(self) -> float:  # lower score is better
        return self.calories + self.saturated_fat * 20 + self.trans_fat * 150 - self.unsaturated_fat * 7 + self.cholesterol / 2 + self.sodium / 2 + self.carbs * 5 - self.fiber * 10 + self.sugar * 40 - self.protein * 20

    @staticmethod
    def violates_limits(meals: list[NutritionFacts]) -> bool: 
        total_calories = sum(meal.calories for meal in meals)
        total_saturated_fat = sum(meal.saturated_fat for meal in meals)
        total_trans_fat = sum(meal.trans_fat for meal in meals)
        total_cholesterol = sum(meal.cholesterol for meal in meals)
        total_sodium = sum(meal.sodium for meal in meals)
        total_carbs = sum(meal.carbs for meal in meals)
        total_sugar = sum(meal.sugar for meal in meals)
 