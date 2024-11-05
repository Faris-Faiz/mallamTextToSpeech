# Mesolitica MS-TTS Streamlit App

## Overview
This is a Text-to-Speech (TTS) Streamlit application that leverages Mesolitica's VITS (Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech) models. The app converts text to speech using the Hugging Face Space at [https://huggingface.co/spaces/mesolitica/ms-tts-VITS](https://huggingface.co/spaces/mesolitica/ms-tts-VITS).

## Features
- Multiple TTS model selection
- Text-to-Speech conversion using Mesolitica's Hugging Face Space
- Pitch manipulation via temperature slider
- Duration manipulation via length ratio slider
- Instant audio playback

## Available TTS Models
- mesolitica/VITS-osman
- mesolitica/VITS-yasmin
- mesolitica/VITS-female-singlish
- mesolitica/VITS-haqkiem
- mesolitica/VITS-orkid
- mesolitica/VITS-bunga
- mesolitica/VITS-jebat
- mesolitica/VITS-tuah
- mesolitica/VITS-male
- mesolitica/VITS-female
- mesolitica/VITS-husein

## Prerequisites
- Python 3.8+
- Streamlit
- Gradio Client

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-repo/mesolitica-tts-app.git
cd mesolitica-tts-app
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install required dependencies:
```bash
pip install streamlit gradio-client
```

## Running the Application

```bash
streamlit run ms_tts_streamlit_app.py
```

## How to Use
1. Enter the text you want to convert to speech
2. Select a TTS model from the dropdown
3. Adjust temperature and length ratio sliders
4. Click "Generate Audio" to create and play the speech

## Dependencies
- Streamlit
- Gradio Client

## Note
This application uses the Mesolitica MS-TTS VITS Hugging Face Space (https://huggingface.co/spaces/mesolitica/ms-tts-VITS) for audio generation. An active internet connection is required.
