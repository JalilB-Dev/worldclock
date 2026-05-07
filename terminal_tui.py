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

    def display_time(self, city, timezone):
        current_time = datetime.now(ZoneInfo(timezone))
        time_text = Text(f"{current_time}", "Time belongs to you, choose yours",
                         style="#00ff41", justify="center")
        time_panel = Panel(f"{self.display_time(self.cities[0]['name'], self.cities[0]['timezone'])}", style="#00ff41",
                           border_style="#d474ff")
        self.Console.print(time_panel)
        return f"{city}: {current_time.strftime('%A, %B %d %I:%M %p %Z')}"
