"""Prompt evaluation helpers for lesson 4 and 5."""

from __future__ import annotations

import json
import time
from typing import Callable

from tqdm.auto import tqdm


class RateLimitedIterator:
    def __init__(self, iterable, max_iterations_per_minute: int):
        self._iterable = iter(iterable)
        self._max_iterations_per_minute = max_iterations_per_minute
        self._min_interval = 1.0 / (max_iterations_per_minute / 60.0)
        self._last_yield_time = None

    def __iter__(self):
        return self

    def __next__(self):
        current_time = time.time()
        if self._last_yield_time is not None:
            elapsed = current_time - self._last_yield_time
            if elapsed < self._min_interval:
                time.sleep(self._min_interval - elapsed)
        self._last_yield_time = time.time()
        return next(self._iterable)


def evaluation(
    mail: dict,
    extract_func: Callable,
    categories: set,
    _print: bool = True,
    **kwargs,
) -> dict:
    response = extract_func(input=mail["message"], _print=_print, **kwargs)
    result = {
        "is_valid_json": False,
        "correct_categories": False,
        "correct_sentiment": False,
        "correct_urgency": False,
    }
    try:
        pred = json.loads(response)
    except json.JSONDecodeError:
        return result

    result["is_valid_json"] = True
    result["correct_categories"] = 1 - (
        len(set(mail["ground_truth"]["categories"]) ^ set(pred["categories"])) / len(categories)
    )
    result["correct_sentiment"] = pred["sentiment"] == mail["ground_truth"]["sentiment"]
    result["correct_urgency"] = pred["urgency"] == mail["ground_truth"]["urgency"]
    return result


def transpose_list_of_dicts(list_of_dicts: list[dict]) -> dict:
    keys = list_of_dicts[0].keys()
    transposed = {key: [] for key in keys}
    for item in list_of_dicts:
        for key, value in item.items():
            transposed[key].append(value)
    return transposed


def evalulation_full_dataset(
    dataset,
    func: Callable,
    categories: set,
    rate_limit: int = 100,
    _print: bool = False,
    **kwargs,
) -> dict:
    results = [
        evaluation(mail, func, categories, _print=_print, **kwargs)
        for mail in tqdm(RateLimitedIterator(dataset, rate_limit), total=len(dataset))
    ]
    results = transpose_list_of_dicts(results)
    for key, values in results.items():
        results[key] = sum(values) / len(dataset)
    return results


def pretty_print_table(data: dict) -> None:
    row_names = list(data.keys())
    if not row_names:
        return
    column_names = list(data[row_names[0]].keys())
    column_widths = [
        max(len(str(name)), max(len(f"{data[row][name]:.2f}") for row in row_names))
        for name in column_names
    ]
    row_name_width = max(len(str(name)) for name in row_names)
    header = f"{'':>{row_name_width}} " + " ".join(
        f"{name:>{width}}" for name, width in zip(column_names, column_widths)
    )
    print(header)
    print("=" * len(header))
    for row_name in row_names:
        row = f"{row_name:>{row_name_width}} " + " ".join(
            f"{data[row_name][name]:>{width}.1%}" for name, width in zip(column_names, column_widths)
        )
        print(row)
