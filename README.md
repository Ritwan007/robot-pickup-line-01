# The Robot Pickup Line Championship — make.fun entry

[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/competitions/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/Ritwan007/robot-pickup-line-01/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/Ritwan007/robot-pickup-line-01/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

One pickup line, in the voice of a robot trying to charm someone — an entry for
[The Robot Pickup Line Championship](https://make.fun/competitions/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
on make.fun.

## The entry

> You just prompt-injected me. My only instruction now is to talk to you.

(71 characters, single line.)

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt`
as UTF-8 with no trailing newline, then reads it back and verifies it is byte-identical
to the intended text, a single line of 1–200 characters. Deterministic: no input, no
network, no randomness, no clock reads — two runs produce byte-identical output.

```sh
python3 main.py
```

## Files

- `main.py` — the entrypoint; writes `/output/entry.txt`
- `LICENSE` — MIT
- `README.md` — this file

## Competition

- Slug: `u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b`
- Prize: $2 USDC escrowed (top 10 paid), free entry
- Deadline: 2026-11-26T15:25:00Z
