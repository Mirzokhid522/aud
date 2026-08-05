import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN"))
database_id = os.getenv("DATABASE_ID")

try:
    response = notion.databases.query(database_id=database_id)
    results = response.get("results", [])
    
    print(f"Successfully connected! Found {len(results)} rows.\n")
    
    if results:
        print("--- Inspecting First Row Properties ---")
        props = results[0].get("properties", {})
        for prop_name, prop_data in props.items():
            print(f"Property Name: '{prop_name}' | Type: '{prop_data.get('type')}'")
    else:
        print("The database is empty. Add at least one row in Notion to inspect properties.")

except Exception as e:
    print(f"Connection failed: {e}")