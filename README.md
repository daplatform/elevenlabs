# Bloopa 🌈🐾  
**It was difficult to show everything in the demo video. Hence, we have created this section**  

## Overview 📚✨  
Welcome to **Bloopa**, the innovative app designed to empower children with speech difficulties! Bloopa transforms learning and communication through interactive features that engage kids in fun and meaningful ways. 🌟  

- **Multi-modal Input**: Engage through speech, touch, or gestures 🎤🤚  
- **AI-Powered Support**: Friendly virtual bots help develop communication skills 🤖❤️  
- **Visual Learning**: Avatars like mothers and Santa Claus teach abstract concepts 🌟🎅  
- **Speech Restoration**: Advanced speech recognition enhances communication abilities 🔊🗣️  

## Architecture 📚✨  
<p align="center">
  <img src="static/images/arch-1.png" alt="Architecture 1" width="300" />
  <img src="https://raw.githubusercontent.com/daplatform/elevenlabs/main/static/images/arch-2.png" alt="Architecture 2" width="300" />
</p>  

## Videos 📚✨  
<a href="https://youtu.be/MVfWJsBO7ts">
  <img src="https://img.youtube.com/vi/MVfWJsBO7ts/hqdefault.jpg" alt="Video 1" width="150" />
</a>
<a href="https://youtu.be/fUZh-2TX7VY">
  <img src="https://img.youtube.com/vi/fUZh-2TX7VY/hqdefault.jpg" alt="Video 2" width="150" />
</a>
<a href="https://youtu.be/oyo2T2cGHik">
  <img src="https://img.youtube.com/vi/oyo2T2cGHik/hqdefault.jpg" alt="Video 3" width="150" />
</a>
<a href="https://youtu.be/2N_XUn7aDLU">
  <img src="https://img.youtube.com/vi/2N_XUn7aDLU/hqdefault.jpg" alt="Video 4" width="150" />
</a>

## Steps to Install 📦  
Follow these steps to set up **Bloopa**:

### 1. Install Required Libraries  
To use ElevenLabs, Deepgram, and TogetherAPI, install the necessary Python libraries using `pip`. Run the following commands:

```bash
pip install elevenlabs
pip install deepgram-sdk
pip install togetherai

## Create config.py
Create a config.py file with below information -
class Config:
    # Your Eleven Labs API key
    XI_API_KEY = ""
    XI_API_KEY2 = ""  
    
    # Your Deepgram API key
    DEEPGRAM_API_KEY = ""
    
    # Your Voice ID
    VOICE_ID = ""
    
    # Your Gemini API key
    GEMINI_API_KEY = ""
    
    # LimeWire API key
    LIMEWIRE_API_KEY1 = ""
    
    # Your TOG API key
    TOG_API_KEY = ""
    
    # Your Serper API key
    SERPER_API_KEY = ""
    
    # Secret key (used for security purposes)
    SECRET_KEY = ""
