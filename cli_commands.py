
from generating_content import GeneratingContent
from save_content import SaveContent

class CLICommands:
    def __init__(self , generate , storge):
        self.generator = generate or GeneratingContent()
        self.storage = storge or SaveContent()

    def welcome_message(self):
        print("Welcome to Samuria AI Content Generator (V1)")
        print("Samuria AI is a multi task AI generator powered by OpenAI.")

    def start_ai(self):
        print("1-Generate Text (school work, emails, etc.)")
        print("2-Generate Ad")
        print("3-Generate Idea")
        print("_" * 50)
        print("4-Show Last Chats")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            topic = input("Write a social media post about: ")
            prompt = f"Write a social media post about {topic}"
        elif choice == "2":
            product = input("Enter a product or service: ")
            prompt = f"Generate a short, persuasive marketing ad for {product}. Make it catchy and engaging."
        elif choice == "3":
            topic = input("Enter a topic or category: ")
            prompt = f"Generate an idea for {topic}"
        elif choice == "4":
            self.storage.show_last_chats()
            # self.continue_chatting()
            return
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")
            return

        count = input("How many results do you want to generate? (default 1): ") or "1"
        count = int(count) if count.isdigit() and int(count) > 0 else 1

        for _ in range(count):
            result = self.generator.generate_text(prompt)
            if result:
                print("\n--- AI Response ---")
                print(result)
                self.storage.save_result(prompt, result)
            else:
                print("Failed to generate text.")

        self.continue_chatting()

    def continue_chatting(self):
        co = input("Do you wish to continue? (y/n): ")
        if co.lower() == "y":
            self.start_ai()
        else:
            print("Goodbye!")