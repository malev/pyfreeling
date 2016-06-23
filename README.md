# PyFreeling

Freeling wrapper. Works around the `analize` command line tool.
It will return a `lxml` object.

## Installation

```
pip install pyfreeling
```

or

```
conda install pyfreeling -c malev
```

## Usage

```
from pyfreeling import Analyzer

analyzer = Analyzer(config='config.cfg')
xml = analyzer.run('Hello World')

analyzer = Analyzer(config='config.cfg', lang='es')

analyzer.run('Hola mundo', 'noflush')
```

All the options [here](https://talp-upc.gitbooks.io/freeling-user-manual/content/analyzer.html)
are available as optional arguments for the `run` method. There are more examples [here](https://github.com/malev/pyfreeling/blob/master/examples.ipynb).
