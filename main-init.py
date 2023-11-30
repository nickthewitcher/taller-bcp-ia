from gpt4all import GPT4All

model = GPT4All("C:\\Users\\nickq\\AppData\\Roaming\\nomic.ai\\ggml-model-gpt4all-falcon-q4_0.bin", allow_download=False)

def process_question(prompt_text):
    try:
        print(f'User question: {prompt_text}')
        if len(prompt_text.strip()) == 0:
            print("Empty question. Please input again.")
        else:
            output = model.generate(prompt_text, max_tokens=200)
            print(f'GPT4All response: {output}')
    except Exception as e:
        print(f"Error processing question: {e}")

def main():
    print("Enter your text input or type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        process_question(user_input)

if __name__ == '__main__':
    main()
