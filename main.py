from pathlib import Path

import mymodules
import mymodules.dumplog


def load_txt(fpath: str) -> list:
    with Path.open(fpath, encoding="utf-8") as f:
        data: str = f.read().splitlines()[0]
    return data


def disco_markdown() -> None:
    webhook = load_txt("webhook_url")

    messages = """
    # title

    - testmarkdown
        - hoge
        - foo
    """

    mymodules.discord_messages(webhook, messages)


def main() -> None:
    # disco_md() a
    data = {"score": 123, "recall": 567}
    mymodules.jsonlog("test.json", data)


if __name__ == "__main__":
    main()
