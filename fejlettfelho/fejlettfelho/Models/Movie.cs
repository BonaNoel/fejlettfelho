namespace fejlettfelho.Models
{
    public class Movie
    {
        public string Title { get; set; } = string.Empty;
        public string Year { get; set; } = string.Empty;
        public string ImdbId { get; set; } = string.Empty;
        public string Type { get; set; } = string.Empty;
        public string Poster { get; set; } = string.Empty;
        public string Plot { get; set; } = string.Empty;
        public string Director { get; set; } = string.Empty;
        public string Actors { get; set; } = string.Empty;
        public string Genre { get; set; } = string.Empty;
        public string Rating { get; set; } = string.Empty;
        public string Runtime { get; set; } = string.Empty;
        public string Released { get; set; } = string.Empty;
    }

    public class MovieSearchResult
    {
        public List<Movie> Search { get; set; } = new();
        public string TotalResults { get; set; } = string.Empty;
        public string Response { get; set; } = string.Empty;
    }

    public class ChatMessage
    {
        public string Text { get; set; } = string.Empty;
        public bool IsUser { get; set; }
        public DateTime Timestamp { get; set; } = DateTime.Now;
        public List<Movie>? Movies { get; set; }
    }
}
