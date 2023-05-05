## Ontology Documentation

This is the documentation for the example used for the KIM-Workshop 2023 metadata hands-on session. Data about movies is represented as linked data.

This is used for the demonstration how to create a human-readable ontology documentation in Markdown and automatically extract it as turtle with Github workflow pipelines.
It has several benefits:
* human-readable.
* create ontology as turtle syntax automated with Github CI/CD.
* versioning.
* discussion adn issue management via the Github platform.
  * users can reference distinct lines in the ontology directly.


### Namespaces
The following namespaces are used in this ontology:

```
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/ont/>
```

### Character

```
ex:Character
    a rdfs:Class ;
    rdfs:label "Character"@en ;
    rdfs:comment "An entity describing a fictive character."@en ;
    rdfs:range rdfs:Resource .
```

### Company

```
ex:Company
    a rdfs:Class ;
    rdfs:label "Company"@en ;
    rdfs:comment "An entity describing a company creating moving."@en ;
    rdfs:range rdfs:Resource .
```


### Genre

```
ex:Genre
    a rdfs:Class ;
    rdfs:label "Genre"@en ;
    rdfs:comment "An entity describing a movie genre."@en ;
    rdfs:range rdfs:Resource .
```


### Movie

```
ex:Movie
    a rdfs:Class ;
    rdfs:label "Movie"@en ;
    rdfs:comment "An entity describing a movie."@en ;
    rdfs:range rdfs:Resource .
```

#### ex:hasCharacter
```
ex:hasCharacter
    a rdf:Property ;
    rdfs:label "has character"@en ;
    rdfs:comment "A character appearing in a movie."@en ;
    rdfs:range ex:Character .
```

#### ex:hasSideCharacter
```
ex:hasGenre
    a rdf:Property ;
    rdfs:label "has side character"@en ;
    rdfs:comment "A side character appearing in a movie."@en ;
    rdfs:range ex:Character .
```

#### ex:hasGenre
```
ex:hasGenre
    a rdf:Property ;
    rdfs:label "has genre"@en ;
    rdfs:comment "A genre the movie is associated with."@en ;
    rdfs:range ex:Genre .
```

### Person

```
ex:Person
    a rdfs:Class ;
    rdfs:label "Person"@en ;
    rdfs:comment "An entity describing an existing person."@en ;
    rdfs:range rdfs:Resource .
```

#### ex:plays
```
ex:plays
    a rdf:Property ;
    rdfs:label "plays"@en ;
    rdfs:comment "The character a person plays in a movie."@en ;
    rdfs:range ex:Character .
```