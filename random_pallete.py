import sqlite3
import requests

def setup_database():
    conn = sqlite3.connect("palettes.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='palettes'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("ALTER TABLE palettes RENAME TO palettes_old")
    
    cursor.execute("""
        CREATE TABLE palettes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            color1 TEXT,
            color2 TEXT,
            color3 TEXT,
            color4 TEXT,
            color5 TEXT
        )
    """)

    if table_exists:
        cursor.execute("""
            INSERT INTO palettes (color1, color2, color3, color4, color5)
            SELECT color1, color2, color3, color4, color5 FROM palettes_old
        """)
        # Delete the old table
        cursor.execute("DROP TABLE palettes_old")

    conn.commit()
    conn.close()

def generate_random_palette(model_type):
    url = "http://colormind.io/api/"
    data = {"model": model_type}
    
    try:
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            if response.content.strip():
                result = response.json()
                if "result" in result:
                    colors = [tuple(color) for color in result["result"]]
                    return colors
                else:
                    raise Exception(f"Model '{model_type}' did not return valid data.")
            else:
                raise Exception(f"API response is empty for model '{model_type}'.")
        else:
            raise Exception(f"API error for model '{model_type}': {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Connection error with the API: {e}")
    except ValueError as e:
        raise Exception(f"Error processing JSON from API for model '{model_type}': {e}")

def save_palette_to_database(model_type, colors):
    conn = sqlite3.connect("palettes.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO palettes (model, color1, color2, color3, color4, color5)
        VALUES (?, ?, ?, ?, ?, ?)
    """, [model_type] + [str(color) for color in colors])
    conn.commit()
    conn.close()
    print("Palette saved to the database!")

def generate_palette_and_save_to_database(model_type):
    setup_database()
    print("Database configured.")
    
    try:
        colors = generate_random_palette(model_type)
        print("Generated palette:", colors)
        
        save_palette_to_database(model_type, colors)
        return colors
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    generate_palette_and_save_to_database("default")
