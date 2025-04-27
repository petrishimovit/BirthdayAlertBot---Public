# BirthdayBot

**BirthdayBot** is a Telegram bot for the group that automates birthday greetings for members. The bot checks daily for upcoming birthdays and sends congratulatory messages with photos.

## 📄 Description

BirthdayBot automatically checks for upcoming birthdays and sends congratulatory messages to the group chat. It allows adding new people to the database, including their name, surname, birthdate, and photo, which are then used for future birthday checks.

## 🚀 Core Features

### ✅ Automated Birthday Check
- The bot checks for upcoming birthdays every day.
- On a member’s birthday, the bot sends a congratulatory message to the group chat, attaching a photo (if provided).

### ✅ Adding a New Person
- Through an FSM form, users can add a new person to the database.
  - The user provides the name, surname, birthdate, and uploads a photo.
  - The data is saved in a AISQLite database for future checks.

### ✅ Date Format Validation
- Birthdate input must follow the **YYYY-MM-DD** format, with proper validation to ensure correct input.

### ✅ AISQLite Support
- All data is stored in a AISQLite database, ensuring safe storage of user information.
- SQLAlchemy is used to interact with the database.

### ✅ Docker Support
- The project supports Docker and Docker Compose for easy deployment.
- **Docker Compose** ensures the app restarts automatically in case of failure.

## 🔧 Tech Stack
- **Python 3.13.1**
- **Aiogram** — for working with the Telegram API.
- **SQLAlchemy** — for interacting with the database.
- **AISQLite** — the database for storing user data.
- **Docker** — for containerization of the app.

## 🛠 Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/petrishimovit/BirthdayAlertBot---Public
   cd your-project
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables or configuration files for Telegram API, database, and other settings.

4. Run the project with Docker Compose:

   ```bash
   docker-compose up -d
   ```

   The bot will automatically restart in case of failure.

## ⚙️ Project Structure

```
.
├── bot/
│   ├── main.py 
│   ├── loader.py
│   ├── config.py # Pydantic-Settings config
│   ├── handlers/ 
│       ├── keyboards/
│       ├── rotes/
│       ├── states/               
│   ├── utils                     
│   └── database/ 
├── Dockerfile                # Docker configuration
├── docker-compose.yml        # Docker Compose configuration
├── requirements.txt          
└── README.md                 
```

## 📝 Notes
- To use the Telegram bot, make sure to configure your `bot_token` in the configuration.
- To connect to the database, set up connection parameters in the `docker-compose.yml` file or a separate configuration file.

---
