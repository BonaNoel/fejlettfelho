# 🎬 Movie Hub - AI-Powered Movie Application

A comprehensive fullstack movie application that combines the power of AI with extensive movie data to provide users with an intelligent movie discovery experience.

## 🌟 Features

### 🤖 AI Movie Assistant
- Intelligent chatbot powered by OpenAI GPT
- Ask questions about movies, actors, directors, and film history
- Get personalized movie recommendations
- Discuss plot details, trivia, and industry insights

### 🔍 Movie Search & Discovery
- Search for movies using the OMDB API
- View detailed movie information including cast, plot, ratings
- Browse movie posters and metadata
- Quick access to popular movies and trending content

### 🎲 Interactive Movie Quiz
- Test your movie knowledge with curated questions
- Multiple choice format with explanations
- Score tracking and progress indicators
- Questions covering various aspects of cinema

### 📱 Modern Responsive UI
- Built with Blazor Server for real-time interactivity
- Bootstrap-powered responsive design
- Smooth animations and transitions
- Dark theme support

## 🏗️ Architecture

### Frontend (Blazor Server)
- **Language**: C# with Razor components
- **Framework**: .NET 9.0
- **UI Library**: Bootstrap 5
- **Real-time**: SignalR for interactive components

### Backend Services
- **C# API**: Handles OMDB integration and business logic
- **Python REST API**: Dedicated OpenAI integration service
- **External APIs**: OMDB API for movie data

### Key Components
- `OmdbService`: Movie data integration
- `AiService`: Communication with Python AI service
- `ChatMessage`: Real-time chat functionality
- Interactive Blazor components with server-side rendering

## 🚀 Getting Started

### Prerequisites
- .NET 9.0 SDK
- Python 3.8+
- Active internet connection for API calls

### 1. Clone the Repository
```bash
git clone <repository-url>
cd fejlettfelho
```

### 2. Set Up Environment Variables
```bash
# Copy the example environment file
cp python/.env.example python/.env

# Edit python/.env and add your API keys:
# OPENAI_API_KEY=your_openai_api_key_here
# OMDB_API_KEY=your_omdb_api_key_here
```

### 3. Set Up Python API
```bash
# On Windows
start-python-api.bat

# On Linux/macOS
chmod +x start-python-api.sh
./start-python-api.sh
```

This will:
- Install required Python packages (Flask, OpenAI, python-dotenv, etc.)
- Start the Python API server on port 5000

### 4. Run the Blazor Application
```bash
cd fejlettfelho/fejlettfelho
dotnet restore
dotnet run
```

The application will be available at `https://localhost:7xxx` (check console output for exact port).

## 🔧 Configuration

### API Keys
The application uses the following APIs. Create a `.env` file in the `python/` directory with your API keys:

**Environment Variables** (in `python/.env`):
```env
# OpenAI API Key - Get from https://platform.openai.com/account/api-keys
OPENAI_API_KEY=your_openai_api_key_here

# OMDB API Key - Get from https://www.omdbapi.com/apikey.aspx
OMDB_API_KEY=your_omdb_api_key_here
```

You can copy `python/.env.example` to `python/.env` and fill in your actual API keys.

**OMDB API** (configured in `Services/OmdbService.cs`):
```csharp
private readonly string _apiKey = "abc7180d";
```

### Development Settings
- Python API runs on `http://localhost:5000`
- Blazor app typically runs on `https://localhost:7xxx`
- CORS is enabled for cross-origin requests

## 📁 Project Structure

```
fejlettfelho/
├── fejlettfelho/                 # Main Blazor application
│   ├── Components/
│   │   ├── Pages/
│   │   │   ├── Home.razor        # Main movie search page
│   │   │   ├── Chat.razor        # AI chat interface
│   │   │   └── Quiz.razor        # Movie quiz game
│   │   └── Layout/               # Navigation and layout
│   ├── Models/
│   │   └── Movie.cs              # Data models
│   ├── Services/
│   │   ├── OmdbService.cs        # OMDB API integration
│   │   └── AiService.cs          # Python API communication
│   └── wwwroot/
│       └── app.css               # Custom styling
├── python/
│   ├── RestApi.py                # Python Flask API
│   └── requirements.txt          # Python dependencies
├── start-python-api.bat          # Windows setup script
├── start-python-api.sh           # Linux/macOS setup script
└── README.md
```

## 🎯 Usage Examples

### Movie Search
1. Navigate to the home page
2. Enter a movie title, actor name, or ask a question
3. Browse search results or view AI responses
4. Click "View Details" for comprehensive movie information

### AI Chat
1. Go to the Chat page
2. Ask questions like:
   - "Recommend me a good sci-fi movie"
   - "Tell me about Christopher Nolan's filmography"
   - "What are the best movies of 2023?"
3. Use quick question buttons for common queries

### Movie Quiz
1. Navigate to the Quiz page
2. Click "Start Quiz" to begin
3. Answer multiple-choice questions
4. View explanations and track your score

## 🛠️ Development

### Adding New Features
1. **New Blazor Pages**: Add to `Components/Pages/`
2. **API Endpoints**: Extend `python/RestApi.py`
3. **Services**: Add to `Services/` directory
4. **Models**: Define in `Models/` directory

### Key Technologies
- **Blazor Server**: For reactive UI components
- **Flask**: Python web framework for AI service
- **OpenAI API**: GPT integration for intelligent responses
- **OMDB API**: Comprehensive movie database
- **Bootstrap**: Responsive UI framework

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is for educational purposes. Please ensure you comply with the terms of service for OpenAI and OMDB APIs.

## 🆘 Troubleshooting

### Common Issues

**Python API not starting:**
- Ensure Python 3.8+ is installed
- Check if all dependencies installed correctly
- Verify OpenAI API key is valid

**Movie search not working:**
- Check internet connection
- Verify OMDB API key is valid
- Ensure Python API is running

**AI chat not responding:**
- Confirm Python API is accessible at localhost:5000
- Check OpenAI API quota and key validity
- Review browser console for errors

### Support
For issues and questions, please check the troubleshooting section or create an issue in the repository.

---

**Built with ❤️ using .NET, Python, and modern web technologies**


@BonaNoel
@DavidVeres02
@skazalien
@LoosAP
