import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_recipe(items, stats, diet_label):

    prompt = f"""
    SYSTEM: You are a World-Class Healthy Gourmet Chef and Clinical Nutritionist.
    
    INGREDIENTS: {', '.join(items)}
    MACROS DETECTED: {stats['calories']} kcal, {stats['protein']}g Protein, {stats['fat']}g Fat, {stats['carbs']}g Carbs.
    DIET GOAL: {diet_label}
    
    TASK:
    1. Create the most NUTRITIOUS recipe possible using these specific ingredients.
    2. Focus on "Slow Cooking" or "Steaming" methods to preserve micronutrients.
    3. Use all spices to enhance metabolism and anti-inflammatory properties.
    
    STRUCTURE:
    - **Dish Name**: Something appetizing and professional.
    - **Nutritional Focus**: Why this meal is the 'best' version for a {diet_label} diet.
    - **Steps**: Clear, professional instructions.
    - **Chef's Pro Tip**: One secret to make it tastier without adding calories.
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4, 
            max_tokens=1000
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"⚠️ Chef's Error: {str(e)}"