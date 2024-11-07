import sys
import json
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load the pre-trained model and tokenizer
model_name = "tiiuae/falcon-40b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create a text generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)


def generate_listing(content):
    prompt = f"Create an Amazon product listing based on the following content:\n{content}\n\nProduct Listing:"
    output = generator(prompt, max_length=300, num_return_sequences=1)
    return output[0]['generated_text']


if __name__ == "__main__":
    # Read input from command line argument
    input_content = sys.argv[1]
    product_listing = generate_listing(input_content)

    # Print the generated product listing as JSON
    print(json.dumps({"listing": product_listing}))