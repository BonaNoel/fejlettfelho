using fejlettfelho.Models;
using System.Text.Json;

namespace fejlettfelho.Services
{
    public class OmdbService
    {
        private readonly HttpClient _httpClient;
        private readonly string _apiKey = "abc7180d";
        private readonly string _baseUrl = "https://www.omdbapi.com/";

        public OmdbService(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public async Task<MovieSearchResult> SearchMoviesAsync(string query)
        {
            try
            {
                var response = await _httpClient.GetStringAsync($"{_baseUrl}?apikey={_apiKey}&s={Uri.EscapeDataString(query)}");
                var result = JsonSerializer.Deserialize<MovieSearchResult>(response, new JsonSerializerOptions
                {
                    PropertyNameCaseInsensitive = true
                });
                return result ?? new MovieSearchResult();
            }
            catch
            {
                return new MovieSearchResult();
            }
        }

        public async Task<Movie> GetMovieDetailsAsync(string imdbId)
        {
            try
            {
                var response = await _httpClient.GetStringAsync($"{_baseUrl}?apikey={_apiKey}&i={imdbId}&plot=full");
                var result = JsonSerializer.Deserialize<Movie>(response, new JsonSerializerOptions
                {
                    PropertyNameCaseInsensitive = true
                });
                return result ?? new Movie();
            }
            catch
            {
                return new Movie();
            }
        }

        public async Task<Movie> GetMovieByTitleAsync(string title)
        {
            try
            {
                var response = await _httpClient.GetStringAsync($"{_baseUrl}?apikey={_apiKey}&t={Uri.EscapeDataString(title)}&plot=full");
                var result = JsonSerializer.Deserialize<Movie>(response, new JsonSerializerOptions
                {
                    PropertyNameCaseInsensitive = true
                });
                return result ?? new Movie();
            }
            catch
            {
                return new Movie();
            }
        }
    }
}
