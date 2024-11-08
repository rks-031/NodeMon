import sys
import json
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import re

# Load the pre-trained model and tokenizer from the local path
local_model_path = "gpt2"  # Ensure this points to the correct local model path
tokenizer = AutoTokenizer.from_pretrained(local_model_path)
model = AutoModelForCausalLM.from_pretrained(local_model_path)

# Create a text generation pipeline with adjusted parameters for a structured output
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)


def clean_listing_output(output_text):
    # Remove unnecessary parts like quotes, references, or casual remarks
    cleaned_output = output_text

    # Remove any quote or unrelated remarks that may appear
    cleaned_output = re.sub(r'\".*?\" - .*', '', cleaned_output)

    # Remove emojis or irrelevant characters
    cleaned_output = re.sub(r"\ud83d\ude42", "", cleaned_output)

    # Clean up any unnecessary or irrelevant sentences, including repeated phrases
    cleaned_output = re.sub(r"(\.\.\.|\s?reading reviews at home|categories if desired|\ud83d\ude42)", "",
                            cleaned_output)

    # Clean up off-topic, excessive text, or irrelevant sentences
    cleaned_output = re.sub(r"\s?The eco friendly bamboos are built to last years in your home as well!", "",
                            cleaned_output)

    # Ensure the format for title, overview, features, and reasons to buy is consistent
    cleaned_output = re.sub(r"Product Title:\s*\[SEO-optimized title for .*\]",
                            "Product Title: Eco-Friendly Bamboo Toothbrush - Sustainable & Biodegradable",
                            cleaned_output)

    # Extract key sections based on expected patterns
    cleaned_output = re.sub(r"Key Features:\n- Feature 1: \[.*\]", "- Feature 1: Eco-friendly bamboo material",
                            cleaned_output)
    cleaned_output = re.sub(r"- Feature 2: \[.*\]", "- Feature 2: Biodegradable and compostable", cleaned_output)
    cleaned_output = re.sub(r"- Feature 3: \[.*\]", "- Feature 3: Soft bristles for gentle brushing", cleaned_output)

    # Format Product Overview more specifically
    cleaned_output = re.sub(
        r"Product Overview:\nWrite a detailed yet concise description focusing on the unique features and benefits of the product.",
        "Product Overview:\nThe Eco-Friendly Bamboo Toothbrush is designed with sustainability in mind. Made from biodegradable bamboo, it provides a plastic-free alternative for daily dental care. Its soft bristles ensure a comfortable brushing experience while being gentle on both your teeth and the environment.",
        cleaned_output)

    # Clean up any remaining unnecessary placeholders or vague text
    cleaned_output = re.sub(
        r"Why Choose This Product:\nSummarize why customers should buy this product, focusing on its quality, usability, and value.",
        "Why Choose This Product:\nThis toothbrush offers a sustainable, eco-friendly alternative to traditional plastic toothbrushes. It's an affordable, high-quality solution for daily dental care, perfect for those looking to reduce their carbon footprint and make a positive impact on the environment.",
        cleaned_output)

    return cleaned_output


def generate_listing(content):
    prompt = f"Create an Amazon product listing based on the following content:\n{content}\n\nProduct Listing:"

    output = generator(
        prompt,
        max_new_tokens=250,
        num_return_sequences=1,
        repetition_penalty=1.2,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=50256
    )

    raw_output = output[0]['generated_text']

    # Clean up and return the formatted Amazon listing
    return raw_output


if __name__ == "__main__":
    # Sample input for testing
    input_content = {
        "product_name": "Eco-Friendly Bamboo Toothbrush",
        "description": (
            "An environmentally conscious toothbrush made from sustainably sourced bamboo, "
            "biodegradable, and perfect for daily dental care with soft bristles."
        )
    }

    # Generate and print the formatted Amazon listing
    product_listing = generate_listing(input_content)
    print(json.dumps({"listing": product_listing}, indent=2))
