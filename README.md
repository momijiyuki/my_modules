# mymodules

個人的に欲しいと思った機能をモジュールとして追加していく

## 使用しているライブラリ

- matplotlib
- numpy
- requests
- 他標準ライブラリ

## 使い方

```py {.line-numbers}
from mymodules import discord_alert

webhook = "{任意のwebhook url}"
messages = ""

discord_alert.discord_messages(webhook, messages)
```


```py {.line-numbers}
from mymodules import timecounter

@timecounter
def any_function():
    return

@timecounter(dump=True)
def response_function():
    return

returns = any_function()
returns, time = response_function()
```


```py {.line-numbers}
from mymodules import jsonlog

data = {
    "score": 123,
    "recall": 567
}

jsonlog("test.json", data)
```
