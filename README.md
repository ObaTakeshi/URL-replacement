# URL replacement

URL のパスをそのままにホストを置換したりできる Alfred Workflow

## url_list ファイル

`~/Documents/URL_replacement/url_list.json`

上のパスに以下の内容の json ファイルを配置。

動作として、それぞれの置換候補を探索し、置換候補内に現在の URL がヒットした場合、その置換候補のブロックを Alfred に返す。

```
{
    "data": [
        // 置換候補1
        [
            {
                "name": ページ名,
                "url": ページのURL
            },
            {
                "name": ページ名,
                "url": ページのURL
            }
        ],

        // 置換候補2
        [
            {
                "name": ページ名,
                "url": ページのURL
            },
            {
                "name": ページ名,
                "url": ページのURL
            }
        ]
    ]
}
```
