"""Generate RenderCV inputs for every CV variant and language from cv/master.yaml.

Usage:
    python scripts/build_cvs.py            # write generated/*.yaml
    python scripts/build_cvs.py --render   # also render PDFs (and HTML/Markdown for the generic CV)

Outputs:
    generic EN -> build/Fabrizio_Dante_Pauselli.pdf, build/index.html, build/README.md (published to gh-pages)
    generic ES -> build/Fabrizio_Dante_Pauselli_ES.pdf, build/es.html, build/README_ES.md (published to gh-pages)
    variants   -> dist/Fabrizio_Dante_Pauselli_<Variant>[_ES].pdf (local only, not published)
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "cv" / "master.yaml"
GENERATED = ROOT / "generated"
SCHEMA = "https://raw.githubusercontent.com/rendercv/rendercv/refs/tags/v2.8/schema.json"
FILE_STEM = "Fabrizio_Dante_Pauselli"
LANGUAGES = ("en", "es")
META_KEYS = {"in", "rank", "id"}

yaml = YAML()
yaml.width = 4096
yaml.allow_unicode = True


def text(value, lang):
    """Resolve a value that is either language-neutral or a {en, es} mapping."""
    if isinstance(value, dict) and set(value) <= set(LANGUAGES):
        return value[lang]
    return value


def select(items, variant):
    """Keep the items tagged for this variant, ordered by their per-variant rank."""
    kept = [
        (index, item)
        for index, item in enumerate(items)
        if not isinstance(item, dict) or variant in item.get("in", [variant])
    ]
    def key(pair):
        index, item = pair
        rank = item.get("rank", {}).get(variant) if isinstance(item, dict) else None
        return (rank if rank is not None else 1000, index)
    return [item for _, item in sorted(kept, key=key)]


def entry(item, variant, lang):
    """Turn a master entry into a RenderCV entry for one variant and language."""
    result = {}
    for field, value in item.items():
        if field in META_KEYS:
            continue
        if field == "highlights":
            highlights = [text(h if isinstance(h, str) else {k: h[k] for k in LANGUAGES}, lang)
                          for h in select(value, variant)]
            if highlights:
                result[field] = highlights
        else:
            result[field] = text(value, lang)
    return result


def render_settings(variant, lang, stem):
    if variant == "generic":
        suffix = "" if lang == "en" else "_ES"
        return {
            "dont_generate_png": True,
            "pdf_path": f"../build/{FILE_STEM}{suffix}.pdf",
            "markdown_path": f"../build/README{suffix}.md",
            "html_path": "../build/index.html" if lang == "en" else "../build/es.html",
            "typst_path": f"../rendercv_output/{stem}.typ",
        }
    return {
        "dont_generate_png": True,
        "dont_generate_html": True,
        "dont_generate_markdown": True,
        "pdf_path": f"../dist/{stem}.pdf",
        "typst_path": f"../rendercv_output/{stem}.typ",
    }


def build(master, variant, lang):
    config = master["variants"][variant]
    person = master["person"]
    titles = master["section_titles"]

    sections = {}
    for name in config["sections"]:
        if name == "summary":
            body = [text(config["summary"], lang).strip()]
        else:
            body = [entry(item, variant, lang) for item in select(master[name], variant)]
        if body:
            sections[text(titles[name], lang)] = body

    stem = FILE_STEM + config["file_suffix"] + ("_ES" if lang == "es" else "")
    document = {
        "cv": {
            "name": person["name"],
            "headline": text(config["headline"], lang),
            "location": text(person["location"], lang),
            "email": person["email"],
            "phone": person["phone"],
            "website": person["website"],
            "social_networks": person["social_networks"],
            "sections": sections,
        },
        "locale": master["locale"][lang],
        "design": master["design"],
        "settings": {"render_command": render_settings(variant, lang, stem)},
    }
    return stem, document


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--render", action="store_true", help="render every generated file with rendercv")
    args = parser.parse_args()

    master = yaml.load(MASTER)
    shutil.rmtree(GENERATED, ignore_errors=True)
    GENERATED.mkdir()

    paths = []
    for variant in master["variants"]:
        for lang in LANGUAGES:
            stem, document = build(master, variant, lang)
            path = GENERATED / f"{stem}.yaml"
            with path.open("w", encoding="utf-8") as stream:
                stream.write(f"# yaml-language-server: $schema={SCHEMA}\n")
                stream.write("# GENERATED from cv/master.yaml by scripts/build_cvs.py. Do not edit.\n")
                yaml.dump(document, stream)
            paths.append(path)
            print(f"generated {path.relative_to(ROOT)}")

    if args.render:
        rendercv = shutil.which("rendercv") or str(Path(sys.executable).parent / "rendercv")
        for path in paths:
            subprocess.run([rendercv, "render", str(path.relative_to(ROOT))], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
