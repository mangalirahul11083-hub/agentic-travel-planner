# ✈️ Agentic AI-Based Travel Planning Assistant

## 📌 Project Overview
The **Agentic AI-Based Travel Planning Assistant** is an intelligent travel planning application that automatically generates a complete trip plan based on user inputs such as source city, destination city, and number of days.

The system follows an **Agentic AI architecture**, where an AI agent autonomously coordinates multiple tools (flight search, hotel recommendation, itinerary planning, weather forecasting, and budget estimation) to produce an optimized travel plan.

The application is implemented using **Python** and **Streamlit**, with real-world JSON datasets.

---

## 🧠 What is Agentic AI?
Agentic AI refers to AI systems that can:
- Break a problem into multiple steps
- Decide which tools to use
- Execute actions autonomously
- Combine results into a final output

In this project, the AI agent acts as a **travel planner** that reasons over available data and generates a structured travel itinerary.

---

## 🚀 Key Features
- Interactive **Streamlit-based UI**
- Dropdown-based city selection (data-driven)
- Cheapest flight selection from dataset
- Budget hotel recommendation
- Day-wise itinerary generation
- Real-time weather forecast using Open-Meteo API
- Automatic budget calculation
- Graceful handling of unavailable routes

---

## 🏗️ Project Architecture
The project follows a **modular architecture**:

- **UI Layer** – Streamlit frontend (`app.py`)
- **Agent Layer** – Central reasoning logic (`agent/travel_agent.py`)
- **Tools Layer** – Individual task-specific tools (`tools/`)
- **Data Layer** – JSON datasets (`data/`)

This separation ensures clean code, scalability, and easy maintenance.

---

## 🛠️ Technologies Used
- Python 3.10+
- Streamlit
- JSON
- Requests
- Open-Meteo Weather API
- GitHub (for deployment)

---

## 📂 Folder Structure
```bash
agentic-travel-planner/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
│
├── agent/
│ ├── travel_agent.py
│ └── init.py
│
├── tools/
│ ├── flight_tool.py
│ ├── hotel_tool.py
│ ├── places_tool.py
│ ├── weather_tool.py
│ ├── budget_tool.py
│ └── init.py
│
├── data/
│ ├── flights.json
│ ├── hotels.json
│ └── places.json
│
└── .gitignore
```
## ▶️ How to Run the Project Locally

### Step 1: Install dependencies
pip install -r requirements.txt

## 🌐 Deployment

The application is deployed using:

GitHub for version control

Streamlit Community Cloud for hosting

The deployment automatically builds the app using requirements.txt and serves app.py as the main entry point.

## 📊 Sample Output

The application generates:

Selected flight details

Recommended hotel

Weather forecast

Day-wise travel itinerary

Budget breakdown (flight, hotel, food & travel)

## ✅ Conclusion

This project successfully demonstrates how Agentic AI systems can autonomously plan complex real-world tasks by coordinating multiple tools. The solution is robust, user-friendly, and suitable for real-world travel planning scenarios. The modular design allows easy extension and scalability.
