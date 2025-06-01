## MiniCorpus: Analyzing Lemmatized Word Frequencies in Classic Children’s Literature
This is a simple NLP project created to explore common word usage in classic children's literature.

### 📚 Books Analyzed
- Pollyanna by Eleanor H. Porter
- Winnie-the-Pooh by A. A. Milne
- Peter Pan by J. M. Barrie

### Project Overview
- Scrapes full text of the books from Project Gutenberg
- Tokenizes and lemmatizes text using spaCy
- Removes stopwords and punctuation
- Generates:
  - Word frequency bar charts
  - Word clouds as PNG images


### How to Run

git clone https://github.com/thecognicode/mini_corpus_project.git

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python -m spacy download en_core_web_sm



### Special Thanks

Thanks to Project Gutenberg for making Pollyanna by Eleanor H. Porter, Winnie-the-Pooh by A. A. Milne, and Peter Pan by J. M. Barrie freely available to the public.


