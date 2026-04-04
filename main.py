from openai import OpenAI

client = OpenAI(
    api_key="OPENAI_API_KEY"
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

    text = input("Choose an option (1-3): ")

    if(text == "1"):
        prompt = f"Write a social media post about{input("Write a social media post about: ")}"
    elif(text == "2"):
        prompt = f"Generate an ad for{input("Enter a product or service: ")}"
    elif(text == "3"):        
        prompt = f"Generate an idea for{input("Enter a topic or category: ")}"
    else:     
        print("Invalid option. Please choose 1, 2, or 3.")

    result = generate_text(prompt=prompt)

    if result:
        print(result)
    else:
        print("Failed to generate text.")

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
