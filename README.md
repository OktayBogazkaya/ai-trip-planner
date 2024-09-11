# AI Travel Planner

AI Travel Planner is a Streamlit-based web application that uses OpenAI's API to generate personalized travel itineraries. Users can input their travel destinations and dates to receive detailed trip plans, including suggestions for accommodation, popular attractions, and local cuisine.

## Features

- **Generate Itinerary:** Get personalized travel plans based on your inputs (cities, arrival, and departure date).

## Requirements

To run the script, you need the following Python libraries:

- streamlit==1.23.1
- openai==0.27.0

## How to Use

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/ai-travel-planner.git
    cd ai-travel-planner
    ```

2. **Create a Virtual Environment (Optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit App:**

    ```bash
    streamlit run app.py
    ```

5. **Enter Your OpenAI API Key:**

   Open the app in your browser and enter your OpenAI API key in the sidebar.

6. **Add Cities and Dates:**

   Use the form to input cities, arrival, and departure dates.

7. **Generate Your Trip Plan:**

   Click on "Generate AI-Powered Trip Plan" to receive detailed itineraries for your specified cities.

## Troubleshooting

- **API Initialization Errors:** Ensure your OpenAI API key is correctly entered.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

If you have any questions or suggestions, feel free to contact me at [@RhinoInsight](https://x.com/RhinoInsight).