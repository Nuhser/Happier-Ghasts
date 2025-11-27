import shutil

NAMESPACES: list[str] = ["custom_crafter", "happier_ghasts"]
LANG_PATH: str = "resource_pack/assets/{namespace}/lang"
LANGS: dict[str, list[str]] = {
    "de_de": ["de_at", "de_ch"],
    "en_us": ["en_au", "en_ca", "en_gb", "en_nz"]
}

if (__name__ == "__main__"):
    for namespace in NAMESPACES:
        print(f"Copying messages for namespace '{namespace}'...")

        for src_lang, langs in LANGS.items():
            for lang in langs:
                shutil.copy(
                    f"{LANG_PATH.format(namespace=namespace)}/{src_lang}.json",
                    f"{LANG_PATH.format(namespace=namespace)}/{lang}.json"
                )
                print(f"Copied {src_lang} to {lang}")

        print()