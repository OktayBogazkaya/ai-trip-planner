import streamlit as st
import datetime
import pandas as pd
from openai import OpenAI

# Include suggestions for accommodation, popular attractions, and local cuisine.

def generate_trip_suggestion(client, city, arrival_date, departure_date):
    prompt = f"Please generate a detailed itinerary for {city} from {arrival_date} to {departure_date}. Provide a day-by-day itinerary."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful travel planner assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating trip suggestion: {str(e)}"

# Sidebar
st.sidebar.title("AI Travel Planner")
#st.sidebar.subheader("Create your dream travel itinerary in just seconds!")

# Option to input OpenAI API key
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

# Initialize client as None
client = None

if api_key:
    try:
        client = OpenAI(api_key=api_key)
        st.sidebar.success("API key set successfully!")
    except Exception as e:
        st.sidebar.error(f"Error initializing OpenAI client: {str(e)}")

# Main content
st.title("Welcome to AI-Powered Travel Planner!")
st.write("Plan your dream trip with the help of AI. Add your destinations, and get personalized itineraries for you.")

if not api_key:
    st.info("👈 Please enter your OpenAI API key in the sidebar to start generating AI-powered trip plans.")

# Initialize session state for storing cities
if 'cities' not in st.session_state:
    st.session_state.cities = []

# Input form for adding a new city
st.subheader("Add a City to Your Trip")
with st.form("add_city"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        arrival_date = st.date_input("Arrival Date")   
    
    with col2:
        departure_date = st.date_input("Departure Date")
    
    with col3:
        city_name = st.text_input("City Name")

    submit_button = st.form_submit_button("Add Trip")

if submit_button:
    if city_name and arrival_date <= departure_date:
        st.session_state.cities.append({
            "Arrival Date": arrival_date,
            "Departure Date": departure_date,
            "City": city_name
        })

        st.success(f"Added {city_name} to your trip!")
    else:
        st.error("Please enter a valid city name and ensure departure date is not before arrival date.")


# Display current trip plan
if st.session_state.cities:
    st.subheader("Your Trip Plan")

    # Convert list of cities to a DataFrame
    cities_df = pd.DataFrame(st.session_state.cities)

    
    # Display the DataFrame as a table
    st.table(cities_df)
else:
    st.write("No cities have been added yet.")


# Generate AI-powered trip plan button
if st.button("Get My Travel Plan"):
    if not client:
        st.error("Please enter a valid OpenAI API key in the sidebar to use the AI features.")
    elif st.session_state.cities:
        st.subheader("AI-Generated Trip Plan")
        for city in st.session_state.cities:
            st.write(f"## {city['City']}")
            st.write(f"**Duration:** {city['Arrival Date']} to {city['Departure Date']}")
            
            with st.spinner(f"Generating trip suggestions for {city['City']}..."):
                trip_suggestion = generate_trip_suggestion(
                    client,
                    city['City'],
                    city['Arrival Date'].strftime("%Y-%m-%d"),
                    city['Departure Date'].strftime("%Y-%m-%d")
                )
            
            st.write(trip_suggestion)
            st.write("---")
    else:
        st.warning("Please add at least one city to generate a trip plan.")

