#### Introdução

Estes códigos possuem como objetivo introduzir de uma forma simples, clara e objetiva as principais estruturas de dados, junto de comentários explicando o propósito do código.

Eu não vou estar colocando os mesmos comentários nos códigos de java, pois os códigos fazem práticamente a mesma coisa, a diferença sendo os inputs e a localização das funções.

Em breve vai ter comentários nos códigos das estruturas primitivas, e eu também vou fazer a Tupla em Java, ninguém é de ferro.

E por último, algumas poucas linhas de teste dos códigos (Arvore_de_Arquivos.py, Fila_de_Notificacoes.py, Grafo_de_Redes_Sociais.py) foram feitos por IA, mas isso é porque fazer a variedade necessária pra certos testes de forma única e distinta, rápidamente identificavel, faria ser lento fazer isso manualmente, e não possui relação alguma com o código, é apenas uma forma de testar ele de diferentes formas.

#### Ordem de Leitura

1. Anstratos/Node/
2. Anstratos/Lista_Encadeada/
3. Anstratos/Pilha/
4. Anstratos/Fila/
5. Anstratos/Árvore/
6. Anstratos/Grafo/Matriz
7. Anstratos/Grafo/Lista_Adjacente

##### Porque essa Ordem?

Em resumo: cada tópico vai construindo a partir do que você já sabe, e colocando uma camada de complexidade ou algo novo pra você aprender, indo de algo fácil e simples, a algo médio e complexo.

Essa é a recomendação da ordem de leitura pois, além dos comentários nos códigos seguirem uma ordem lógica, a forma como essa lista foi montada também segue uma ordem lógica.

O Node é a estrutura mais básica, mas também a mais versátil de todas, e a gente o usa pra fazer todas as outras (a não ser que você seja fã de arrays), e portanto é a primeira estrutura a ser estudada.

Já a lista encadeada serve como uma "demonstração" de como apontar nodes pra outros nodes, como adicionar novos valores e procurar por esses mesmos valores, algo que será extremamente útil pra aprender as próximas estruturas.

E por último, a Árvore fica antes do Grafo pois uma Árvore não é nada mais do que um Grafo simplificado. Em uma Árvore, não existe a possibilidade de ser feito um loop, diferente do Grafo, ja que na Árvore, cada node vai ter no máximo 1 conexão a ele, no Grafo porém, essa quantidade é ilimitada.