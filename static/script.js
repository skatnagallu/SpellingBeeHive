document.addEventListener('DOMContentLoaded', () => {
    const centralInput = document.getElementById('central');
    const othersInput = document.getElementById('others');
    const solveBtn = document.getElementById('solve-btn');
    const resultsArea = document.getElementById('results-area');
    const wordCount = document.getElementById('word-count');
    const wordList = document.getElementById('word-list');

    const modal = document.getElementById('definition-modal');
    const modalWord = document.getElementById('modal-word');
    const modalBody = document.getElementById('modal-body');
    const closeBtn = document.querySelector('.close-btn');

    solveBtn.addEventListener('click', async () => {
        const central = centralInput.value.trim();
        const others = othersInput.value.trim();

        if (!central || central.length !== 1) {
            alert('Please enter a single central letter.');
            return;
        }

        if (!others) {
            alert('Please enter other letters.');
            return;
        }

        solveBtn.textContent = 'Buzzing...';
        solveBtn.disabled = true;

        try {
            const response = await fetch('/api/solve', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ central, others })
            });

            const data = await response.json();

            if (response.ok) {
                displayResults(data.words);
            } else {
                alert(data.error || 'An error occurred.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to fetch results.');
        } finally {
            solveBtn.textContent = 'Solve Puzzle';
            solveBtn.disabled = false;
        }
    });

    function displayResults(words) {
        wordList.innerHTML = '';
        wordCount.textContent = words.length;
        resultsArea.classList.remove('hidden');

        words.forEach((item, index) => {
            const li = document.createElement('li');
            li.textContent = item.word;
            li.className = 'word-item';
            if (item.is_pangram) {
                li.classList.add('pangram');
                li.title = 'Pangram!';
            }
            // Stagger animation
            li.style.animationDelay = `${index * 0.03}s`;

            // Add click event for definition
            li.addEventListener('click', () => showDefinition(item.word));

            wordList.appendChild(li);
        });
    }

    async function showDefinition(word) {
        modal.classList.remove('hidden');
        modalWord.textContent = word;
        modalBody.innerHTML = '<p>Loading definition...</p>';

        try {
            const response = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`);
            const data = await response.json();

            if (response.ok && Array.isArray(data) && data.length > 0) {
                const entry = data[0];
                let html = '';

                if (entry.phonetics && entry.phonetics.length > 0) {
                    const text = entry.phonetics.find(p => p.text)?.text;
                    if (text) {
                        html += `<p style="color: #888; margin-bottom: 1rem;">${text}</p>`;
                    }
                }

                entry.meanings.forEach(meaning => {
                    html += `<div class="definition-item">
                        <span class="part-of-speech">${meaning.partOfSpeech}</span>`;

                    meaning.definitions.slice(0, 2).forEach((def, i) => {
                        html += `<p class="definition-text">${i + 1}. ${def.definition}</p>`;
                    });

                    html += `</div>`;
                });

                modalBody.innerHTML = html;
            } else {
                modalBody.innerHTML = '<p>No definition found.</p>';
            }
        } catch (error) {
            console.error('Error fetching definition:', error);
            modalBody.innerHTML = '<p>Failed to load definition.</p>';
        }
    }

    closeBtn.addEventListener('click', () => {
        modal.classList.add('hidden');
    });

    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.classList.add('hidden');
        }
    });
});
