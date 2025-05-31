import os
import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

nlp = spacy.load("en_core_web_sm")

def load_and_clean(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    start = text.find("*** START")  
    end = text.find("*** END")
    if start != -1 and end != -1:
        text = text[start:end]

    return text

def analyze_book(filepath, title):
    print(f"Analyzing: {title}")
    text = load_and_clean(filepath)
    doc = nlp(text)

    tokens = [
        token.lemma_.lower()
        for token in doc
        if token.is_alpha and not token.is_stop
    ]

    counts = Counter(tokens)
    top = counts.most_common(20)

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(counts)
    os.makedirs("plots", exist_ok=True)
    wordcloud.to_file(f"plots/{title}_wordcloud.png")

    df = pd.DataFrame(top, columns=["Word", "Frequency"])
    plt.figure(figsize=(10,5))
    plt.bar(df["Word"], df["Frequency"], color="skyblue")
    plt.title(f"Top Words in {title.title()}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"plots/{title}_barchart.png")
    plt.close()

    print(f"Saved plots for {title}")

def run_analysis():
    for filename in os.listdir("data/raw"):
        if filename.endswith(".txt"):
            filepath = os.path.join("data/raw", filename)
            title = filename.replace(".txt", "")
            analyze_book(filepath, title)

if __name__ == "__main__":
    run_analysis()
