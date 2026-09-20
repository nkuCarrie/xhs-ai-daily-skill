---
name: xhs-ai-daily
description: Use when the user asks to monitor Xiaohongshu/Rednote AI hot posts, find AI-related posts with more than 1000 likes, generate a daily brief, deduplicate recent posts, send the brief via Feishu, or turn the workflow into a reusable monitoring skill. Must use a logged-in Chrome controlled through Kimi WebBridge for Xiaohongshu data and preserve a permanent post ledger.
version: 1.0.0
license: MIT
---

# Xiaohongshu AI Daily

Use this skill to collect, verify, deduplicate, summarize, and optionally send a Chinese daily brief of Xiaohongshu AI posts with more than 1,000 likes.

## Non-negotiable data source

- Read the local Kimi WebBridge instructions before browsing.
- Run `~/.kimi-webbridge/bin/kimi-webbridge status` first. If the daemon is not running, start it and retry.
- Continue only when both `running=true` and `extension_connected=true`.
- Use one session name for the whole run and control the user's already logged-in Chrome through `http://127.0.0.1:10086/command`.
- Do not substitute Codex's built-in browser, search-engine snippets, curl against Xiaohongshu, public HTML, or third-party aggregators.

## Required workflow

1. Read the memory file and permanent JSONL ledger before searching.
2. Open `https://www.xiaohongshu.com/search_result` in a new WebBridge tab. Confirm the login sidebar, dynamic result cards, and detail pages are readable.
3. Search these terms: `AI`, `人工智能`, `AIGC`, `AI工具`, `AI应用`, `AI副业`, `AI学习`, `AI绘画`, `AI视频`, `AI办公`.
4. Extract candidates from the live result-card DOM. Keep only cards whose generated safe link contains `/search_result/<note_id>` and `xsec_token`.
5. Enter details through that safe link. Never construct `/explore/<note_id>` for navigation. On the detail page verify title, author, original publish time when available, likes, favorites, comments, shares, and visible comment samples.
6. Normalize public links to `https://www.xiaohongshu.com/explore/<note_id>` by removing temporary query parameters.
7. Keep only posts above 1,000 likes and clearly label unconfirmed fields instead of guessing.
8. Apply a seven-day deduplication window by Note ID or normalized canonical URL. A post may reappear only as a clearly labeled tracking update when its interaction count has materially increased.
9. Prefer posts that crossed the threshold in the last 24 hours. If fewer than five qualify, add posts first seen in the last seven days; if still fewer, add recent high-quality posts as `补充观察`.
10. Do not send a report unless at least five posts were successfully verified in the logged-in Chrome session.
11. Save the report as `report-YYYY-MM-DD.md` in the configured automation directory.
12. Send with Feishu user identity only after the report is complete. Use the recipient's configured open_id and never expose tokens or secrets.
13. After successful send, append/update ledger entries through a temporary file and atomic rename. Never truncate or overwrite the historical ledger.
14. Append a short run summary to memory; never rewrite memory wholesale.
15. Close only tabs opened by this session. Never close the user's original tabs.

## Failure behavior

If the daemon, extension, logged-in session, dynamic results, safe links, or detail verification is unavailable, stop the run. Preserve a failure report and explicitly state:

`飞书发送未完成：无法访问已登录 Chrome 的小红书动态数据`

Do not send an empty report, trend-only report, or fabricated samples.

## Report format

For every item include:

- title or topic
- normalized Xiaohongshu URL
- author
- publish date or `未确认`
- likes/favorites/comments/shares when available
- status: `24小时新增`, `近7天首次收录`, `追踪更新`, or `补充观察`
- a short explanation covering topic choice, pain point, title/cover, comment sentiment, usefulness, trend borrowing, account positioning, or platform distribution logic

Finish with:

- today's AI content directions
- recurring engagement triggers
- reusable content tactics

## Configuration

Keep personal values outside the skill package. Pass them through the user's automation or environment configuration:

```text
XHS_AUTOMATION_DIR=/path/to/automation
XHS_LEDGER_PATH=/path/to/posts_ledger.jsonl
XHS_MEMORY_PATH=/path/to/memory.md
FEISHU_RECIPIENT_OPEN_ID=...
FEISHU_AS=user
```

Do not place Chrome cookies, Feishu tokens, app secrets, private recipient data, or personal ledgers in GitHub.
