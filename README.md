# Text-to-Speech Converter

Text-to-Speech Converter is a Python-based tool that transforms written text into spoken audio using **Google Text-to-Speech (gTTS)**. This project is ideal for anyone looking to quickly convert text into a .mp3 audio format for ease of listening, accessibility, or simple experimentation.
## Features

- **Customizable text input**: Enter any text to convert into an audio file.
- **Language Support**: Choose from multiple languages (default is English).
- **Adjustable Speed**: Set the audio output to a slower pace if needed.


## How It Works

The converter takes text input from the user, processes it with **gTTS**, and saves the resulting audio as an MP3 file. Users can customize the speed of the audio output and choose from a variety of languages supported by gTTS.

## Getting Started

To get started with Text-to-Speech Converter, clone or download the repository to your local machine:

```bash
git clone https://github.com/nikhilsambarapu8978/texttospeech
```

## Dependencies

Ensure Python is installed on your machine, then install the required dependencies by running the following command in the project directory:

```bash
pip install gTTS
```
## Running

Run the main script:

```bash
python text_to_speech.py
```
## Output Example

```bash
Enter the text you want to convert to speech: Hi,How are you?
The audio has been saved as 'sample.mp3'
```
