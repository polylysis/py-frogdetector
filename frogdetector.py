import re
import argparse
import logging

# Configure logging
logging.basicConfig(filename="frogdetector.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def detect_words(text, words):
    """
    Detect occurrences of multiple words in the given text.
    """
    results = {}

    for word in words:
        pattern = rf'\b{word}\b'  # Match whole word only
        matches = re.findall(pattern, text, re.IGNORECASE)
        results[word] = len(matches)

    return results

def main():
    # Setup command-line argument parsing
    parser = argparse.ArgumentParser(description="Detect occurrences of 'frog', 'toad', and 'turtle' in text.")
    parser.add_argument("text", nargs="?", help="The input text to analyze (if not using --file)")
    parser.add_argument("--word", nargs="+", choices=["frog", "toad", "turtle"], default=["frog"], help="Words to detect")
    parser.add_argument("--file", help="Path to a text file to analyze")
    parser.add_argument("--log", action="store_true", help="Enable logging of detections")

    args = parser.parse_args()

    # Read text from file if provided
    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print(f"❌ Error: File '{args.file}' not found.")
            return
    elif args.text:
        text = args.text
    else:
        print("❌ Error: No input provided. Use --file <filename> or provide text.")
        return

    # Run detection for all specified words
    results = detect_words(text, args.word)

    # Print and log results
    found_any = False
    for word, count in results.items():
        if count > 0:
            print(f"✅ Detected '{count}' instance(s) of '{word}' in the text! 🐸")
            found_any = True
            if args.log:
                logging.info(f"Detected {count} '{word}' occurrences.")

    if not found_any:
        print("❌ No target words found.")

    if args.log:
        logging.info(f"Checked text: {text[:50]}... | Results: {results}")

if __name__ == "__main__":
    main()

