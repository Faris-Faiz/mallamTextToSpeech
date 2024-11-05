import streamlit as st
from utils import generate_tts, autoplay_audio, get_tts_models

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Mesolitica Text-to-Speech",
        page_icon="🔊",
        layout="wide"
    )

    # Main title
    st.title("🎙️ Mesolitica Text-to-Speech Converter")
    
    # Create a sidebar for inputs
    with st.sidebar:
        st.header("🛠️ Audio Generation Settings")
        
        # Model selection with help text
        models = get_tts_models()
        model = st.selectbox(
            "Select TTS Model", 
            models, 
            index=0,
            help="Choose the text-to-speech model for audio generation"
        )
        
        # Temperature slider with detailed explanation
        temperature = st.slider(
            "Temperature (Pitch Variation)", 
            0.0, 1.0, 0.6666,
            help="Controls pitch variation. Lower values make speech more monotone, higher values add more variation."
        )
        
        # Length ratio slider with explanation
        length_ratio = st.slider(
            "Length Ratio (Speech Duration)", 
            0.0, 3.0, 1.0,
            help="Adjusts speech duration. Values < 1 speed up speech, > 1 slow it down."
        )

    # Main content area
    col1, col2 = st.columns(2)
    
    with col1:
        # Text input with more context
        text = st.text_area(
            "Enter Text to Convert", 
            "Nama saya Sarah",
            height=200,
            help="Type or paste the text you want to convert to speech"
        )
    
    with col2:
        # Audio generation and preview
        st.write("### 🔊 Audio Preview")
        
        # Generate button
        generate_button = st.button("Generate Audio", type="primary")
        
        # Audio generation logic
        if generate_button:
            with st.spinner('Generating audio...'):
                try:
                    # Generate audio
                    audio_path = generate_tts(text, model, temperature, length_ratio)
                    
                    if audio_path:
                        # Display audio player
                        st.audio(audio_path, format='audio/wav')
                        st.success(f"Audio successfully generated from: {audio_path}")
                    else:
                        st.error("Failed to generate audio. Please check your input.")
                
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        
        # Additional guidance
        st.info(
            "💡 Tips:\n"
            "- Adjust temperature for pitch variation\n"
            "- Use length ratio to control speech speed\n"
            "- Select different models for varied outputs"
        )

if __name__ == "__main__":
    main()
