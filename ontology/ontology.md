## Ontology Documentation

This is a dummy ontology documentation used for the KIM-Workshop 2023 metadata hands-on session.

It is used for the demonstration how to create a human-readable ontology documentation in Markdown and automatically extract it as turtle with Github workflow pipelines.


### Namespaces
The following namespaces are used in this ontology:

```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
```

### MyPerson

Class: foaf:Person


#### foaf:name
```
foaf:name
    a rdf:Property ;
    rdfs:label "name"@en ;
    rdfs:comment "The full name of the person."@en ;
    rdfs:range rdfs:Literal .
```

#### foaf:birthday
```
foaf:birthday
    a rdf:Property ;
    rdfs:label "birthday"@en ;
    rdfs:comment "The date the person was born"@en ;
    rdfs:range rdfs:Literal .
```
