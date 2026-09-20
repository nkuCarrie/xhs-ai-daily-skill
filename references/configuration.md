# Configuration template

Use a private local config or automation memory. Do not commit personal values.

```toml
[paths]
automation_dir = "/private/path/to/automation"
ledger = "/private/path/to/posts_ledger.jsonl"
memory = "/private/path/to/memory.md"

[feishu]
recipient_open_id = "replace-locally"
as_identity = "user"

[search]
keywords = ["AI", "人工智能", "AIGC", "AI工具", "AI应用", "AI副业", "AI学习", "AI绘画", "AI视频", "AI办公"]
like_threshold = 1000
dedup_days = 7
```
