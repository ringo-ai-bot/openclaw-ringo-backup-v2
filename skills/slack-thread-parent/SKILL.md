---
name: slack-thread-parent
description: Fetch only the Slack thread parent/original message for channel or DM thread replies. Use when the envelope has threadId/thread_ts/TransportThreadId, the root post is missing, or someone refers to the original thread message.
---

# Slack thread parent

Recover **only the parent Slack message** for a thread reply. Never dump the rest of the channel or the rest of the DM.

This is mandatory for:

- Channel threads (`slack:channel:…:thread:…`)
- DM threads, including when OpenClaw folds the reply into the peer DM session (`slack:direct:<user>`) instead of a `:thread:` session

A message you sent because someone else asked you to (for example Ashil asked you to DM Diana) lives in the **sender’s** session, not the recipient’s. The only safe copy of that original text is the Slack parent message.

## When

Do this on the first turn when **any** of these are true:

- Inbound envelope has `threadId`, `thread_ts`, or `TransportThreadId`
- The prompt does not already contain the root post you (or anyone) started the thread with
- The user talks about “the original message”, “this thread”, “those tickets”, or similar
- The current session history is an older unrelated DM/channel topic

## How

Use the current thread id as `messageId`. `target` is the conversation from the envelope (channel id `C…`, DM id `D…`, or `user:U…`):

```json
{
  "action": "read",
  "channel": "slack",
  "target": "D0AH2PFQ199",
  "messageId": "1786689653.263599"
}
```

`messageId` **must** equal the thread id. Do this before answering.

## Do not

- `read` with `threadId` and no `messageId` — the plugin drops the parent (`ts === threadId`)
- `read` with `before` / `around` / a large `limit` to scrape the channel or DM
- `sessions_history` on the peer DM or channel session to recover the send
- Copy or search the requester’s private session (the person who asked you to send the DM)
- Enable or assume `thread.inheritParent` (that copies the full channel transcript)
- Answer from the last top-level DM topic when a `threadId` is present

## Then

Answer from that parent body plus the current reply (and later replies already in this thread). If the parent read fails, say so and ask for the missing detail instead of guessing from other tickets or older DM history.
