# Meta AI Discord Bot

A simple open-source Discord bot with built-in integration for Meta AI, enabling intelligent conversations and image generation. This bot uses Meta's cutting-edge AI technologies to bring advanced capabilities directly to your Discord server.

## Features
- 💬 **Smart Conversations**: Interact with Meta AI for natural, context-aware responses.
- 🎨 **Image Generation**: Create unique images based on user prompts.
- ⚡ **Easy Integration**: Simple setup to get started quickly.

## Installation

### Prerequisites
- Python 3.8 or higher
- A Discord bot token ([How to get one](https://discord.com/developers/applications))
- Meta AI API key (from Meta's developer platform)
- `pip` for package management

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/RebeloSebasstien/Discord-Meta-AI.git
   cd Discord-Meta-AI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add the following:
   ```
   DISCORD_TOKEN= your-discord-bot-token
   ```

4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage
- **Chat with Meta AI**: Use the `!ask` command followed by your question or message.
  ```
  !ask What is the capital of France?
  ```
- **Generate Images**: Use the `!generate` command with a creative prompt.
  ```
  !generate A futuristic city at sunset
  ```

## File Structure
```
meta-ai-discord-bot/
│
├── main.py
├── actions.py
├── decorators.py
├── errors.py
├── processing.py
├── sharedfuncs.py
├── start.py              # Start bot script
├── main.py              # Main bot script
├── requirements.txt      # Dependencies
├── .env                  # Environment variables (add this manually)
└── README.md             # Documentation
```

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
