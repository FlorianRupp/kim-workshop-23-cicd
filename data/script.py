from rdflib import Graph, Literal
from rdflib.namespace import RDF, RDFS, Namespace
import xml.etree.ElementTree as ET


root = ET.parse("movies.xml")
root.findall(".//movie")

ONT = Namespace("http://example.org/ont/")
MOVIE_TYPE = ONT.Movie
MOVIES = Namespace("http://example.org/movie/")

movies = Graph()

for movie in root.findall(".//movie"):
    id = movie.get("id")
    movie_uri = MOVIES[id]
    movies.add((movie_uri, RDF.type, MOVIE_TYPE))

    for title in movie.findall("title"):
        movies.add((movie_uri, ONT.title, Literal(title.text)))
        movies.add((movie_uri, RDFS.label, Literal(title.text)))

    for rating in movie.findall("rating"):
        movies.add((movie_uri, ONT.rating, Literal(float(rating.text))))

    for canonical_title in movie.findall("canonical-title"):
        movies.add((movie_uri, ONT.canonical_title, Literal(canonical_title.text)))

    for long_imdb_title in movie.findall("long-imdb-title"):
        movies.add((movie_uri, ONT.long_imdb_title, Literal(long_imdb_title.text)))

    for top_250_rank in movie.findall("top-250-rank"):
        movies.add((movie_uri, ONT.top_250_rank, Literal(int(top_250_rank.text))))

    for year in movie.findall("year"):
        movies.add((movie_uri, ONT.year, Literal(int(year.text))))

    for plot_outline in movie.findall("plot-outline"):
        movies.add((movie_uri, ONT.plot_outline, Literal(plot_outline.text)))

    for plot in movie.findall("plot"):
        plot_items = " ".join(item.text for item in plot.findall("item"))
        movies.add((movie_uri, ONT.plot, Literal(plot_items)))

    for genre in movie.findall("genres"):
        for item in genre.findall("item"):
            movies.add((movie_uri, ONT.genre, Literal(item.text)))

movies.serialize("movies.ttl", format="turtle")
