# Bookbot! 🤖

Bookbot is a simple command-line program that reads in text from a file, and generates a statistical report about the text.

## Live Demo 🤹🏻‍♂️

- [Run Demo](https://replit.com/@tsoh/bookbot#main.py) - hosted on Replit.

## Installation 💾

In your command line clone this repo by typing or copy pasting following command: `git clone git@github.com:ts-oh/bookbot.git`

## Run 🏃🏻‍♂️

1. cd into the bookbot directory: `cd bookbot`
2. Run the script by typing: `python main.py`

## Output 📄

You should see something like this as your output in your command line console:

```
+++ Begin report of ./books/the_odyssey.txt +++

132606 words found in the document

The 'e' character was found 68550 times
The 't' character was found 46972 times
The 'o' character was found 44271 times
The 'a' character was found 42667 times
The 'h' character was found 38673 times
The 'n' character was found 36461 times
The 's' character was found 35913 times
The 'i' character was found 33625 times
The 'r' character was found 29799 times
The 'd' character was found 23303 times
The 'l' character was found 21475 times
The 'u' character was found 17335 times
The 'm' character was found 14542 times
The 'w' character was found 14397 times
The 'y' character was found 12359 times
The 'f' character was found 11996 times
The 'g' character was found 11185 times
The 'c' character was found 10414 times
The 'p' character was found 8053 times
The 'b' character was found 7705 times
The 'v' character was found 5450 times
The 'k' character was found 4174 times
The 'x' character was found 562 times
The 'j' character was found 549 times
The 'q' character was found 299 times
The 'z' character was found 152 times

and so on...

--- End report of ./books/the_odyssey.txt ---

⏱️ Parsing time: 0.128 seconds!
```

## Options 📚

You can use your own text file to parse using the book bot. Simply copy your text file inside the `./books` directory.

**Update:** Now the program will prompt you to type out the name of the text file that you would like to parse. Just simply keep your text files in the `./books` directory like before. Furthermore, it should list out available books in the directory for your convinience.

<s>Open main.py in your editor and assign the `book_path` variable with your text file `"./books/YOUR_TEXT_FILE.txt"`

It should look like this `book_path = "./books/YOUR_TEXT_FILE.txt"`

Once it's assigned, save it and run the script as instructed in installation section.</s>


