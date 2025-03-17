import streamlit as st

st.set_page_config(
    page_icon = "🔃",
    page_title= "Unit converter",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("UNIT CONVERTER APP📟")
st.markdown("## Convert units of measurement with ease!")
st.write("Select the unit you want to convert from and to, and enter the value you want to be converted.")

value =  st.number_input("Input the value you want to convert:", min_value =0.0, max_value=1000.0, step=0.1, value=0.1)

unit_categories = ["Time","Weight","Distance"]
let = st.selectbox("Select a category", unit_categories, key="category")

def convert_units(value, from_unit, to_unit):
    # Conversion dictionaries for different categories

    conversion_dict = {
        # Distance (Length) conversions
        ("Meters", "Kilometers"): value / 1000,
        ("Meters", "Centimeters"): value * 100,
        ("Meters", "Millimeters"): value * 1000,
        ("Kilometers", "Meters"): value * 1000,
        ("Kilometers", "Centimeters"): value * 100000,
        ("Kilometers", "Millimeters"): value * 1000000,
        ("Centimeters", "Meters"): value / 100,
        ("Centimeters", "Kilometers"): value / 100000,
        ("Centimeters", "Millimeters"): value * 10,
        ("Millimeters", "Meters"): value / 1000,
        ("Millimeters", "Kilometers"): value / 1000000,
        ("Millimeters", "Centimeters"): value / 10,

        # Weight conversions
        ("Grams", "Kilograms"): value / 1000,
        ("Grams", "Pounds"): value / 453.592,
        ("Kilograms", "Grams"): value * 1000,
        ("Kilograms", "Pounds"): value * 2.20462,
        ("Pounds", "Grams"): value * 453.592,
        ("Pounds", "Kilograms"): value / 2.20462,

        # Time conversions
        ("Seconds", "Minutes"): value / 60,
        ("Seconds", "Hours"): value / 3600,
        ("Seconds", "Days"): value / 86400,
        ("Seconds", "Weeks"): value / 604800,
        ("Minutes", "Seconds"): value * 60,
        ("Minutes", "Hours"): value / 60,
        ("Minutes", "Days"): value / 1440,
        ("Minutes", "Weeks"): value / 10080,
        ("Hours", "Seconds"): value * 3600,
        ("Hours", "Minutes"): value * 60,
        ("Hours", "Days"): value / 24,
        ("Hours", "Weeks"): value / 168,
        ("Days", "Seconds"): value * 86400,
        ("Days", "Minutes"): value * 1440,
        ("Days", "Hours"): value * 24,
        ("Days", "Weeks"): value / 7,
        ("Weeks", "Seconds"): value * 604800,
        ("Weeks", "Minutes"): value * 10080,
        ("Weeks", "Hours"): value * 168,
        ("Weeks", "Days"): value * 7,
    }


    if from_unit == to_unit:
       return value
    return conversion_dict.get((from_unit,to_unit),"No conversion is available!")
    


if let == 'Distance':
   convert_from = st.radio("Select the current unit of your value:", ("Meters", "Kilometers", "Centimeters", "Millimeters"), key="distance_from")
   convert_to = st.radio("Select the unit you want to convert to:", ("Meters", "Kilometers","Centimeters","Millimeters"), key="distance_to")
   result = convert_units(value,convert_from, convert_to)

elif let == 'Weight':
   convert_from = st.radio("Select the current unit of your value:", ("Grams", "Kilograms", "Pounds"), key="weight_from")
   convert_to = st.radio("Select the unit you want to convert to:", ("Grams", "Kilograms", "Pounds"), key="weight_to")
   result = convert_units(value,convert_from, convert_to )

else: 
   convert_from = st.radio("Select the current unit of your value:", ("Seconds", "Minutes", "Hours", "Days", "Weeks"), key="time_from")
   convert_to = st.radio("Select the unit you want to convert to:", ("Seconds", "Minutes", "Hours", "Days", "Weeks"), key="time_to")
   result = convert_units(value,convert_from, convert_to)


if isinstance (result, str):
   st.error(result)

else:
   st.success(f"{value} {convert_from} is equal to {result:.2f} {convert_to} 🎈")

st.write("---")  
st.write("Created by Aqsa Iftikhar")
