import csv
import random

sources = ["IDX Market", "Jakarta Wire", "Asia Macro", "Equity Pulse", "Tech Times", "Gov Finance"]

with open('/mnt/2AA67636A676031D/Katalis/backend/data/sample_train.csv', 'r') as f_in, open('/mnt/2AA67636A676031D/Katalis/backend/data/sample_seed.csv', 'w', newline='') as f_out:
    reader = csv.DictReader(f_in)
    writer = csv.DictWriter(f_out, fieldnames=['source', 'title', 'sentiment'])
    writer.writeheader()
    for row in reader:
        writer.writerow({
            'source': random.choice(sources),
            'title': row['text'],
            'sentiment': row['label']
        })
