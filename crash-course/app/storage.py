from pathlib import Path
import json


Data_Dir=Path("data")
Data_File=Data_Dir / "issues.json"

def load_data():
    if Data_File.exists():
        with open(Data_File,"r") as f:
            content=f.read()
            if content.strip():
                return json.loads(content)

    return []

def save_data(data):
    Data_Dir.mkdir(parents=True, exist_ok=True)
    with open(Data_File,"w") as f:
        json.dump(data, f, indent=2)