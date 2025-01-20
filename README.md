# Color Palette Generator

This project provides a user-friendly interface for generating random color palettes using the [Colormind API](http://colormind.io/). Users can select from predefined models to create unique palettes, which are saved to a local SQLite database for future use. The project is built using Streamlit for the frontend and Python for backend operations.

---

## Features

- **Model Selection:** Choose from predefined models like `default`, `ui`, and `metroid_fusion` to generate palettes.
- **Random Palette Generation:** Generates five random colors using the selected model.
- **Database Integration:** Saves generated palettes to an SQLite database for persistence.
- **Visual Display:** Displays generated palettes in a visually appealing way with RGB color codes.

---

## Prerequisites

Before running the application, ensure the following dependencies are installed:

- Python 3.7 or later
- Required Python libraries:
  - `streamlit`
  - `requests`
  - `sqlite3` (built-in with Python)

Install the required libraries using pip:

```bash
pip install streamlit requests
```

---

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-repo/color-palette-generator.git
   cd color-palette-generator
   ```

2. Start the Streamlit application:

   ```bash
   streamlit run main.py
   ```

3. Open the application in your browser using the provided URL (usually `http://localhost:8501`).

---

## Project Structure

```
color-palette-generator/
├── main.py                    # Main Streamlit application
├── random_palette.py          # Module for generating and saving palettes
├── palettes.db                # SQLite database (auto-created)
└── README.md                  # Project documentation
```

---

## Usage

- Launch the application in your browser.
- Click on a model button (e.g., `Generate Default`) to create a palette.
- View the generated palette, including RGB codes, displayed visually.
- Palettes are automatically saved to the `palettes.db` SQLite database.

---

## Example

Below is an example of a generated palette:

| Color | RGB Code         |
|-------|------------------|
| ![#color1](https://via.placeholder.com/20/FF5733) | (255, 87, 51) |
| ![#color2](https://via.placeholder.com/20/33FF57) | (51, 255, 87) |
| ![#color3](https://via.placeholder.com/20/3357FF) | (51, 87, 255) |
| ![#color4](https://via.placeholder.com/20/FFFF33) | (255, 255, 51) |
| ![#color5](https://via.placeholder.com/20/33FFFF) | (51, 255, 255) |

---

## Troubleshooting

### Common Issues

1. **API Errors:** Ensure you have an active internet connection. If the API response is empty, verify the model name.

2. **Database Issues:** If there are problems with the database, delete the `palettes.db` file to reset it.

---

## Contributing

Contributions are welcome! If you'd like to add features or fix bugs, feel free to fork the repository and submit a pull request.

---

## Acknowledgments

- [Colormind API](http://colormind.io/) for providing random color palette generation.

