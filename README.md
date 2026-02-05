# INDG Architect Interview Prep v2 🏗️

An AI-powered interview coaching tool designed to help candidates prepare for the **Web Application Architect 3** role at INDG (Industrial/Defense Digital Group). This application provides real-time feedback on behavioral and system design interview answers using OpenAI's GPT models and a "Bar Raiser" evaluation framework.

## Features

- **Speech Recognition**: Record your interview answers directly via microphone
- **AI-Powered "Bar Raiser" Feedback**: Get structured, expert feedback from a Principal Architect perspective
- **Behavioral Interview Questions**: Multi-tier behavioral questions (Foundational → Intermediate → Deep Dive)
- **System Design Questions**: AWS-focused architecture questions with event-driven, serverless, and microservices emphasis
- **Intelligent Feedback Structure**:
  - Scorecard (Technical Accuracy, Communication Clarity, Seniority Signal)
  - Trade-Off Analysis
  - Mental Model Check
  - "Level-Up" Rephrase with Principal Architect terminology
- **Interactive Streamlit UI**: Clean, user-friendly web interface
- **Technology-Specific Coaching**: Tailored for AWS Serverless, EDA, Microservices, and Micro-frontends

## Technologies & Stack

- **Target Role Stack**: AWS (Serverless focus), Event-Driven Architecture (EDA), Microservices, Micro-frontends
- **Level**: Senior/Principal Individual Contributor

## Prerequisites

- Python 3.8+
- Microphone (for audio recording)
- OpenAI API key

## Installation

1. **Navigate to the project directory**:

   ```bash
   cd BloombergInterviewPrep
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Usage

Run the Streamlit application:

```bash
streamlit run interview_coach.py
```

The app will open in your browser at `http://localhost:8501`.

### Workflow

1. Select a question category (Behavioral or System Design)
2. Choose a difficulty level (Foundational, Intermediate, or Deep Dive)
3. Click to get a random question
4. Record your answer using your microphone
5. Submit to receive detailed "Bar Raiser" feedback with:
   - Technical accuracy scoring
   - Trade-off analysis
   - Architectural pattern recognition
   - Principal-level rephrase of your answer

6. **Activate the virtual environment**:

   ```bash
   source venv/bin/activate
   ```

7. **Run the Streamlit app**:

   ```bash
   streamlit run interview_coach.py
   ```

8. **Open your browser** to the local URL (typically `http://localhost:8501`)

9. **Interact with the coach**:
   - Use the microphone button to record your answer
   - Or type your answer directly
   - Get AI-powered feedback with professional suggestions

## Project Structure

```
GrayMatterSystemsInterviewPrep/
├── interview_coach.py          # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── venv/                       # Virtual environment (created on setup)
```

## Dependencies

- **streamlit**: Web app framework for building interactive interfaces
- **openai**: Official OpenAI Python client library
- **SpeechRecognition**: Speech-to-text conversion using Google's API
- **pyaudio**: Audio I/O support for microphone input

## API Keys & Authentication

This application uses the OpenAI API. You'll need:

1. An OpenAI account (https://openai.com)
2. An API key from your account settings
3. Set the `OPENAI_API_KEY` environment variable

## Troubleshooting

### "No module named 'speech_recognition'"

Ensure all dependencies are installed:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### PyAudio Installation Issues (macOS)

```bash
brew install portaudio
CFLAGS="-I/opt/homebrew/include" LDFLAGS="-L/opt/homebrew/lib" pip install pyaudio
```

### Microphone Not Working

- Ensure your microphone is properly connected
- Check system audio settings allow microphone access
- Try increasing the timeout in `recognize_speech()` for slower systems

## Features in Detail

### Interview Feedback Structure

The coach provides feedback organized into three sections:

1. **🟢 What You Did Well**: Highlights strengths and alignment with GrayMatter values
2. **🟡 Areas for Improvement**: Constructive critique on structure, tone, and completeness
3. **💡 Suggested Phrasing**: Two professional variations of your response (Confident/Direct and Thoughtful/Collaborative)

### GrayMatter Systems Context

The coach is specialized for the Engineer I role with knowledge of:

- Company values: Accountability, Integrity, Respect, Innovation, Teamwork
- Program details: 2-year mentorship, hands-on field work, industrial automation
- Key traits: "Thinking and Doing" mentality, owning mistakes, learning agility

## Contributing

Suggestions for improvements are welcome! Consider:

- Adding more question templates for different interview scenarios
- Expanding company context for other roles
- Improving speech recognition accuracy
- Adding answer history/progress tracking

## License

This project is for educational and interview preparation purposes.

## Support

For issues or questions about the application, refer to the troubleshooting section above or check the official documentation for:

- [Streamlit](https://docs.streamlit.io/)
- [OpenAI API](https://platform.openai.com/docs/)
- [SpeechRecognition](https://github.com/Uberi/speech_recognition#readme)
