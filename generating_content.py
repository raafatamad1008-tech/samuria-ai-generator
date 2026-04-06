from openai import OpenAI
import os
from dotenv import load_dotenv

class GeneratingContent:

    def __init__(self):    
        load_dotenv()

        self.client = OpenAI(
            api_key= os.getenv("OPENAI_API_KEY")
        )

    def generate_text(self,  prompt):
        print("Generating...")

        try:
            response = self.client.responses.create(
                model="gpt-5-nano",
                input=prompt,
                # store=True,
            )

            print("AI Response:")
            return response.output_text

        except Exception as e:
            print(f"Error: {e}")
            return None
