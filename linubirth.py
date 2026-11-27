#!/data/data/com.termux/files/usr/bin/env python3
"""LinuBirth CLI — the pretty useless countdown to Linus Torvalds' birthday,
right in your terminal. No dependencies, Python 3 standard library only.

Usage:
    python3 linubirth.py            # live countdown (updates every second)
    python3 linubirth.py --once     # print once and exit (for scripts / pipes)
    python3 linubirth.py --no-color # disable ANSI colors
"""

import argparse
import datetime
import os
import sys
import time

TUX = r"""
      .--.
     |o_o |
     |:_/ |
    //   \ \
   (|     | )
  /'\_   _/`\
  \___)=(___/
"""

COLORS = {
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "dim": "\033[2m",
    "reset": "\033[0m",
}


def target_date():
    now = datetime.datetime.now()
    target = datetime.datetime(now.year, 12, 28)
    if target <= now:
        target = datetime.datetime(now.year + 1, 12, 28)
    return target


def color(text, name, enabled):
    if not enabled:
        return text
    return COLORS[name] + text + COLORS["reset"]


def progress_bar(now, target, width, use_color):
    prev = datetime.datetime(target.year - 1, 12, 28)
    span = (target - prev).total_seconds()
    done = (now - prev).total_seconds()
    frac = min(1.0, max(0.0, done / span)) if span else 0.0
    filled = int(round(frac * width))
    bar = "█" * filled + "░" * (width - filled)
    return color(bar, "green", use_color) + color(" %3d%%" % round(frac * 100), "dim", use_color)


def render(once, use_color):
    now = datetime.datetime.now()
    target = target_date()
    diff = int((target - now).total_seconds())

    days, rem = divmod(diff, 86400)
    hours, rem = divmod(rem, 3600)
    mins, secs = divmod(rem, 60)

    line = "  ".join(
        [
            color("%3d" % days, "green", use_color) + color("d", "dim", use_color),
            color("%2d" % hours, "yellow", use_color) + color("h", "dim", use_color),
            color("%2d" % mins, "yellow", use_color) + color("m", "dim", use_color),
            color("%2d" % secs, "red", use_color) + color("s", "dim", use_color),
        ]
    )

    if diff <= 0:
        banner = color("HAPPY BIRTHDAY LINUS!", "red", use_color)
        body = TUX
    else:
        banner = color("LinuBirth", "green", use_color) + color(
            "  —  countdown to Dec 28", "dim", use_color
        )
        body = TUX + "\n" + line + "\n" + progress_bar(now, target, 28, use_color)

    return banner + "\n" + body


def main():
    parser = argparse.ArgumentParser(description="Countdown to Linus Torvalds' birthday.")
    parser.add_argument("--once", action="store_true", help="print once and exit")
    parser.add_argument("--no-color", action="store_true", help="disable ANSI colors")
    args = parser.parse_args()

    use_color = not args.no_color and sys.stdout.isatty()

    if args.once or not sys.stdout.isatty():
        print(render(True, use_color))
        return

    try:
        while True:
            sys.stdout.write("\033[H\033[J")
            print(render(False, use_color))
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()