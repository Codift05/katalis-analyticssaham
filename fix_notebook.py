import json

path = '/mnt/2AA67636A676031D/Katalis/Model_Prototipe_Katalis.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Check if the install cell is already there
new_cell = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "import sys\n",
        "!{sys.executable} -m pip install pandas numpy matplotlib scikit-learn"
    ]
}

# insert it at the second position, right after the markdown header
nb['cells'].insert(1, new_cell)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated.")
