# (c) @UniBorg
# Original written by @UniBorg edit by @INF1N17Y
"""Syntax .param"""
from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.param", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("PARAM"))
	for _ in range(31):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
