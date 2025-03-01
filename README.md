# Gemini 1.5 Pro Chatbot with Streamlit

This project demonstrates how to create a simple chatbot using Google's Gemini 1.5 Pro model and Streamlit for the user interface.

## Prerequisites

Before running the chatbot, ensure you have the following:

* **Python 3.7 or later:** Python is required to run the application.
* **Google Cloud Project and API Key:** You need a Google Cloud project with the Generative Language API enabled and a corresponding API key.
* **`.env` file:** Create a `.env` file in the project's root directory and add your Google Gemini API key as follows:

    ```
    GOOGLE_GEMINI_KEY=YOUR_API_KEY
    ```

## Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <your_repository_url>
    cd <your_repository_directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS and Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run main.py
    ```

2.  **Open the application in your browser:** Streamlit will provide a local URL (e.g., `http://localhost:8501`) that you can open in your web browser.

3.  **Start chatting:** Enter your messages in the input box and press Enter. The chatbot will respond using the Gemini 1.5 Pro model.

## Code Explanation

* **`main.py`:**
    * Loads the API key from the `.env` file using the `dotenv` library.
    * Configures the Gemini API using `google.generativeai`.
    * Initializes the Gemini 1.5 Pro model.
    * Uses Streamlit to create a chat interface.
    * Manages chat history using Streamlit's session state.
    * Sends user messages to the Gemini model and displays the responses.
* **`requirements.txt`:**
    * Lists all the Python packages required to run the application.

## Dependencies

The `requirements.txt` file includes the following key dependencies:

* `google-generativeai`: For interacting with the Gemini API.
* `streamlit`: For creating the web-based chat interface.
* `python-dotenv`: For loading environment variables from the `.env` file.

## Screenshots

Here are some screenshots of the completed chatbot:

![Screenshot 1](https://github.com/vaish-navi-n/AI-Chatbot/blob/main/Screenshot%20chatbot.png)
![Screenshot 2](https://github.com/vaish-navi-n/AI-Chatbot/blob/main/Screenshot%20chatbot%202.png)


## Future Improvements

* Add error handling for API requests.
* Implement more advanced chat features, such as context management and conversation history persistence.
* Add a way to change the model parameters.
* Add a way to upload files for the model to analyze.
* Improve the UI/UX.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/vaish-navi-n/AI-Chatbot/blob/main/LICENSE) file for details.
