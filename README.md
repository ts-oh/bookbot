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
The 'ο' character was found 42 times
The 'ν' character was found 37 times
The 'τ' character was found 31 times
The 'α' character was found 29 times
The 'σ' character was found 26 times
The 'ρ' character was found 25 times
The 'π' character was found 23 times
The 'έ' character was found 19 times
The 'ε' character was found 19 times
The 'ι' character was found 18 times
The 'δ' character was found 15 times
The 'λ' character was found 15 times
The 'ς' character was found 12 times
The 'μ' character was found 11 times
The 'κ' character was found 9 times
The 'η' character was found 8 times
The 'γ' character was found 8 times
The 'θ' character was found 7 times
The 'ό' character was found 7 times
The 'ί' character was found 7 times
The 'ὶ' character was found 7 times
The 'φ' character was found 6 times
The 'ὄ' character was found 6 times
The 'ἀ' character was found 6 times
The 'ἐ' character was found 5 times
The 'ω' character was found 5 times
The 'ἰ' character was found 5 times
The 'υ' character was found 4 times
The 'ὼ' character was found 4 times
The 'χ' character was found 3 times
The 'ύ' character was found 3 times
The 'æ' character was found 3 times
The 'ῖ' character was found 3 times
The 'ῥ' character was found 3 times
The 'ῇ' character was found 3 times
The 'ῳ' character was found 2 times
The 'ῶ' character was found 2 times
The 'ά' character was found 2 times
The 'ἦ' character was found 2 times
The 'ὦ' character was found 2 times
The 'ἄ' character was found 2 times
The 'ἔ' character was found 2 times
The 'ζ' character was found 2 times
The 'ὺ' character was found 2 times
The 'ή' character was found 2 times
The 'ù' character was found 2 times
The 'ὀ' character was found 2 times
The 'ῆ' character was found 1 times
The 'ώ' character was found 1 times
The 'ὡ' character was found 1 times
The 'ἷ' character was found 1 times
The 'ἠ' character was found 1 times

--- End report of ./books/the_odyssey.txt ---

Parsing time: 0.075 seconds!
```

## Options 📚

You can use your own text file to parse using the book bot. Simply copy your text file inside the `./books` directory.

**Update:** Now the program will prompt you to type out the name of the text file that you would like to parse. Just simply keep your text files in the `./books` directory like before.

<s>Open main.py in your editor and assign the `book_path` variable with your text file `"./books/YOUR_TEXT_FILE.txt"`

It should look like this `book_path = "./books/YOUR_TEXT_FILE.txt"`

Once it's assigned, save it and run the script as instructed in installation section.</s>


