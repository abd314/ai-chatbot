# AI Chatbot

This repository contains an AI-powered chatbot designed to provide intelligent and interactive responses. The chatbot is built using Python and integrates with a Redis cache for efficient data handling.

## Features
- AI-driven conversational capabilities
- Caching support with Redis
- Modular and extensible architecture

## Installation

Follow these steps to set up the chatbot on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abd314/ai-chatbot.git
   cd ai-chatbot
   ```

2. **Set up a Python virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

4. **Set up Redis:**
   - Install Redis on your system. For example, on Ubuntu:
     ```bash
     sudo apt update
     sudo apt install redis-server
     ```
   - Start the Redis server:
     ```bash
     sudo service redis-server start
     ```

5. **Run the chatbot:**
   ```bash
   python app/main.py
   ```

## Usage

Once the chatbot is running, you can interact with it via the terminal or integrate it into your application. Customize the AI engine by modifying `app/ai_engine.py`.

## Deployment on Render

You can deploy this chatbot on Render for easy hosting and scalability. Follow these steps:

1. **Create a Render Account:**
   - Sign up at [Render](https://render.com/) if you don’t already have an account.

2. **Create a New Web Service:**
   - In the Render dashboard, click on **New > Web Service**.

3. **Connect Your Repository:**
   - Select the GitHub repository containing this chatbot.

4. **Configure the Service:**
   - Use the following settings:
     - **Environment:** Python 3.x
     - **Build Command:**
       ```bash
       pip install -r requirement.txt
       ```
     - **Start Command:**
       ```bash
       python app/main.py
       ```

5. **Set Up Redis:**
   - Add a Redis instance in Render by creating a new **Redis** service from the dashboard.
   - Note the Redis URL and configure it in your application.

6. **Deploy:**
   - Save the settings and deploy the service. Render will automatically build and start your chatbot.

Once deployed, you can access your chatbot via the URL provided by Render.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the chatbot.
