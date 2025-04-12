import httpx
from config import config

async def get_weather(key: str , city : str = config.CURRENT_CITY):
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q=Engels"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        if response.status_code == 200:
            temperature = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            
            # Определяем комментарий в зависимости от состояния погоды
            if "Clear" in condition or "Sunny" in condition:
                condition_comment = "Ясно и солнечно"
            elif "Cloudy" in condition:
                condition_comment = "Облачно"
            elif "Rain" in condition:
                condition_comment = "Дождливо"
            elif "Snow" in condition:
                condition_comment = "Снег"
            else:
                condition_comment = "Неизвестная погода"

            # Определяем комментарий в зависимости от температуры
            if temperature <= -10:
                comment = "❄️ Смертельный дубак! Надевай пуховик и не забывай про термос! 🥶"
            elif -10 < temperature <= 0:
                comment = "🥶 Прохладненько, не забудь шарф и перчатки! 🧣🧤"
            elif 0 < temperature <= 10:
                comment = "🌬️ Холодновато, но можно выйти на свежий воздух, но оденься теплее! 🧥"
            elif 10 < temperature <= 20:
                comment = "🌤️ Немного прохладно, но уже можно радоваться! Лучше кофту взять! ☕"
            elif 20 < temperature <= 30:
                comment = "🌞 Тепло, но не жарко! Отличная погода для прогулки! 😎"
            else:
                comment = "🔥 Жарковато! Время для пляжа и мороженого! 🏖️🍦"
            
            return f"Погода в Энгельсе: {temperature}°C, {condition_comment}.\n{comment}"
        else:
            return "Не удалось получить информацию о погоде."
        
