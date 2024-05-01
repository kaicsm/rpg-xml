# rpg-xml
Uma biblioteca python que interpreta código XML para um RPG de texto no terminal.



https://github.com/kaicsalomao/rpg-xml/assets/68879185/074b1d70-4f8e-41c5-965a-b0c30907e0c3



Inicialmente, criei essa biblioteca como base para fazer um trabalho de sociologia: [marx-legacy](https://github.com/kaicsalomao/marx-legacy)


### Funções suportadas
- Colorizar o texto
- Controlar a velocidade de digitação 
- Aplicar uma pausa antes do texto ser impresso
- Músicas

### Dependências
Para reproduzir música é necessário ter o [MPV](https://mpv.io/) instalado no sistema.

### Como começar
1. Use `pip install rpg-xml` para instalar a biblioteca
2. Crie um arquivo python de nome de sua preferência e inicie a `Engine` passando como argumento o local do seu arquivo .xml:
```python
from rpg_xml import Engine

if __name__ == "__main__":
  eng = Engine("./src/game.xml")
  eng.start_game()
```

### O modelo do seu arquivo XML deve cumprir as seguintes regras
1. Iniciar com a tag `<game>...</game>`.
2. Você deve organizar todo o seu jogo em cenas (scenes) que se conectam umas com as outras.
3. Cada cena deve ter um id númerico definido pelo atributo `id`

##### exemplo de código:
```xml
<game>
  <scene id="1">
    ...
  </scene>
  <scene id="2">
    ...
  </scene>
</game>
```

### Tags disponíveis 
| TAG | FUNÇÃO | ATRIBUTOS |
| --- | --- | --- |
| `<msg>` | Imprime texto no terminal | `color`, `delay-before`, `type-vel`, `wrap-line` |
| `<clear/>` | Limpa o terminal (equivalente ao comando `clear` do linux) | - |
| `<option>` | Caixa de enquete. Deve conter outra tag chamada `<query>` | - |
| `<query>`| Define uma opção para uma enquete | `go-to` |
| `<music/>` | Reproduzir uma música | `play`, `stop` |

### Especificação dos atributos
#### Atributos da tag `<msg>`
- color: Define a cor do texto a ser impresso. As cores disponíveis atualmente são: `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `black`.

- delay-before: Define o tempo de pausa em milissegundos antes do texto ser impresso.

- type-vel: Define a velocidade de digitação do texto em milissegundos. 

- wrap-line: Define se o texto deve ou não quebrar linha. Pode ser "true" ou "false".

#### Atributos da tag `<query>`
- go-to: Define o ID da cena para a qual o jogo deve avançar quando essa opção for selecionada.

#### Atributos da tag `<music>`

- play: Especifica o caminho para o arquivo de música a ser reproduzido.

- stop: Define que a música que está em reprodução deve ser interrompida. Não recebe nenhum valor.

### Exemplo de uso das tags
```xml
<game>
  <scene id="1">
    <msg color="green" delay-before="500">Olá, mundo!</msg>
    <option>
      <query go-to="2">Continuar</query>
    </option>
  </scene>
  
  <scene id="2">
    <music play="./assets/musica.mp3"/>
    <msg delay-before="1000">Aqui está uma mensagem com uma pausa antes de ser exibida.</msg>
  </scene>
</game>
```

### Contribuições
Para quem quiser contribuir pesso que sempre mantenha as boas práticas de programação.
