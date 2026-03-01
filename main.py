from src.vision import get_ingredients
from src.nutrition import fetch_macros
from src.ml_logic import predict_diet
from src.ai_chef import get_recipe

def main(img):
    items = get_ingredients(img)
    stats = fetch_macros(items)
    diet = predict_diet(stats['protein'], stats['fat'], stats['carbs'])
    recipe = get_recipe(items, stats, diet)
    
    print(f"Detected: {items}\nDiet Type: {diet}\n\nRecipe:\n{recipe}")

if __name__ == "__main__":
    main("test.jpg")