# Bookbot! 🤖

Bookbot is a simple command-line program that reads in text from a file, and generates a statistical report about the text.

## Live Demo 🤹🏻‍♂️

- [Run Demo](https://replit.com/@tsoh/bookbot#main.py) - hosted on Replit.

## Installation 💾

In your command line clone this repo by typing:
`git clone git@github.com:ts-oh/bookbot.git`

## Run 🏃🏻‍♂️

1. cd into the bookbot directory: `cd bookbot`
2. Run the script by typing: `python main.py`

## Output 📄

You should see this as your output in your command line console:

```
+++ Begin report of ./books/the_bible_kjv.txt +++

824528 found in the document

The 'e' character was found 412514 times
The 't' character was found 317976 times
The 'h' character was found 282819 times
The 'a' character was found 275828 times
The 'o' character was found 243394 times
The 'n' character was found 225127 times
The 'i' character was found 194019 times
The 's' character was found 190146 times
The 'r' character was found 170388 times
The 'd' character was found 158124 times
The 'l' character was found 130020 times
The 'f' character was found 83598 times
The 'u' character was found 83508 times
The 'm' character was found 79962 times
The 'w' character was found 65508 times
The 'y' character was found 58595 times
The 'g' character was found 55326 times
The 'c' character was found 55110 times
The 'b' character was found 48900 times
The 'p' character was found 43312 times
The 'v' character was found 30368 times
The 'k' character was found 22326 times
The 'j' character was found 8903 times
The 'z' character was found 2975 times
The 'x' character was found 1479 times
The 'q' character was found 964 times

--- End report of ./books/the_bible_kjv.txt ---

Parsing time: 0.463 seconds!
```

## Options 📚

You can use your own text file to parse using the book bot. Simply copy your text file inside the `./books` directory.

Open main.py in your editor and assign the `book_path` variable with your text file `"./books/YOUR_TEXT_FILE.txt"`

It should look like this `book_path = "./books/YOUR_TEXT_FILE.txt"`

Once it's assigned, save it and run the script as instructed in installation section.
