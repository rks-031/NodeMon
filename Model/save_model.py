from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "gpt2"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Save the model locally
model.save_pretrained("./saved_model")
tokenizer.save_pretrained("./saved_model")

print("Model saved to ./saved_model")