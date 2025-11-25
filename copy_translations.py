import shutil

LANG_PATH: str = "resource_pack/assets/happier_ghasts/lang"

LANGS: dict[str, list[str]] = {
    "de_de": ["de_at", "de_ch"],
    "en_us": ["en_au", "en_ca", "en_gb", "en_nz"]
}

for src_lang, langs in LANGS.items():
    for lang in langs:
        shutil.copy(f"{LANG_PATH}/{src_lang}.json", f"{LANG_PATH}/{lang}.json")
        print(f"Copied {src_lang} to {lang}")