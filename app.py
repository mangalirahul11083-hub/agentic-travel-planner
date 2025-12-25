import json
import streamlit as st
from agent.travel_agent import travel_agent

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")

st.title("✈️ Agentic AI Travel Planning Assistant")

# ---- LOAD FLIGHT DATA ----
with open("data/flights.json", "r") as f:
    flights = json.load(f)

source_cities = sorted(set(f["from"] for f in flights))
destination_cities = sorted(set(f["to"] for f in flights))

# ---- USER INPUT ----
source = st.selectbox("Source City", source_cities)
destination = st.selectbox("Destination City", destination_cities)
days = st.number_input("Number of Days", min_value=1, max_value=7, step=1)

# ---- GENERATE PLAN ----
if st.button("Generate Travel Plan 🚀"):
    if source == destination:
        st.error("Source and Destination cannot be the same.")
    else:
        with st.spinner("Planning your trip..."):
            result = travel_agent(source, destination, days)

        if result is None:
            st.error("❌ No valid travel plan found for this route.")
        else:
            st.success("Trip Plan Generated Successfully!")

            st.subheader("✈️ Flight Selected")
            st.write(result["flight"])

            st.subheader("🏨 Hotel Recommended")
            st.write(result["hotel"])

            st.subheader("🌦️ Weather Forecast")
            for i, temp in enumerate(result["weather"], 1):
                st.write(f"Day {i}: {temp}°C")

            st.subheader("🗺️ Day-wise Itinerary")
            for item in result["itinerary"]:
                st.write(item)

            st.subheader("💰 Budget Breakdown")
            for k, v in result["budget"].items():
                st.write(f"{k.capitalize()}: ₹{v}")
