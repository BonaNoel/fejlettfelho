using System.Text.Json;
using System.Text;

namespace fejlettfelho.Services
{
    public class AiService
    {
        private readonly HttpClient _httpClient;
        private readonly string _pythonApiUrl = "http://localhost:5000";

        public AiService(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public async Task<string> GetMovieAiResponseAsync(string question, string language = "English")
        {
            try
            {
                var requestData = new
                {
                    question = question,
                    language = language,
                    model_name = "gpt-3.5-turbo"
                };

                var json = JsonSerializer.Serialize(requestData);
                var content = new StringContent(json, Encoding.UTF8, "application/json");

                var response = await _httpClient.PostAsync($"{_pythonApiUrl}/ai/movie", content);
                
                if (response.IsSuccessStatusCode)
                {
                    var responseContent = await response.Content.ReadAsStringAsync();
                    
                    try
                    {
                        var jsonResponse = JsonSerializer.Deserialize<JsonElement>(responseContent);
                        return jsonResponse.GetProperty("response").GetString() ?? "No response received.";
                    }
                    catch
                    {
                        // If parsing fails, return the raw response
                        return responseContent;
                    }
                }
                
                return "Sorry, I couldn't process your request at the moment.";
            }
            catch
            {
                return "Sorry, I couldn't connect to the AI service. Please make sure the Python API is running.";
            }
        }
    }
}
