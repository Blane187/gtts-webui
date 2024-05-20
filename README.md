# gtts-webui

gtts-webui is a web-based interface for Google Text-to-Speech (gTTS). This tool allows users to input text and receive spoken audio output using Google’s TTS API. The web UI makes it easy to generate speech in various languages and accents.

<audio controls>
  <source src="https://github.com/Blane187/gtts-webui/raw/main/output.mp3" type="audio/mp3">

</audio>


## Features

- Simple web interface for text-to-speech conversion.
- Supports multiple languages and accents.
- Ability to download the generated audio.
- Adjustable speech rate.
- Supports SSML (Speech Synthesis Markup Language) for advanced speech customization.

## Installation

To get started with gtts-webui, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Blane187/gtts-webui.git
    cd gtts-webui
    ```

2. **Install Dependencies:**

    Make sure you have Python installed. Then install the necessary packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    Start the web server by running:

    ```bash
    python app.py
    ```

4. **Access the Web UI:**

    Open your web browser and navigate to `http://127.0.0.1:5000` to start using the gtts-webui.

## Usage

1. **Enter Text:**

    Type or paste the text you want to convert to speech into the input box.

2. **Select Language and Accent:**

    Choose your preferred language and accent from the dropdown menu.

3. **Adjust Speech Rate:**

    Use the slider to adjust the speech rate to your liking.

4. **Generate Speech:**

    Click the "Convert" button to generate the speech. The audio will be played automatically, and you will have the option to download it.

5. **Advanced Customization:**

    Use SSML tags in your text for more control over the speech output.

## Contributing

We welcome contributions from the community! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Open a pull request to the main repository.

Please make sure to follow the coding standards and include appropriate tests for your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses [gTTS](https://github.com/pndurette/gTTS), a Python library and CLI tool to interface with Google Text-to-Speech API.
- Thanks to all contributors and users for their support and feedback.

---

## Terms of Use

By using the gtts-webui application, you agree to the following terms:

1. **Usage:**
   - The application is provided for personal and non-commercial use only.
   - You must comply with all applicable laws and regulations while using the application.

2. **Content:**
   - You are solely responsible for the text you input and the audio you generate using the application.
   - Do not use the application to generate audio that is harmful, offensive, or violates any laws.

3. **Limitations:**
   - The application is provided "as is" without any warranties or guarantees.
   - The maintainers are not responsible for any damages or losses resulting from the use of the application.

4. **Privacy:**
   - The application does not store or share your input text or generated audio. However, be mindful of the data you input as it is processed by the Google Text-to-Speech API.
   - We do not collect any personal information from users.

5. **Changes:**
   - We reserve the right to modify these terms at any time. Changes will be posted on the repository, and your continued use of the application constitutes acceptance of the new terms.

6. **Third-Party Services:**
   - The application uses Google Text-to-Speech API, and your use of the application is subject to Google’s terms and policies.

By using the gtts-webui, you acknowledge that you have read, understood, and agree to these terms of use. If you do not agree with any part of these terms, you must discontinue using the application immediately.

