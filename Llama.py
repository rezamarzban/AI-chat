from llama_cpp import Llama

# Path to your GGUF model file
model_path = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"

# Load the model
llama = Llama(model_path=model_path)

# Define the prompt
prompt = "What is short dipole antenna radiation resistance formula?"

# Generate response with specified max tokens
response = llama(prompt, max_tokens=200)  # Adjust max_tokens as needed

# Extract the final answer from the response
final_answer = response['choices'][0]['text'].strip()

# Print the final answer
print(final_answer)
