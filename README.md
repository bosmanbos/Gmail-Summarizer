# Gmail Summary Crew

This project uses CrewAI to fetch, analyze, and summarize important emails from your Gmail account.

## Features

- Fetches emails from your Gmail inbox
- Analyzes emails to determine importance
- Summarizes important emails
- Outputs a summary to a text file

## Prerequisites

- Python 3.8 or higher
- A Google Cloud Project with the Gmail API enabled
- OAuth 2.0 Client ID credentials

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/gmail-summary-crew.git
   cd gmail-summary-crew
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up Google Cloud Project and obtain the client_secret.json file:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Gmail API for your project
   - Create OAuth 2.0 credentials (Desktop app)
   - Download the client_secret.json file

4. Place the client_secret.json file in the project directory

5. Update the `credentials_path` in `gmailScraper.py` to point to your client_secret.json file

6. Set your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY="your-api-key-here"
   ```

## Usage

Run the main script:

```
python ./src/Gmail_Summarizer/main.py
```

The script will:
1. Authenticate with your Gmail account (first run will require manual authentication)
2. Fetch emails from your inbox
3. Analyze the importance of each email
4. Summarize important emails
5. Save the summary to `Important_Email_Summary.txt`

## File Structure

- `main.py`: The main script that orchestrates the CrewAI agents and tasks
- `agents_tasks.py`: Defines the agents and their tasks
- `gmailScraper.py`: Contains the GmailFetchTool for interacting with the Gmail API
- `requirements.txt`: Lists all the Python dependencies
- `README.md`: This file, containing project information and setup instructions

## Obtaining client_secret.json

To get the client_secret JSON file needed for this program:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the Gmail API:
   - In the left sidebar, click on "APIs & Services" > "Library"
   - Search for "Gmail API" and click on it
   - Click the "Enable" button
4. Create OAuth 2.0 credentials:
   - In the left sidebar, click on "APIs & Services" > "Credentials"
   - Click the "Create Credentials" button and select "OAuth client ID"
   - Choose "Desktop app" as the application type
   - Give your OAuth client a name (e.g., "Gmail Summary Crew")
   - Click "Create"
5. Download the client secret JSON file:
   - After creating the credentials, you'll see a modal with your client ID and client secret
   - Click the download button (looks like a down arrow) to download the JSON file
   - Rename the file to `client_secret.json` for consistency
6. Move the `client_secret.json` file to your project directory.
7. Update the `credentials_path` in `gmailScraper.py` to point to your `client_secret.json` file.

Note: Never share your `client_secret.json` file publicly. Add it to your `.gitignore` file to prevent accidental commits.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
