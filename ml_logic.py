def classify_diet_accurately(protein, fat, carbs):
    total_cal = (protein * 4) + (fat * 9) + (carbs * 4)
    if total_cal == 0: return "Balanced"
    
    p_ratio = (protein * 4) / total_cal
    c_ratio = (carbs * 4) / total_cal

    if c_ratio < 0.20: return "Keto Friendly"
    if p_ratio > 0.25: return "High Protein"
    if c_ratio > 0.55: return "High Carb"
    return "Balanced Healthy"