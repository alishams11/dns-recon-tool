import json
import os
from datetime import datetime

def save_results(data, output_file="outputs/results.json"):
    os.makedirs("outputs", exist_ok=True)

    if not os.path.exists(output_file) or os.stat(output_file).st_size == 0:
        results = []
    else:
        with open(output_file, "r") as f:
            results = json.load(f)

    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": data
    }

    results.append(entry)

    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    print(f"[+] Results saved to {output_file}")
