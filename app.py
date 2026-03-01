import streamlit as st
import PIL.Image
from src.vision import get_ingredients
from src.nutrition import fetch_macros
from src.ml_logic import classify_diet_accurately
from src.ai_chef import get_recipe

st.set_page_config(page_title="NutriGen AI", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: white; padding: 15px; border-radius: 12px; border: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

st.title("🥗 NutriGen: Universal Smart Nutritionist")

uploaded_file = st.file_uploader("Upload an image of ingredients", type=['jpg', 'png'])

if uploaded_file:
    img = PIL.Image.open(uploaded_file)
    st.image(img, width=450)
    with open("temp.jpg", "wb") as f: f.write(uploaded_file.getbuffer())
    
    with st.spinner("Analyzing Image..."):
        detected = get_ingredients("temp.jpg")
    
    confirmed = st.multiselect(
        "AI found these items. Please confirm or add more:",
        options=list(set(detected + ["Paneer", "Rice", "Broccoli", "Chicken", "Lentils", "Spinach","cheese","milk","yogurt","tomato","beans",
                                     "fruits"])),
        default=detected
    )

    if st.button("Generate Best Health Recipe"):
        if not confirmed:
            st.warning("Please select at least one ingredient.")
        else:
   
            stats = fetch_macros(confirmed)
            diet = classify_diet_accurately(stats['protein'], stats['fat'], stats['carbs'])
           
            recipe = get_recipe(confirmed, stats, diet)
           
            st.divider()
            st.subheader(f"Optimal Diet: {diet}")
            
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Calories", f"{stats['calories']} kcal")
            c2.metric("Protein", f"{stats['protein']}g")
            c3.metric("Fats", f"{stats['fat']}g")
            c4.metric("Carbs", f"{stats['carbs']}g")
            
            st.markdown("---")
            st.markdown("### 👨‍🍳 Master Chef's Nutritional Recipe")
            st.write(recipe)