import pickle

def load_fact_checks_embeddings(model_name):
    with open(f"./data/embeddings/fact_checks_embeddings/{model_name}/fact_checks_embeddings.pkl", "rb") as file:
        fact_checks_embeddings = pickle.load(file)
    return fact_checks_embeddings