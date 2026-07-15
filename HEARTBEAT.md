# Execution Follow-up Guard

On each heartbeat:

1. Inspect the current active direct session for user requests from the last 15 minutes.
2. Identify requests that received only an acknowledgement, a progress claim, or a clarification request—but no corresponding completed tool action, verified result, or explicit blocker.
3. If any exists:
   - Resume the outstanding action immediately if it is safe and does not need confirmation.
   - If confirmation is required, send one concise message naming the exact confirmation needed.
   - If blocked, send the exact blocker and the next action needed.
4. Never claim progress without a tool result or other observable evidence.
5. If no action needs follow-up, reply HEARTBEAT_OK.
