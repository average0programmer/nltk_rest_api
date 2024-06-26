import nltk
import os


def setup():
    download_dir = os.path.join(os.getcwd(), 'api', 'services', 'nltk_data') # directory to download necessary resources
    nltk.download('punkt', quiet=True, download_dir=download_dir)
    nltk.download('averaged_perceptron_tagger', quiet=True, download_dir=download_dir)
    nltk.download('maxent_ne_chunker', quiet=True, download_dir=download_dir)
    nltk.download('words', quiet=True, download_dir=download_dir)


def tokenize_text(text: str):
    return nltk.word_tokenize(text)


def pos_tagging(text: str):
    setup()

    tokenized_text = tokenize_text(text)
    pos_tags = nltk.pos_tag(tokenized_text)
    return pos_tags


def extract_named_entities(tree):
    named_entities = []
    for subtree in tree:
        if hasattr(subtree, 'label'):
            entity_name = ' '.join(s[0] for s in subtree)
            entity_type = subtree.label()
            named_entities.append((entity_name, entity_type))
    return named_entities


def entity_recognition(text: str):
    pos_tagged_text = pos_tagging(text)
    named_entities_tree = nltk.ne_chunk(pos_tagged_text)
    named_entities = extract_named_entities(named_entities_tree)
    return named_entities
