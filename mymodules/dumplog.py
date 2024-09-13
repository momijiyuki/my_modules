import json
from datetime import datetime
from pathlib import Path


def jsonlog(fpath: str, data: dict) -> None:
    if not Path.is_file(fpath):
        with Path.open(fpath, "w") as f:
            json.dump({}, f)

    with Path.open(fpath, "r+") as f:
        jsons = json.load(f)
        jsons[f"{datetime.now(tz='JST')}"] = data
        f.seek(0)
        json.dump(jsons, f, ensure_ascii=False, indent=4)
