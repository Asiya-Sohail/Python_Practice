import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the pre-trained model and tokenizer
model_name = "t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Define a function to interact with me
def interact_with_me(input_text):
    # Tokenize the input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate a response
    output = model.generate(input_ids, max_length=100)

    # Decode the response
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response

# Test the function
input_text = "Hello, how are you?"
response = interact_with_me(input_text)
print(response)