# Trabalho 1 da disciplina Tópicos em Inteligência Artificial

## Problema do caixeiro viajante para um grafo totalmente conectado

### Problema

Dada a matriz de adjacência abaixo, faça um algoritmo genético que minimize o custo de um percurso do caixeiro viajante

|                  | Campo Grande | Bonito | Corumbá | Dourados | Camapuã | Água Clara |
|------------------|--------------|--------|---------|----------|---------|------------|
| **Campo Grande** |              |        |         |          |         |            |
| **Bonito**       | 325          |        |         |          |         |            |
| **Corumbá**      | 420          | 335    |         |          |         |            |
| **Dourados**     | 230          | 270    | 588     |          |         |            |
| **Camapuã**      | 143          | 285    | 563     | 373      |         |            |
| **Água Clara**   | 189          | 474    | 609     | 413      | 213     |            |

## Problema extra
Com o dataset encontrado em `states.json` baixado [daqui](https://github.com/llpinokio/tsp_dataset_brazilian_cities/blob/master/results/states_merged.json)
ache o melhor caminho do caixeiro viajante começando e terminando em "Mato Grosso do Sul" utilizando algorítmos genéticos.

melhor caminho encontrado:
```
Mato Grosso do Sul -> Rio Grande do Sul -> Santa Catarina -> 
Paraná -> São Paulo -> Rio de Janeiro -> Espírito Santo -> 
Minas Gerais -> Goiás -> Tocantins -> Ceará -> Rio Grande do Norte -> 
Paraíba -> Pernambuco -> Alagoas -> Sergipe -> Bahia -> Piauí -> Maranhão -> 
Pará -> Amapá -> Mato Grosso -> Rondônia -> Amazonas -> Roraima -> Acre -> 
Mato Grosso do Sul
```
custo : 14,519,563.74 Km