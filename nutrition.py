import pandas as pd
from difflib import get_close_matches

def fetch_macros(ingredients):
    try:
       
        df = pd.read_csv('data/raw/global_nutrition.csv')
    except FileNotFoundError:
        print("Error: data/raw/nutrition.csv not found.")
        return {"calories": 0, "protein": 0, "fat": 0, "carbs": 0, "found": []}

    total = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0, "found": []}
    
    for item in ingredients:
        
        match = get_close_matches(item.lower(), df['food_name'].str.lower().tolist(), n=1, cutoff=0.3)
        
        if match:
           
            row = df[df['food_name'].str.lower() == match[0]].iloc[0]
            
            total["calories"] += float(row['calories'])
            total["protein"] += float(row['protein_g'])
            total["fat"] += float(row['fat_g'])
            total["carbs"] += float(row['carbs_g'])
            total["found"].append(match[0].capitalize())
            
    return total