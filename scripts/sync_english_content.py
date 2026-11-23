#!/usr/bin/env python3
"""Keep the English dashboard structure aligned with the approved Turkish DOCX.

The existing English translation is retained by stable topic ID. This script
reorders moved topics, copies gallery metadata, carries paragraph alignment,
and applies the small translation updates introduced by the final Turkish copy.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def load_payload(path: Path):
    match = re.search(r"=\s*(\[.*\]);\s*$", path.read_text(encoding="utf-8"), re.S)
    if not match:
        raise ValueError(f"Could not read content payload: {path}")
    return json.loads(match.group(1))


def find_item(categories, item_id):
    for category in categories:
        for item in category["items"]:
            if item["id"] == item_id:
                return item
    raise KeyError(item_id)


def block_text(block):
    if block.get("type") == "list":
        return " ".join(
            "".join(run.get("text", "") for run in item)
            for item in block.get("items", [])
        )
    return "".join(run.get("text", "") for run in block.get("runs", []))


def replace_in_runs(item, old, new):
    for block in item.get("blocks", []):
        for run in block.get("runs", []):
            run["text"] = run.get("text", "").replace(old, new)
        for list_item in block.get("items", []):
            for run in list_item:
                run["text"] = run.get("text", "").replace(old, new)


def update_translation(content):
    urban_gardens = find_item(content, "kent-bostani")
    replace_in_runs(urban_gardens, "1,189 women", "1.2K women")
    urban_gardens["metrics"][1][0] = "1.2K"

    seed_centre = find_item(content, "ekolojik-kent-yerel-tohum-merkezi")
    seed_centre["blocks"] = [
        block
        for block in seed_centre["blocks"]
        if "220K summer seedlings" not in block_text(block)
    ]
    seed_centre["metrics"] = [
        metric for metric in seed_centre["metrics"] if metric[0] != "220K"
    ]

    employment = find_item(content, "altin-bilezik")
    replace_in_runs(employment, "NEARLY 1,000 JOB VACANCIES", "NEARLY 1K JOB VACANCIES")

    activity_centres = find_item(content, "cocuk-oyun-aktivite")
    replace_in_runs(activity_centres, "1,731 children", "1.7K children")
    activity_centres["metrics"][1][0] = "1.7K"

    belkahve = find_item(content, "belkahve")
    belkahve["lead"] = "TURNING WASTE INTO RESOURCES, AND RESOURCES INTO THE FUTURE"
    belkahve["blocks"][0]["runs"] = [
        {
            "text": (
                "In line with our sustainability vision, we established Belkahve Inc., "
                "a municipal subsidiary, to help return waste to the economy and strengthen "
                "the circular economy. Waste management begins where waste is generated. "
                "Under a defined collection programme, we collect waste separated by type "
                "from producers' premises and transport it in suitable vehicles to licensed "
                "facilities. At the facility, we weigh, inspect and record the waste. This "
                "allows us to track where the waste came from, how much there is and which "
                "process it is sent to."
            )
        }
    ]

    carbon = find_item(content, "bireysel-karbon-ayak-izi")
    replace_in_runs(carbon, "7,166 kg CO₂e", "7.1K kg CO₂e")
    replace_in_runs(carbon, "4,494 kg CO₂e", "4.5K kg CO₂e")
    replace_in_runs(carbon, "8,500 kg CO₂e", "8.5K kg CO₂e")
    carbon["metrics"][1][0] = "7.1K kg CO₂e"
    carbon["metrics"][2][0] = "4.5K kg CO₂e"
    carbon["metrics"][4][0] = "8.5K kg CO₂e"

    training = find_item(content, "atik-yonetimi-egitimleri")
    replace_in_runs(training, "1,369 people", "1.4K people")
    training["metrics"][0][0] = "1.4K"


def align_with_turkish(turkish, english):
    english_categories = {category["id"]: category for category in english}
    english_items = {
        item["id"]: item
        for category in english
        for item in category["items"]
    }
    aligned = []
    for turkish_category in turkish:
        english_category = english_categories[turkish_category["id"]]
        category = {
            **turkish_category,
            "title": english_category["title"],
            "items": [],
        }
        for turkish_item in turkish_category["items"]:
            item = english_items[turkish_item["id"]]
            item["galleryKeys"] = list(turkish_item.get("galleryKeys", [item["id"]]))
            if item.get("lead"):
                item["leadAlign"] = turkish_item.get("leadAlign", "justify")
            else:
                item.pop("leadAlign", None)
            for block in item.get("blocks", []):
                block["align"] = "justify"
            category["items"].append(item)
        aligned.append(category)
    return aligned


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--turkish", type=Path, required=True)
    parser.add_argument("--english", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    turkish = load_payload(args.turkish)
    english = load_payload(args.english)
    update_translation(english)
    aligned = align_with_turkish(turkish, english)

    payload = json.dumps(aligned, ensure_ascii=False, indent=2)
    output = (
        "// English translation aligned with the approved Turkish COP31 DOCX source.\n"
        "// Run scripts/sync_english_content.py after refreshing dist/content.js.\n"
        f"window.COP31_CONTENT_EN = {payload};\n"
    )
    args.out.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
