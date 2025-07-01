import os
from src.bot.handlers import start_bot

def main():
    start_bot()

if __name__ == "__main__":
    main()

# Порт для Railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    start_bot()
