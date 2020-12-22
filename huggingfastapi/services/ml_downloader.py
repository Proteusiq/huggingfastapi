'''
Directly download Hugging Face Model to a local directory
'''
import sys

def downloader():
    from transformers import AutoTokenizer
    from transformers import AutoModelForQuestionAnswering
    from transformers import pipeline

    from huggingfastapi.services.utils import ModelLoader
    from huggingfastapi.core.config import (
        DEFAULT_MODEL_PATH,
        QUESTION_ANSWER_MODEL
    )

    try:
        # Question Answer Model
        print(f"[+] Loading Question Answer Model: {QUESTION_ANSWER_MODEL}")
        qa_tokenizer, qa_model = ModelLoader(
            model_name=QUESTION_ANSWER_MODEL,
            model_directory=DEFAULT_MODEL_PATH,
            tokenizer_loader=AutoTokenizer,
            model_loader=AutoModelForQuestionAnswering,
        ).retrieve()
    except: # Any Error Exit
        sys.exit('Could not to download or load models!')

    # Test Loading and the Results
    context = "This is a tale of a tiny snail and a great big grey blue humpback whale"
    questions = ["What is the color of the humpback whale?", "What kind of a whale is it?"]

    nlp = pipeline("question-answering", model=qa_model, tokenizer=qa_tokenizer)

    print(f"\nTesting Question & Answers Using {QUESTION_ANSWER_MODEL}\n")
    for question in questions:
        QA_input = {"question": question, "context": context}
        response = nlp(QA_input)
        print(f"Question: {question}")
        print(f"Answer  : {response.get('answer')}")
        print(f"Details: {response}\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(download())
    
