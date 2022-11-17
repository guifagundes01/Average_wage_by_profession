# ChicoAI_case

This is a project made with Django.

## Objectives

The project's main objective was to build an API with Django to consult the average wage for a given occupation in Brasil.

## How it works?

To find the average wage for occupation was used web scrapping on the website www.salario.com.br, which has all the occupations of the CBO (Classificação Brasileira de Ocupações) and uses official data on more than 38 million wages.
The query can be made with the correct name of the occupation or with the CBO number for the occupation and returns the CBO number of the occupation, the official name of the occupation, and the average wage.

## Endpoints

```
/occupations/<str:cbo>                 views.cbo_detail      cbo_detail

```

## Examples

### Input

```
GET http://localhost:8000/occupations/Engenheiro eletrônico

```

### Output

```
{
    "data": {
        "Profissão": "Engenheiro eletrônico",
        "Média salarial": "R$ 9.062,70",
        "Código da CBO": "214310"
    }
}

```


## Possible improvements

The output could contain more information about the occupation, such as how much active workers have, the average hours of the workday, and "happiness" with the occupation.

About the consistency of the queries, could be made improvements for wrong spelling in the consult, or an inexistent CBO number.

Another idea that exists is to find also the average degree of education for an occupation, the average age, and the more "desired" occupations for the recruiters.

