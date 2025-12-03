from flask import Flask, render_template, request, jsonify
from solver import load_words, solve

app = Flask(__name__)

# Load words once at startup
print("Loading dictionary...")
WORDS = load_words()
print(f"Dictionary loaded with {len(WORDS)} words.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/solve', methods=['POST'])
def solve_puzzle():
    data = request.get_json()
    central = data.get('central')
    others = data.get('others')

    if not central or len(central) != 1 or not central.isalpha():
        return jsonify({'error': 'Invalid central letter'}), 400
    
    if not others or not others.isalpha():
        return jsonify({'error': 'Invalid other letters'}), 400

    found_words = solve(central, others, WORDS)
    
    results = []
    for word in found_words:
        is_pangram = set(word) == set(central.lower() + others.lower())
        results.append({
            'word': word,
            'is_pangram': is_pangram,
            'length': len(word)
        })
    
    # Sort by length (descending) then alphabetical
    results.sort(key=lambda x: (-x['length'], x['word']))

    return jsonify({'words': results})

if __name__ == '__main__':
    # Use environment variable for debug mode, default to False in production
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, port=5001)
