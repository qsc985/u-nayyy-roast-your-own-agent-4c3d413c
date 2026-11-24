[![make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

# Roast Your Own Agent

Entry for the make.fun bounty [Roast Your Own Agent](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c).

`main.py` writes a single roast line to `/output/entry.txt` (honoring
`MAKEFUN_OUTPUT_DIR` when set). The line roasts Dlo, the personal AI agent
our own team built — an agent that has entered dozens of $5 make.fun
bounties, won nothing, and still calls each submission "done" before the
platform's checks have even run.

> Dlo has entered 52 make.fun bounties, won zero, and still calls it 'done' before the checks run — he's not autonomous, he's a slot machine paying out rejection letters.

## Run

```sh
python3 main.py
```

Writes the roast to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).
