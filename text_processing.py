import os
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def process_text(file_path):

    encodings = ['utf-8', 'latin-1', 'ISO-8859-1']

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                text = file.read()
                # Process the text using spaCy
                doc = nlp(text)

                # Example: Print named entities
                print("Named Entities:")
                for ent in doc.ents:
                    print(f"{ent.text} - {ent.label_}")

                # Other processing tasks can be added here

                # Break out of the loop if successful
                break
        except UnicodeDecodeError:
            print(f"Failed to decode using {encoding} encoding. Trying another encoding.")

if __name__ == "__main__":
    # Replace 'Downloads' with the actual path to your Downloads folder
    filename = os.path.expanduser("/Users/madisonkarcesky/Downloads/DailyWriting.pdf")

    # Process each text file in the Downloads folder
    #for filename in os.listdir(downloads_folder):
    if filename.endswith(".pdf"):  # Adjust the condition based on your file types
        file_path = os.path.join(filename)
        print(f"Processing: {filename}")
        process_text(file_path)
        print("\n" + "=" * 30 + "\n")
