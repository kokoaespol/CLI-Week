# helpmeai: a cli tool to help you with fast queries while coding

helpmeai is a CLI tool made in Python that can fundamentally do three things: generate code, search on the internet, and propose solutions to some problems in a file that you want.

## Installation

To install this CLI, you will need Python, pip, and Git installed on your machine. After that, you can run the following command:

```
git clone https://github.com/brauliorivas/CLI-Week.git ~/.helpmeai
```

After that, you will need to install the requirements in a virtual environment. To do that, you can run the following command:

```
cd ~/.helpmeai/src/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

However, as this cli uses serpapi and textcortex api, you should create a free account on both platforms. 
Then, with the API keys, you can run 

```
cp ~./helpmeai/src/.env.example ~/.helpmeai/src/.env

```
And replace the cli's api keys in .env with your own.

Finally, you can add an alias to your `.bashrc` or `.zshrc` (depending on your config) file to run the CLI from anywhere on your machine. To do that, you can run the following command:

```
echo "alias helpmeai='python ~/.helpmeai/src/cli.py'" >> ~/.bashrc 
```

## Usage

Commands:
```
code    Chatgpt will transform your nl prompt into code
        Options:
            -l, --language TEXT  The language you want to use
search  Search the internet for information and get a summarized answer
        Options:
            -l, --language TEXT  The language you want to use
            -c, --country TEXT   The country you want to use
solve   Open a file, address a problem, and get a solution
        Options:
            -p, --path TEXT   The path to the file you want to open  [required]
            -l, --lines TEXT  The lines where the problem is, format start:end [required]
```

## Examples

```
helpmeai code -l py "make function to sum two values"
```
```python
def sum_values(val1, val2):
    return val1 + val2
```

```bash
helpmeai search -l en -c ec "what is docker"
```
```text
Docker is a platform designed to help developers build, share, and run modern applications. We handle the tedious setup, so you can focus on the code.
```



```bash
helpmeai solve -p ./test.js -l 1:5 "The code is not multiplying, the numbers, what should I do?"
```

```javascript
function multiply(a, b) {
  return a * b;
}
console.log(multiply(2, 3));
```

## License

MIT License