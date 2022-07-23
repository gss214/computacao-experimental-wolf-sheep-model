# Projeto de Computação Experimental, por Guilherme Silva Souza

## Instalação

Para instalar as dependências use pip e requirements.txt no diretório raiz desse projeto.
```
    $ git clone https://github.com/gss214/computacao-experimental-wolf-sheep-model.git
    $ cd cd computacao-experimental-wolf-sheep-model 
    $ pip install -r requirements.txt
```

## Rodando o modelo

Para rodar o modelo digite o comando `mesa run server` no diretorio raiz do repositorio.

Abra seu navegador no endereço http://127.0.0.1:8521/ e pressione o botão `Start` para iniciar a simulação.

## Apresentação do modelo

O modelo Wolf Sheep Predation se baseia em um ecossistema que simula a situação de presa e predador. O funcionamento básico da simulação lobos e ovelhas vagam aleatoriamente pelo ecossistema, enquanto os lobos procuram ovelhas para se alimentar. Cada passo da simulação energia dos lobos é diminuída, e eles devem comer ovelhas para reabastecer suas energias, e quando ficam sem energia, eles morrem. Para permitir que a população continue, cada lobo ou ovelha tem uma probabilidade fixa de se reproduzir em cada passo de tempo. 
