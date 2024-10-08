PLN 2024 - Atividade 3:
=====================================
** Uso de Datasets Desbalanceados**
**Autor:** *Paulo M.*

# Descrição do Projeto
Este projeto faz parte da Atividade 3 da disciplina de Processamento de Linguagem Natural (PLN) de 2024. O objetivo é trabalhar com um dataset desbalanceado de no mínimo 10 mil registros e aplicar técnicas de aprendizado de máquina supervisionado e não supervisionado para resolver uma tarefa de classificação multiclasse.

# O projeto inclui:

* Pré-processamento dos dados utilizando Pandas.
* Implementação de modelos de classificação Naive Bayes com Scikit-learn.
* Utilização de embeddings de linguagem com GPT-2.
* Busca e indexação eficiente com FAISS.
* Avaliação de desempenho utilizando métricas Micro e Macro F1 Score.

## Dataset Utilizado
O dataset utilizado para esta atividade é o Fake News Dataset, contendo notícias com títulos, textos, e categorias associadas. Ele pode ser encontrado no seguinte link: [Fake News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

## Tecnologias e Bibliotecas Utilizadas
* Python 3.8+
* Pandas: Manipulação e análise de dados.
* Scikit-learn: Implementação do Naive Bayes e métricas de avaliação.
* Scikit-multilearn: Para realizar a divisão dos dados em conjuntos de treinamento, validação e teste.
* Hugging Face GPT-2: Geração de embeddings de linguagem.
* FAISS: Indexação e busca eficiente de embeddings.
* Matplotlib/Seaborn: Para visualização de gráficos.

## Etapas Realizadas
### (1) Carregamento e Análise dos Dados:
* Listagem dos campos e labels presentes no dataset.
* Contagem de registros com e sem labels.

### (2) Pré-processamento:
* Remoção de duplicados.
* Criação de novas colunas, como a que indica a presença ou ausência de labels.
* Concatenar campos textuais para otimizar a análise de texto.

### (3) Divisão do Dataset:
* Dividido em conjunto de treinamento, validação e teste utilizando Scikit-multilearn.

### (4) Classificação com Naive Bayes:
* Aplicação de Naive Bayes com OneVsRest para classificação multiclasse.
* Avaliação utilizando as métricas Micro e Macro F1 Score.

### (5) Embeddings com GPT-2 e Indexação FAISS:
* Geração de embeddings com GPT-2 para representações mais robustas dos textos.
* Indexação com FAISS e busca eficiente de registros similares.

### (6) Avaliação e Comparação de Resultados:
* Comparação entre os resultados do Naive Bayes e o modelo baseado em embeddings GPT-2, utilizando FAISS.