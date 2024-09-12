# rpg-xml
A Python library that interprets XML for a terminal-based RPG

### Supported Functions
- Text colorization
- Typing speed control
- Applying a pause before text is printed
- Music

### Dependencies
To play music, [MPV](https://mpv.io/) needs to be installed on the system.

### Getting Started
1. Use `pip install rpg-xml` to install the library
2. Create a Python file with a name of your choice and initiate the Engine, passing the location of your .xml file as an argument:
```python
from rpg_xml import Engine

if __name__ == "__main__":
  eng = Engine("./src/game.xml")
  eng.start_game()
```

### Your XML file model must comply with the following rules
1. Start with the tag `<game>...</game>`.
2. Organize your entire game into scenes that connect with each other.
3. Each scene must have a numeric id defined by the `id` attribute

##### Code example:
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

### Available Tags
| TAG | FUNCTION | ATTRIBUTES |
| --- | --- | --- |
| `<msg>` | Print text in the terminal | `color`, `delay-before`, `type-vel`, `wrap-line` |
| `<clear/>` | Clear the terminal (equivalent to the `clear` command in Linux) | - |
| `<option>` | Poll box. Must contain another tag called `<query>` | - |
| `<query>`| Define an option for a poll | `go-to` |
| `<music/>` | Play music | `play`, `stop` |

### Specification of Attributes
#### Attributes of the `<msg>` tag
- color: Defines the color of the text to be printed. Currently available colors are: `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `black`.

- delay-before: Defines the pause time in milliseconds before the text is printed.

- type-vel: Defines the typing speed of the text in milliseconds. 

- wrap-line: Defines whether the text should wrap or not. Can be "true" or "false".

#### Attributes of the `<query>` tag
- go-to: Defines the ID of the scene to which the game should advance when this option is selected.

#### Attributes of the `<music>` tag
- play: Specifies the path to the music file to be played.

- stop: Defines that the currently playing music should be stopped. It does not take any value.

### Example of Tag Usage
```xml
<game>
  <scene id="1">
    <msg color="green" delay-before="500">Hello world!</msg>
    <option>
      <query go-to="2">Continue</query>
    </option>
  </scene>
  
  <scene id="2">
    <music play="./assets/music.mp3"/>
    <msg delay-before="1000">A simple message with delay.</msg>
  </scene>
</game>
```
