import os
from dotenv import load_dotenv
from src.bot.handlers import start_bot

def main():
    load_dotenv()
    start_bot()

if __name__ == "__main__":
    main()
