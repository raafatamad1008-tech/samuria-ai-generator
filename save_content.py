import json
import time
import os

    
class SaveContent:
    
    # save the result as json file 
    # it save the prompt and the result in a json file with a timestamp as the filename
    def save_result(self,  prompt,  result):

        timestamp = int(time.time())
        os.makedirs("results", exist_ok=True)
        filename = f"results/result_{timestamp}.json"

        data = {
            "prompt":prompt,
            "result": result
        }

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def show_last_chats(self):
     

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
        
