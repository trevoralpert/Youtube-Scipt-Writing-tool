# <img src="Youtube.jpg" alt="YouTube Script Writing Tool Logo" width="60" style="vertical-align:middle; margin-right:10px;"/> YouTube Script Writing Tool 🎥

A professional Streamlit-based application that empowers creators to generate engaging, SEO-friendly YouTube video scripts. By leveraging OpenAI's language models and DuckDuckGo search results, the app creates optimized video scripts based on user-defined topics, creativity levels, and desired video lengths.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Example Scenarios](#example-scenarios)
- [Contributing](#contributing)
- [License](#license)

## Overview

The YouTube Script Writing Tool is designed to assist YouTube creators in generating high-quality video scripts quickly and efficiently. By combining advanced natural language processing with real-time search engine data, the app provides scripts tailored to specific topics and desired video lengths, all while allowing users to adjust the creativity level for tone and style.

## Features

- 🎬 Generate YouTube video titles and full scripts.
- 🔍 Use DuckDuckGo search data to improve script relevance and depth.
- 🎨 Adjustable creativity levels for varied script tones.
- ⚡ Intuitive Streamlit interface for user-friendly interactions.
- 🔑 Secure API key input for OpenAI access.

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building the web interface.
- **LangChain**: For managing prompts and chains.
- **OpenAI GPT**: For generating video titles and scripts.
- **DuckDuckGo Search**: For enriching script content with search results.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/trevoralpert/Youtube-Scipt-Writing-tool.git
   cd Project\ \#8\ \-\ Youtube\ Script\ Writing\ Tool
   ```
2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up your OpenAI API key:**
   - You will be prompted for your API key in the app sidebar, or you can set it as an environment variable:
     ```bash
     export OPENAI_API_KEY=your_openai_api_key
     ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run st_app2.py
   ```
2. **Open your browser** to the local Streamlit URL (usually http://localhost:8501).
3. **Enter your OpenAI API key** in the sidebar.
4. **Fill in the topic, expected video length, and creativity level.**
5. **Click "Generate Script for me"** to receive a video title, script, and relevant search data.

## Example Scenarios

- **Educational Content:**
  - Topic: "The Science of Sleep"
  - Video Length: 8 minutes
  - Creativity: 0.3 (factual)
- **Entertainment:**
  - Topic: "Top 10 Funniest Cat Moments"
  - Video Length: 5 minutes
  - Creativity: 0.7 (humorous)
- **Product Review:**
  - Topic: "Latest Smartphone Review"
  - Video Length: 10 minutes
  - Creativity: 0.5 (balanced)

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Open a pull request describing your changes.

Please ensure your code follows best practices and is well-documented.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
