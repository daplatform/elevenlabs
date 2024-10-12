# Bloopa 🌈🐾  
**It was difficult to show everything in the demo video. Hence, we have created this section**  

## Overview 📚✨  
Welcome to **Bloopa**, the innovative app designed to empower children with speech difficulties! Bloopa transforms learning and communication through interactive features that engage kids in fun and meaningful ways. 🌟  

- **Multi-modal Input**: Engage through speech, touch, or gestures 🎤🤚  
- **AI-Powered Support**: Friendly virtual bots help develop communication skills 🤖❤️  
- **Visual Learning**: Avatars like mothers and Santa Claus teach abstract concepts 🌟🎅  
- **Speech Restoration**: Advanced speech recognition enhances communication abilities 🔊🗣️  

# Bloopa: An Evidence Based Solution
Bloopa represents a significant advancement in augmentative and alternative communication (AAC) through its integration of multimodal input, AI-driven technologies, and cognitive scaffolding. By supporting speech, touch, and gestures, Bloopa leverages Visual, Auditory, and Kinesthetic (VAK) learning principles to enhance linguistic acquisition, aligning with research that shows multimodal input improves learning outcomes by providing a richer contextual framework (Amariucai et al., 2023). Its specialized automatic speech recognition (ASR) system, tailored for users with speech impairments such as dysarthria, significantly reduces error rates compared to traditional systems that rely on generic datasets (Gonzalez et al., 2022). Furthermore, Bloopa employs large language models (LLMs) to anticipate user responses based on contextual cues, a feature absent in most AAC devices, allowing it to suggest contextually relevant responses and vocalize them using advanced text-to-speech (TTS) technology (Vaswani et al., 2017).

In addition to predictive interaction, Bloopa offers dynamic concept explanation through AI-generated visuals and audio, which simplifies complex concepts and mitigates cognitive overload, following principles from Cognitive Load Theory (Sweller, 1988). Its AI-driven storytelling mechanism automatically generates personalized content tailored to individual learning needs, reducing the manual input burden typically placed on caregivers in traditional AAC systems (Murray et al., 2020). The integration of ElevenLabs' TTS technology enables Bloopa to produce personalized, natural-sounding voices that enhance emotional connection during communication, a factor often overlooked by conventional AAC systems (Wang et al., 2018).

Emotion recognition technology further sets Bloopa apart by analyzing user facial expressions to detect emotional states and adjust responses accordingly, ensuring that the communication remains contextually appropriate (Picard et al., 2001). For non-verbal users, Bloopa provides cognitive scaffolding via generative AI, empowering them to make decisions beyond pre-programmed phrases, thus promoting greater autonomy in communication (Wood et al., 1976). Bloopa’s ASR models are also designed to restore coherent speech from fragmented inputs, providing a transformative solution for users with severe articulation difficulties (Duffy et al., 2019). Moreover, its ability to adapt communication styles in real time based on emotional engagement enhances the overall user experience during emotionally charged interactions (Zeng et al., 2009).

Finally, Bloopa’s scalable, AI-driven architecture leverages advanced NLP and deep learning techniques, ensuring that the platform remains adaptable as AAC needs evolve, positioning it as a leader in the AAC domain (Devlin et al., 2018). This combination of features establishes Bloopa as a superior tool for enhancing communication in individuals with speech impairments, addressing limitations in traditional devices while providing a more natural and intuitive user experience.

### References
- Amariucai, M., et al. (2023). "Multimodal Input in Language Acquisition."  
- Gonzalez, A., et al. (2022). "Advancements in ASR for Speech Impairments."  
- Vaswani, A., et al. (2017). "Attention is All You Need."  
- Sweller, J. (1988). "Cognitive Load During Problem Solving."  
- Murray, T., et al. (2020). "Automated Content Generation in Educational Settings."  
- Wang, Y., et al. (2018). "Text-to-Speech Synthesis Using Deep Learning."  
- Picard, R.W., et al. (2001). "Affective Computing."  
- Wood, D., Bruner, J.S., & Ross, G. (1976). "The Role of Tutoring in Problem Solving."  
- Duffy, J.R., et al. (2019). "The Impact of Speech Restoration Technologies."  
- Zeng, Z., et al. (2009). "A Survey on Affective Computing: From Theory to Applications."  
- Devlin, J., et al. (2018). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding."  

## Architecture 📚✨  
<p align="center">
  <img src="static/images/arch-1.png" alt="Architecture 1" width="300" />
  <img src="https://raw.githubusercontent.com/daplatform/elevenlabs/main/static/images/arch-2.png" alt="Architecture 2" width="300" />
</p>  

## Hands on Demo 📚✨  
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

## Install Libraries
To use ElevenLabs, Deepgram, and TogetherAPI, install the necessary Python libraries using `pip`. Run the following commands:

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

## Top Companies in Assistive Technology (AAC)

1. **Liberator**  
   - **Overview**: Provides customizable AAC devices and software with user-friendly interfaces.  
   - **Limitations**: Compatibility issues and steep learning curve for advanced features.

2. **Zyteq**  
   - **Overview**: High-tech AAC solutions with eye-gaze technology.  
   - **Limitations**: High costs and requires extensive training.

3. **Link Assistive Technology**  
   - **Overview**: Offers high-tech and low-tech AAC tools.  
   - **Limitations**: Less portable devices and limited voice customization.

4. **Tobii Dynavox**  
   - **Overview**: Eye-tracking technology for communication devices.  
   - **Limitations**: Environmental sensitivity, expensive, complex setup.

5. **Prentke Romich Company (PRC)**  
   - **Overview**: AAC devices with symbol-based communication.  
   - **Limitations**: Less intuitive interface compared to newer technologies.

### Bloopa vs Traditional AAC
- **Speed of Communication**: Bloopa reduces speech output delays.  
- **Voice Customization**: Bloopa offers a wider variety of natural voices.  
- **User-Friendliness**: Intuitive interface, easier for new users.  
- **Modern Integration**: Seamless connection with mobile platforms and social media, often limited in other AAC systems.
* Note : This is our independent assessment. We do not want to get into legal issues, so we have kept it to overview areas
In summary, Bloopa's focus on speed, personalization, and modern technology makes it a strong competitor in the AAC market.

