# xhs-ai-daily

Reusable Agent Skill for monitoring Xiaohongshu AI posts over 1,000 likes, producing a Chinese daily brief, deduplicating recent posts, and optionally sending it to Feishu.

## What it includes

- Kimi WebBridge-only Xiaohongshu collection rules
- safe-link detail verification rules
- 7-day Note ID deduplication
- report and ledger persistence rules
- Feishu user-identity delivery guidance
- failure behavior that prevents fabricated or empty reports

## What it deliberately excludes

Personal Chrome state, cookies, Feishu tokens, app secrets, recipient open IDs, private ledgers, and automation schedules.

## Install

Copy the `xhs-ai-daily-skill` directory into the skills directory used by your agent, or package it using the target registry's normal skill publisher.
