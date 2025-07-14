# Weather Bot

A Django-based chatbot web application that provides weather information and suggests nearby beaches using OpenAI and OpenWeather APIs.

## Features

- **Chatbot Interface:** Simple web UI for chatting with the bot.
- **Weather Info:** Get current weather for any location. Obtained from openweathermap
- **Beach Suggestions:** Get suggestions for beaches near a given location.
- **OpenAI Integration:** Uses OpenAI's GPT models, gpt-4o-mini, for intelligent responses.
- **Environment Variables:** API keys and secrets managed securely via `.env` file.

## Setup

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd weather_bot
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the project root:
   ```
   OPEN_WEATHER_KEY=your_openweather_api_key
   OPENAI_KEY=your_openai_api_key
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

6. **Access the app:**  
   Open [http://localhost:8000/](http://localhost:8000/) in your browser.

## Project Structure

- `weather_bot/` – Django project settings and URLs
- `bot/` – Main app with views, agent logic, and templates
- `bot/agent/wagent.py` – Agent logic for weather and beach queries
- `templates/main.html` – Chatbot UI

## Testing

Run tests with:
```sh
python manage.py test bot
```

## Environment Variables

All sensitive keys are loaded from `.env` using `django-environ`.

## License

None

---

**Author:** Juan Barragan 
**Contact:** juan@barragan.fr