# ChicoAI_case

This is a project made with Django.

## Objectives

The main objective of the project was to build an API with Django to consult the average wage for a given occupation in Brasil.

## How it works?

To find the average wage for a occupation was used web scrapping in the website www.salario.com.br, which has all the occupations of the CBO (Classificação Brasileira de Ocupações) and uses oficial data in more than 38 million of wages.
The query can be made with the correct name of the occupation or with the CBO number for the occupation and returns the CBO number of the occupation, the official name of the occupation and the average wage.

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

The output could contain more informations about the occupation, such as how much active workers has, the average hours of workday, "happiness" with the occupation.

About the consistent of the querys, could be made improvements for wrong spelling in the consult, or a inexistent CBO number.

Other ideas that exists is to find also the average degree of eductaion for a occupation, average age, the more "desired" occupations for the recruiters.

