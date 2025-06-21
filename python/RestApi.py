import os
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Get API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

# Set OpenAI API key if available
if OPENAI_API_KEY:
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

OMDB_BASE_URL = "https://www.omdbapi.com/"

def search_movie_omdb(query):
    """Search for movies using OMDB API"""
    try:
        response = requests.get(f"{OMDB_BASE_URL}?apikey={OMDB_API_KEY}&s={query}")
        return response.json()
    except:
        return None

def get_movie_details_omdb(title):
    """Get detailed movie information from OMDB API"""
    try:
        response = requests.get(f"{OMDB_BASE_URL}?apikey={OMDB_API_KEY}&t={title}&plot=full")
        return response.json()
    except:
        return None

@app.route('/ai/movie', methods=['POST'])
def get_movie_ai_response():
    data = request.json
    question = data.get('question')
    language = data.get('language', 'English')
    model_name = data.get('model_name', 'gpt-3.5-turbo')
    
    # Create a movie-specific system prompt
    system_prompt = f"""You are a helpful movie assistant that can answer questions about movies, actors, directors, and film industry. 
    Always respond in {language}. 
    
    If the user asks about specific movies, actors, or directors, provide detailed and accurate information.
    You can discuss plot summaries, cast information, release dates, box office performance, awards, trivia, and recommendations.
    
    When mentioning specific movies, try to include the release year in parentheses.
    Be conversational and engaging while being informative.
    
    If you're not sure about specific details, it's okay to say so rather than provide incorrect information."""
    
    client = OpenAI()
    
    try:
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user", 
                    "content": question
                }
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        ai_response = completion.choices[0].message.content
        return jsonify({"response": ai_response})
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "Sorry, I couldn't process your request at the moment."}), 500

@app.route('/ai', methods=['POST'])
def getAiByPost():
    data = request.json
    question = data.get('question')
    language = data.get('language', 'English')
    model_name = data.get('model_name', 'gpt-3.5-turbo')
    system_prompt = "Always answer in " + language
    
    client = OpenAI()
    
    try:
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        
        return jsonify({"response": completion.choices[0].message.content})
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "Sorry, I couldn't process your request."}), 500

@app.route('/ai/quiz', methods=['POST'])
def generate_quiz():
    try:
        data = request.json
        difficulty = data.get('difficulty', 'medium')  # easy, medium, hard
        category = data.get('category', 'general')  # general, actors, directors, genres, decades
        num_questions = data.get('num_questions', 5)
        
        # Create a prompt for generating quiz questions
        quiz_prompt = f"""
        Generate {num_questions} multiple choice movie quiz questions with the following criteria:
        - Difficulty: {difficulty}
        - Category: {category} movies
        - Each question should have 4 options (A, B, C, D)
        - Include interesting and engaging questions about movies, actors, directors, or cinema history
        - Vary the question types (release years, cast, directors, plot details, awards, etc.)
        - Make sure the questions are factual and have definitive correct answers
        
        Return the response as a JSON object with this exact structure:
        {{
            "questions": [
                {{
                    "question": "Question text here?",
                    "options": ["Option A", "Option B", "Option C", "Option D"],
                    "correct_answer": "Option A",
                    "explanation": "Brief explanation of why this is correct"
                }}
            ]
        }}
        
        Focus on making the questions fun and challenging for movie enthusiasts!
        """
        
        client = OpenAI()
        
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are a movie trivia expert who creates engaging and accurate quiz questions. Always respond with valid JSON format."},
                {"role": "user", "content": quiz_prompt}
            ],
            max_tokens=1500,
            temperature=0.8
        )
        
        # Parse the AI response as JSON
        import json
        quiz_data = json.loads(response.choices[0].message.content)
        
        return jsonify(quiz_data)
    
    except json.JSONDecodeError:
        return jsonify({'error': 'Failed to parse AI response as JSON'}), 500
    except Exception as e:
        print(f"Quiz Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)