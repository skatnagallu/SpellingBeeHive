# Spelling Bee Solver

A Python-based solver for the NYT Spelling Bee puzzle, featuring a command-line interface and a Flask web application.

## Features

- **Solver Logic**: Efficiently finds words from the system dictionary that match Spelling Bee criteria.
- **Web Interface**: Clean, modern web app to interact with the solver.
- **Live Demo**: [Try it now on Render](https://spellingbeehive.onrender.com)
- **Definitions**: Click on any found word to see its definition (powered by Free Dictionary API).
- **Pangram Detection**: Highlights words that use all 7 letters.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd SpellingBeeHive
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Web App
1. Start the server:
   ```bash
   python3 app.py
   ```
   Or for production:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5001 app:app
   ```

2. Open your browser to `http://localhost:5001`.

### Command Line
Run the solver script directly:
```bash
python3 solver.py
```

### Deployment

#### Render (Recommended)
1. Fork or clone this repository to your GitHub.
2. Log in to [Render](https://render.com/).
3. Click "New +" and select "Web Service".
4. Connect your GitHub repository.
5. Render will automatically detect the `render.yaml` file and configure the service.
6. Click "Create Web Service".

Your app will be live in a few minutes!

## License

MIT License
