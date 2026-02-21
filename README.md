# Senior AI Voice Assistant

Senior AI Voice Assistant is designed to assist elderly users in a Senior Smart Community by providing easy-to-use voice-based interaction with various smart systems and services. The project focuses on helping seniors navigate everyday tasks with voice commands, improving their independence and quality of life.


## How it works

1. :microphone: The user speaks into the microphone
2. :keyboard: Voice is converted to text using <a href="https://deepgram.com/" target="_blank">Deepgram</a>
3. :robot: Text is sent to <a href="https://openai.com/" target="_blank">OpenAI</a>'s GPT-3 API to generate a response
4. :loudspeaker: Response is converted to speech using <a href="https://elevenlabs.io/" target="_blank">ElevenLabs</a>
5. :loud_sound: Speech is played using <a href="https://www.pygame.org/wiki/GettingStarted" target="_blank">Pygame</a>
6. :computer: Conversation is displayed in a webpage using <a href="https://github.com/Avaiga/taipy" target="_blank">Taipy</a>


## Requirements

**Python 3.8 - 3.11**

Make sure you have the following API keys:
- <a href="https://developers.deepgram.com/docs/authenticating" target="_blank">Deepgram</a>
- <a href="https://platform.openai.com/account/api-keys" target="_blank">OpenAI</a>
- <a href="https://elevenlabs.io/docs/api-reference/text-to-speech" target="_blank">Elevenlabs</a>

## How to install

1. Clone the repository

2. Install the requirements

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add the following variables:

```bash
DEEPGRAM_API_KEY=XXX...XXX
OPENAI_API_KEY=sk-XXX...XXX
ELEVENLABS_API_KEY=XXX...XXX
```

## How to use

1. Run `display.py` to start the web interface

```bash
python display.py
```

2. In another terminal, run `main.py` to start the voice assistant

```bash
python main.py
```

- Once ready, both the web interface and the terminal will show `Listening...`
- You can now speak into the microphone
- Once you stop speaking, it will show `Stopped listening`
- It will then start processing your request
- Once the response is ready, it will show `Speaking...`
- The response will be played and displayed in the web interface.

Here is an example:

