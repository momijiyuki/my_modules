import json
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import requests


# https://qiita.com/ABBBB/items/e6bdf7fc94b8f6f72a01
def discord_messages(
    webhook_url: str,
    text: str,
    img_path: str | None = None,
    img_name: str = "",
) -> requests.Response:
    data = {"content": text}

    if img_name != "" and img_path:
        print("imgs")
        with Path.open(Path(img_path) / img_name, "rb") as f:
            img_bin = f.read()
        files = {"favicon": (img_name, img_bin)}
    else:
        files = None

    return requests.post(webhook_url, data, files=files, timeout=200)


def main() -> None:
    webhook_url = "https://discord.com/api/webhooks/xxxxxxxx"
    content = "test messages"
    for i in range(3):
        x = np.arange(-3, 5, 0.1)
        y = np.cos(x) * np.sin(i)
        plt.plot(x, y)
        plt.title("sin curve")
        plt.savefig("test.png")
        time.sleep(5)
        res = discord_messages(webhook_url, content + str(i), "./", "test.png")

    print(res.status_code)
    print(json.dumps(json.loads(res.content), indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
