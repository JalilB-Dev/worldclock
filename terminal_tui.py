import pyfiglet
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

from datetime import datetime
from zoneinfo import ZoneInfo


class TerminalTUI:
    def __init__(self):
        self.Console = Console()

    def display_header(self):
        ascii_header = pyfiglet.figlet_format(
            "TPOCH", font="slant"
        )
        header_text = Text(
            ascii_header, style="#00ff41", justify="center", no_wrap=True
        )
        header_panel = Panel(
            header_text, style="#d474ff", border_style="#d474ff", title="//Terminal World Clock", subtitle="//The Only Clock You Need"
        )
        self.Console.print(header_panel
                           )

    def display_time(self, cities):
        time_text = Text(justify="left", style="#00ff41")
        for city in cities:
            current_time = datetime.now(ZoneInfo(city["timezone"]))
            line = f"{city['name']}: {current_time.strftime('%A, %B %d %I:%M %p %Z')}\n"
            time_text.append(line)
        time_panel = Panel(time_text, border_style="#d474ff")
        self.Console.print(time_panel)
