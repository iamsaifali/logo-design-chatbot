# Logo Design Chatbot 🎨

A Streamlit-based chatbot that generates logo designs using OpenAI's DALL-E model. This application allows users to describe their logo requirements and receive AI-generated logo concepts.

## Features

- User-friendly interface for entering logo design requirements
- Integration with OpenAI's DALL-E for image generation
- Support for various logo types (e.g., Wordmark, Lettermark, Pictorial Mark, etc.)
- Customizable DALL-E parameters (model version, image size, quality, number of images)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10 or later installed
- An OpenAI API key (you can obtain one from [OpenAI's website](https://openai.com/))
- Git installed on your system

## Installation

### Windows

1. Open Command Prompt and clone the repository:
   ```
   git clone https://github.com/iamsaifali/logo-design-chatbot.git
   cd logo-design-chatbot
   ```
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```
   venv\Scripts\activate
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### macOS and Linux

1. Open Terminal and clone the repository:
   ```
   git clone https://github.com/YOUR_USERNAME/logo-design-chatbot.git
   cd logo-design-chatbot
   ```
2. Create a virtual environment:
   ```
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Setting up the Environment Variables

1. In the root directory of the project, create a file named `.env`
2. Open the `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
   Replace `your_api_key_here` with your actual OpenAI API key.
3. Alternative for Not Setting Up `.env`
   If you do not create the `.env` file or fail to set the OpenAI API key, when you run the application (e.g., using the following command):
   ```
   streamlit run app.py
   ```
   You will be prompted to provide the OpenAI API key through the interface before the app starts. It's best to use the `.env` method to avoid this interruption.

## Usage

1. Ensure your virtual environment is activated.

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

4. If you haven't set up your API key in the `.env` file, you'll be prompted to enter it in the app.

5. Use the sidebar to select the logo type and customize DALL-E parameters.

6. Enter your logo design requirements in the text area.

7. Click "Generate Logo" to create logo concepts based on your input.

## Project Structure

- `app.py`: The main Streamlit application
- `components/sidebar.py`: Contains the sidebar component for logo type and DALL-E parameter selection
- `utils/openai_helper.py`: Helper functions for interacting with the OpenAI API
- `prompts/logo_prompts.py`: Contains prompts for different logo types

## Troubleshooting

- If you encounter any issues with package installations, make sure your pip is up to date:
  ```
  pip install --upgrade pip
  ```

- If you're having trouble with the OpenAI API, ensure your API key is correctly set in the `.env` file and that you have sufficient credits in your OpenAI account.

## Contributing

Contributions to the Logo Design Chatbot are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the original branch: `git push origin feature-branch-name`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## License

This project uses the [MIT](https://choosealicense.com/licenses/mit/) license.

## Contact

If you want to contact me, you can reach me at `alisaif12435@gmail.com`.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenAI](https://openai.com/)
- [DALL-E](https://openai.com/dall-e-3/)