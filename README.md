# Typer
<p>
Simple program to simulate typing effect animation just like <a href="https://steven.codes/typerjs">Typer.JS</a> but in CLI
</p>
<p>Coded in python. Compiled to binary with <a href="https://pyinstaller.org">pyinstaller</a></p>

<p>Installing and simple demo 👇</p>
<img src="./preview/demo.svg">
<em>yes i made this in <a href="https://termux.com">Termux</a> 🙃</em>
Installation:
```bash
git clone https://github.com/msn-05/typer
cd typer
chmod +x install
./install
```
This will install typer.
Usage:
```
typer [-h] [-delay DELAY]
             [-delete_delay DELETE_DELAY]
             [-words_delay WORDS_DELAY] [-start START]
             words [words ...]

A simple program to simulate animated typing effect
like Typer.JS

positional arguments:
  words                 The words to be typed

optional arguments:
  -h, --help            show this help message and
                        exit
  -delay DELAY          Time delay between typed
                        characters (in ms)
  -delete_delay DELETE_DELAY
                        Time delay between deleted
                        characters (in ms)
  -words_delay WORDS_DELAY
                        Time delay between typed words
                        (in ms)
  -start START          The starting word or sentence
```