```
Listening...
Done listening
Finished transcribing in 1.21 seconds.
Finished generating response in 0.72 seconds.
Finished generating audio in 1.85 seconds.
Speaking...

 --- Senior Andranik: good morning jarvis
 --- Aria: Good morning, Senior Andranik! How can I assist you today?

Listening...
...
```
![Screenshot 2024-12-18 220925](https://github.com/user-attachments/assets/ad126185-1181-4ac0-a364-924475466f87)
# 🤖 Aria — Senior AI Voice Assistant

> A voice-powered AI companion built for elderly users, integrating speech recognition, LLM responses, and AI-synthesized voice — deployed as a live web interface.

[![Python](https://img.shields.io/badge/Python-3.8--3.11-blue?logo=python&logoColor=white)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3-412991?logo=openai&logoColor=white)](https://openai.com)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-orange)](https://elevenlabs.io)
[![Deepgram](https://img.shields.io/badge/Deepgram-STT-13EF93)](https://deepgram.com)
[![Taipy](https://img.shields.io/badge/Taipy-Web%20UI-red)](https://github.com/Avaiga/taipy)

---

## 🎬 Demo

[![Watch the Community Demo](https://img.shields.io/badge/▶%20Watch%20Project%20Demo-YouTube-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=nKVvYBCBXxs)

[![Figma Prototype](https://img.shields.io/badge/Open%20UI%20Prototype-Figma-purple?style=for-the-badge&logo=figma)](https://www.figma.com/proto/Bveqqy4Nn0SfUoR0ARjEVB/Untitled?nodeid=6-2&t=lzhhjAVlM9wNCHYl-1)

---

## What It Does

**Aria** is an AI voice assistant designed specifically for seniors in the *Senior Smart Community* — a holistic platform addressing elderly social isolation through AI, smart transport, and community infrastructure.

The assistant bridges the gap between seniors who want to engage with their community and the technology barriers that stop them. Instead of typing, clicking through menus, or navigating complex UIs, seniors simply **speak** — and Aria responds with a warm, synthesized voice.

```
Senior Andranik: good morning jarvis
Aria: Good morning, Senior Andranik! How can I assist you today?
```

---

## ⚙️ How It Works

```
🎤 User speaks
    ↓
⌨️  Deepgram converts speech → text  (real-time STT)
    ↓
🤖  OpenAI GPT-3 generates a response
    ↓
📢  ElevenLabs converts response → voice  (AI voice synthesis)
    ↓
🔊  Pygame plays the audio
    ↓
💻  Taipy updates the live web interface
```

Five AI/API services working in concert — integrated end-to-end in Python.

---

## 🏗️ Architecture

| File | Role |
|------|------|
| `main.py` | Core voice loop — listen → transcribe → generate → speak |
| `display.py` | Taipy web server, renders conversation in real time |
| `record.py` | Microphone capture and audio handling |
| `display.css` | Accessible UI styling |
| `conv.txt` / `status.txt` | Shared state between voice loop and web display |
| `audio/` | ElevenLabs synthesized audio output |
| `requirements.txt` | Full dependency list |

---

## 🧠 Why These Design Choices

### ElevenLabs for voice synthesis
Generic TTS sounds robotic — which erodes trust for elderly users. ElevenLabs produces warm, natural speech, making Aria feel less like a tool and more like a companion.

### Deepgram for speech recognition
Optimized for real-time, low-latency transcription. Critical for elderly users who speak slowly or pause — Deepgram handles this better than alternatives.

### Taipy for the web interface
Provides a live-updating conversation display without the complexity of a full frontend framework. Seniors and caregivers can monitor the conversation on screen while audio plays.

### Separation of `main.py` and `display.py`
Running the voice loop and web UI as separate processes keeps the assistant responsive during API calls — the display updates asynchronously while audio is still being generated.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8–3.11
- API keys for [Deepgram](https://developers.deepgram.com/docs/authenticating), [OpenAI](https://platform.openai.com/account/api-keys), and [ElevenLabs](https://elevenlabs.io/docs/api-reference/text-to-speech)

### Installation

```bash
git clone https://github.com/SyuzannE/SeniorAssistant.git
cd SeniorAssistant
pip install -r requirements.txt
```

Create a `.env` file:

```env
DEEPGRAM_API_KEY=your_key_here
OPENAI_API_KEY=sk-your_key_here
ELEVENLABS_API_KEY=your_key_here
```

### Run

```bash
# Terminal 1 — start the web display
python display.py

# Terminal 2 — start the voice assistant
python main.py
```

Once both are running, the terminal shows `Listening...`. Speak into the microphone — Aria responds in audio and updates the web interface simultaneously.

---

## 🖥️ Web Interface

![Screenshot](https://github.com/user-attachments/assets/ad126185-1181-4ac0-a364-924475466f87)

Renders the full conversation in real time, accessible from any browser on the local network. Designed with large text and high contrast for senior accessibility.

---

## 🔬 Research Foundation

This assistant was built from a rigorous HCI research foundation:

- **User interviews** with elderly users revealed voice as the most natural interface for seniors with limited digital literacy
- **Empathy mapping** identified core emotional needs: feeling heard, not confused, never abandoned mid-task
- **Persona design** ("Senior Andranik", 70, retired teacher in Yerevan) grounded every design decision in a specific human context
- **Survey data**: 65% of surveyed seniors reported dissatisfaction with current social support — validating the need for an always-available AI companion

---

## 🌐 Broader Project Context

Aria is the AI layer of the **Senior Smart Community** — a full ecosystem:

| Component | Description |
|-----------|-------------|
| **Aria (this repo)** | Voice AI assistant — the personal companion layer |
| **Smart Bus** | AI-integrated accessible transport with voice booking |
| **Web Platform** | Activity discovery, registration, event management |
| **Community Spaces** | 15 purpose-designed physical spaces (art, library, gym, garden…) |

All components are designed to interoperate — Aria can book Smart Bus rides, register for activities, and navigate the community platform on a senior's behalf.

---

## 🔮 Roadmap

- [ ] Upgrade to GPT-4 for richer, more contextual responses
- [ ] Health monitoring prompts (medication reminders, mood check-ins)
- [ ] Armenian and Russian language support
- [ ] Mobile app wrapper (iOS + Android)
- [ ] Smart Bus booking integration via voice command
- [ ] Activity calendar sync with the community web platform

---

## 🛠️ Stack

```
Speech-to-Text   Deepgram
LLM              OpenAI GPT-3
Text-to-Speech   ElevenLabs
Audio Playback   Pygame
Web Interface    Taipy
Language         Python 3.8–3.11
```

---

## 📄 Academic Context

**Human-Computer Interaction** coursework  
French University in Armenia (UFAR) — Faculty of Computer Science & Applied Mathematics  
Professor: Eliza Gyulgyulyan | December 2024

**Syuzanna Ghazaryan's contributions:**
- Full voice assistant pipeline implementation (`main.py`, `record.py`, `display.py`)
- AI assistant interface design in Figma (accessibility-first: large buttons, voice input, persistent help)
- User research: survey design, empathy map canvas, persona development
- Community space design and narrative project brief ("A Day in Our Community")

---

*Built with empathy. Designed for dignity. Powered by AI.*

