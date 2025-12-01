import json
from pathlib import Path
from scripts.consolidate_reports import consolidate_reports
from scripts.clean_data import clean_data
from scripts.generate_summary import generate_summary

CONFIG_PATH = Path("config.json")

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def main():
    config = load_config()
    data_dir = Path(config["paths"]["data_dir"])
    output_dir = Path(config["paths"]["output_dir"])
    
    print("🚀 Starting Spreadsheet Automation Toolkit...\n")
    
    consolidated_path = consolidate_reports(data_dir, output_dir)
    cleaned_path = clean_data(consolidated_path, output_dir)
    final_report = generate_summary(cleaned_path, output_dir)
    
    print(f"✅ Pipeline finished successfully!\nReport generated at: {final_report}")

if __name__ == "__main__":
    main()
