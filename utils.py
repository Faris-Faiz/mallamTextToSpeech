import streamlit as st
import os
import base64
from gradio_client import Client

def generate_tts(text, model, temperature, length_ratio):
    """
    Generate Text-to-Speech audio using Mesolitica VITS models
    
    Args:
        text (str): Input text to convert to speech
        model (str): Selected TTS model
        temperature (float): Pitch manipulation parameter
        length_ratio (float): Duration manipulation parameter
    
    Returns:
        str: Path to generated audio file or None if generation fails
    """
    try:
        # Instantiate Gradio client
        client = Client("https://mesolitica-ms-tts-vits.hf.space/--replicas/t457b/")
        
        # Generate audio
        result = client.predict(
            text,
            model,
            temperature,
            length_ratio,
            api_name="/predict"
        )
        
        # Validate result
        if not result or not isinstance(result, str) or not result.endswith('.wav'):
            st.error("Invalid audio generation result")
            return None
        
        # Save to a consistent location
        path = os.getcwd()
        output_path = os.path.join(f"%s/generated_audio" % path, 'generated_tts.wav')
        
        # Remove previous file if exists
        if os.path.exists(output_path):
            os.remove(output_path)
        
        # Rename/move the generated file
        os.rename(result, output_path)
        
        return output_path
    
    except Exception as e:
        st.error(f"Error generating audio: {e}")
        return None

def autoplay_audio(audio_file):
    """
    Create an HTML5 audio element with autoplay functionality
    
    Args:
        audio_file (str): Path to the audio file to be played
    """
    if not os.path.exists(audio_file):
        st.error(f"Audio file not found: {audio_file}")
        return
    
    # Read the audio file and encode it to base64
    with open(audio_file, 'rb') as audio:
        audio_bytes = audio.read()
        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
    
    # Create an HTML5 audio element with autoplay
    autoplay_html = f"""
    <audio autoplay>
        <source src="data:audio/wav;base64,{audio_base64}" type="audio/wav">
        Your browser does not support the audio element.
    </audio>
    """
    
    # Use st.markdown to render the HTML5 audio element
    st.markdown(autoplay_html, unsafe_allow_html=True)

def get_tts_models():
    """
    Retrieve list of available TTS models
    
    Returns:
        list: Available Mesolitica TTS models
    """
    return [
        'mesolitica/VITS-osman', 
        'mesolitica/VITS-yasmin', 
        'mesolitica/VITS-female-singlish', 
        'mesolitica/VITS-haqkiem', 
        'mesolitica/VITS-orkid', 
        'mesolitica/VITS-bunga', 
        'mesolitica/VITS-jebat', 
        'mesolitica/VITS-tuah', 
        'mesolitica/VITS-male', 
        'mesolitica/VITS-female', 
        'mesolitica/VITS-husein'
    ]
