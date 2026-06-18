"""Load facility support mail dataset and option lists."""

from __future__ import annotations

import json
from pathlib import Path

TUTORIAL_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = TUTORIAL_ROOT / "data"


def load_mails(filename: str = "filtered_mails-hardest.jsonl") -> list[dict]:
    path = DATA_DIR / filename
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def split_dataset(mails: list[dict]) -> tuple[list[dict], list[dict], list[dict]]:
    midpoint = len(mails) // 2
    dev_set = mails[:midpoint]
    test_set = mails[midpoint:]
    test_set_small = test_set[:20]
    return dev_set, test_set, test_set_small


def build_option_lists(mails: list[dict]) -> tuple[set, set, set, dict]:
    categories: set[str] = set()
    urgency: set[str] = set()
    sentiment: set[str] = set()
    for mail in mails:
        categories = categories.union(set(mail["ground_truth"]["categories"]))
        urgency.add(mail["ground_truth"]["urgency"])
        sentiment.add(mail["ground_truth"]["sentiment"])

    option_lists = {
        "urgency": ", ".join(f"`{entry}`" for entry in sorted(urgency)),
        "sentiment": ", ".join(f"`{entry}`" for entry in sorted(sentiment)),
        "categories": ", ".join(f"`{entry}`" for entry in sorted(categories)),
    }
    return categories, urgency, sentiment, option_lists
