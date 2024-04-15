from sentence_transformers import SentenceTransformer, util

#define the categories we want to classify the text into
categories = [
    'multi-modal',
    'large language model',
    'security',
    'text',
    'image',
    'video'
]

# Load the model
model = SentenceTransformer("all-MiniLM-L6-v2")

def categorize_text(text:str) -> str:
    """
    Categorizes the given text into one of the predefined categories.

    Args:
        text (str): The text to be categorized.

    Returns:
        tuple: A tuple containing the category with the highest similarity score and the score itself.
    """
    # Tokenize the text
    text_embedding = model.encode(text, convert_to_tensor=True)

    # Compute the cosine similarity between the text and the categories
    category_embeddings = model.encode(categories, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(text_embedding, category_embeddings)[0]

    # Find the category with the highest similarity score
    max_score = cos_scores.max().item()
    max_score_index = cos_scores.argmax().item()

    return (categories[max_score_index], max_score)

# Test the function
print(categorize_text("Red Teaming GPT-4V: Are GPT-4V Safe Against Uni/Multi-Modal Jailbreak Attacks"))