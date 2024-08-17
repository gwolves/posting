from textual.binding import Binding
from textual.widgets import TabbedContent, Tabs


class PostingTabbedContent(TabbedContent):
    BINDINGS = [
        Binding("i", "next_tab", "Next tab", show=False),
        Binding("m", "previous_tab", "Previous tab", show=False),
        Binding("down,n", "app.focus_next", "Focus next", show=False),
        Binding("up,e", "app.focus_previous", "Focus previous", show=False),
    ]

    def action_next_tab(self) -> None:
        tabs = self.query_one(Tabs)
        if tabs.has_focus:
            tabs.action_next_tab()

    def action_previous_tab(self) -> None:
        tabs = self.query_one(Tabs)
        if tabs.has_focus:
            tabs.action_previous_tab()
