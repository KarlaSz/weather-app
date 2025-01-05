# Weather Application API 🌦️

This project is a Python-based weather application that fetches and displays real-time weather data from the [IMGW Public API](https://danepubliczne.imgw.pl/api/data/synop/). The application allows users to view the temperature and measurement time for selected cities in a clean and user-friendly terminal table format.

## Features
- Retrieves real-time weather data from IMGW's synoptic data API.
- Displays weather information for selected cities in a structured ASCII table.
- Easy to configure and extend for additional cities.

## Requirements
- Python 3.x
- Installed Python modules:
  - `requests`
  - `json`
  - `terminaltables`

1. Install required modules with:
   ```bash
    pip install requests terminaltables   

Usage
2. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/weather-api.git

3. Run the script:
    ```bash
    python weather_app.py

4. View the weather data for the selected cities in the terminal.

Customization
5. To add more cities, modify the CITIES list:
    ```bash
    CITIES = ['Warszawa', 'Gdańsk', 'Kraków']

Example Output
```bash
Aplikacja pogodowa 2025
+----------+------------------+-------------+
| Miasto   | Godzina pomiaru | Temperatura |
+----------+------------------+-------------+
| Szczecin | 12:00           | 5.6         |
| Wrocław  | 12:00           | 6.3         |
+----------+------------------+-------------+