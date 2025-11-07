# AI Research Assistant

A Python-based AI research assistant powered by LangChain and Google's Gemini model. This tool leverages advanced language models to perform web searches, query Wikipedia, and save research outputs to files, making it an efficient companion for gathering and organizing information.

## Features

- **Web Search**: Utilizes DuckDuckGo to search the web for relevant information on any topic.
- **Wikipedia Queries**: Fetches concise summaries from Wikipedia for quick reference.
- **Data Saving**: Automatically saves research outputs to a text file with timestamps.
- **Structured Responses**: Outputs research data in a structured JSON format, including topic, summary, sources, and tools used.
- **Agent-Based Execution**: Employs LangChain's agent framework for intelligent tool selection and execution.

## Prerequisites

- Python 3.8 or higher
- A Google Gemini API key (obtain from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-research-assistant.git
   cd ai-research-assistant
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the API key**:
   - Create a `.env` file in the root directory.
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
   - Ensure `.env` is listed in `.gitignore` to avoid committing sensitive information.

## Usage

1. **Activate the virtual environment** (if not already active):
   ```bash
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Run the assistant**:
   ```bash
   python main.py
   ```

3. **Enter your research query** when prompted:
   ```
   🔍 What would you like me to research?
   ```

4. The assistant will process the query using available tools and output the results in JSON format, along with verbose agent execution details.

## Example

**Input Query**: "Latest developments in quantum computing"

**Output** (simplified example):
```json
{
  "topic": "Latest developments in quantum computing",
  "summary": "Quantum computing has seen significant advancements...",
  "sources": ["https://en.wikipedia.org/wiki/Quantum_computing", "https://www.example.com/quantum-news"],
  "tools_used": ["search", "wiki"]
}
```

Research outputs are automatically saved to `research_output.txt` with timestamps.

## Project Structure

- `main.py`: Main script containing the AI agent setup and execution logic.
- `tools.py`: Definitions for search, Wikipedia, and save tools.
- `requirements.txt`: List of Python dependencies.
- `.gitignore`: Git ignore rules for Python projects.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer

This tool is for educational and research purposes. Ensure compliance with API usage policies and terms of service for all integrated services.
