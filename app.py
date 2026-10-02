import streamlit as st

# Page Configuration
st.set_page_config(page_title="FitBuddy - AI Fitness Planner", page_icon="🏋️‍♂️", layout="centered")

# Title and Subtitle
st.title("🏋️‍♂️ FitBuddy: AI Fitness Plan Generator")
st.write("Generate personalized workout and diet plans instantly!")

st.divider()

# Input Fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10, max_value=100, value=25)
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=65.0)
    diet_pref = st.selectbox("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"])

with col2:
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
    goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "General Fitness"])

st.divider()

# Generate Button and Output Logic
if st.button("Generate Fitness Plan", use_container_width=True):
    st.success("Here is your personalized Fitness Plan:")
    
    # Workout Section
    st.subheader("🏋️‍♂️ Weekly Workout Routine")
    st.markdown(f"""
    - **Monday / Thursday:** Cardio & Core (30 mins Running/Cycling + Planks for **{goal}**)
    - **Tuesday / Friday:** Strength Training (Bodyweight squats, Push-ups, Dumbbell rows)
    - **Wednesday / Saturday:** Active Recovery & Yoga/Stretching
    - **Sunday:** Rest Day
    """)
    
    st.divider()
    
    # Diet Section
    st.subheader("🥗 Customized Diet Chart")
    if diet_pref == "Vegetarian":
        st.markdown("""
        - **Breakfast:** Oats with nuts and fruit + Protein Smoothie
        - **Lunch:** Brown rice, Lentils (Dal), Mixed vegetable curry, and Salad
        - **Snacks:** Roasted Chana or Green Tea with Almonds
        - **Dinner:** Paneer / Tofu with sauteed vegetables and Roti
        """)
    elif diet_pref == "Non-Vegetarian":
        st.markdown("""
        - **Breakfast:** 3 Egg whites + Whole wheat toast + Fruit
        - **Lunch:** Grilled Chicken breast, Quinoa/Brown rice, and Green veggies
        - **Snacks:** Boiled eggs or Protein Shake
        - **Dinner:** Baked Fish or Chicken salad with soup
        """)
    else: # Vegan
        st.markdown("""
        - **Breakfast:** Chia pudding with almond milk and berries
        - **Lunch:** Chickpea salad with veggies and avocado
        - **Snacks:** Mixed seeds and Green Tea
        - **Dinner:** Lentil soup with tofu and steamed broccoli
        """)