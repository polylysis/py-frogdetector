# 🐸 py-frogdetector

**A Python tool to detect "frog", "toad", and "turtle" in text!**

## 🎯 Features:
✅ Detects **"frog"** (default)  
✅ Supports **multiple words** (`--word frog toad`)  
✅ **File input mode** (`--file <filename>`)  
✅ **Logging mode** (`--log`)  
✅ **Case-insensitive** search  

## 🚀 Installation:
Clone this repo and navigate into the project directory:
```sh
git clone https://github.com/yourusername/py-frogdetector.git
cd py-frogdetector
```

## 📃 Examples:
### 🐸 Detect Frogs:
```sh
python frogdetector.py "The frog jumps over the rock."
✅ Detected '1' instance(s) of 'frog' in the text! 🐸
```
### 🐸 Detect Toads
```sh
python frogdetector.py "A toad lives under the tree with a frog." --word toad
✅ Detected '1' instance(s) of 'toad' in the text! 🐸
```
### Detect Multiple
```sh
python frogdetector.py "The turtle, frog, and toad are here." --word frog toad turtle
✅ Detected '1' instance(s) of 'frog' in the text! 🐸
✅ Detected '1' instance(s) of 'toad' in the text! 🐸
✅ Detected '1' instance(s) of 'turtle' in the text! 🐸
```
### Analyse a text file
```sh
python frogdetector.py --file example.txt --word frog toad
✅ Detected '1' instance(s) of 'frog' in the text! 🐸
```
### Enable logging
```sh
python frogdetector.py "The frog and the toad met a turtle." --word frog toad --log
```
frogdetector.log:
```txt
2025-02-28 20:37:12,034 - Detected 1 'frog' occurrences.
2025-02-28 20:37:12,034 - Detected 1 'toad' occurrences.
2025-02-28 20:37:12,034 - Checked text: The frog and the toad met a turtle.... | Results: {'frog': 1, 'toad': 1}
```
### 🐸 HAPPY FROG, TOAD, & TURTLE HUNTING! 🐸
