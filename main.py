from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key= os.getenv("OPENAI_API_KEY")
)

# Start of the program
def welcome_message():
    print("Welcome to Samuria AI Content Generator (V1)")
    print("Samuria AI is a multi task AI generator powered by OpenAI.")

# Take user input and process it with AI
def start_ai():
    prompt = ""
    print("1-Generate Text (school work, emails, etc.)")
    print("2-Generate Ad")
    print("3-Generate Idea")
    print("_" * 50)
    print("4-Show Last Chats")

    text = input("Choose an option (1-4): ")

    if(text == "1"):
        topic = input("Write a social media post about: ")
        prompt = f"Write a social media post about{topic}"
    elif(text == "2"):
        product = input("Enter a product or service: ")
        prompt = f"Generate an ad for{product}"
    elif(text == "3"):        
        topic = input("Enter a topic or category: ")
        prompt = f"Generate an idea for{topic}"
    elif(text == "4"):
        show_last_chats()
        return
    else:     
        print("Invalid option. Please choose 1, 2, or 3.")

    result = generate_text(prompt=prompt)

    if result:
        print(result)
        save_result(prompt=prompt , result= result)
        continue_chatting()
    else:
        print("Failed to generate text.")

# save the result as json file 
# it save the prompt and the result in a json file with a timestamp as the filename
def save_result(prompt,  result):
    import json
    import time

    timestamp = int(time.time())
    filename = f"result_{timestamp}.json"

    data = {
        "prompt":prompt,
        "result": result
    }

    with open(filename, "w") as f:
        json.dump(data, f)

def show_last_chats():
    import os
    import json

    files = [f for f in os.listdir() if f.startswith("result_") and f.endswith(".json")]
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

    if not files:
        print("No previous chats found.")
        return

    print("Last 5 chats:")
    for file in files[:5]:
        with open(file, "r") as f:
            data = json.load(f)
            print(f"Prompt: {data['prompt']}")
            print(f"Result: {data['result']}")
            print("-" * 50)
    continue_chatting()

#countinue chating?
def continue_chatting():
    co = input("you wish to continue? (y/n)")
    if co.lower() == "y":
        start_ai()
    else:
        print("Goodbye!")

# Generate text using AI and return the result
def generate_text(prompt):
    print("Generating...")

    try:
        response = client.responses.create(
            model="gpt-5-nano",
            input=prompt,
            store=True,
        )

        print("AI Response:")
        return response.output_text

    except Exception as e:
        print(f"Error: {e}")
        return None

# Main function that starts the application
def main():
    welcome_message()
    start_ai()

# Run the app if this file is executed directly
if __name__ == "__main__":
    main()
