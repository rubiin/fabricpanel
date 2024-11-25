from fabric.hyprland.widgets import WorkspaceButton, Workspaces as HyperlandWorkspace
from fabric.widgets.box import Box


# This class represents a widget that displays workspace buttons
class WorkSpaces(Box):
    def __init__(self, occupied=True, count=8, **kwargs):
        super().__init__(name="workspaces-box", style_classes="bar-box", **kwargs)
        # Create a HyperlandWorkspace widget to manage workspace buttons
        self.workspace = HyperlandWorkspace(
            name="workspaces",
            spacing=4,
            # Create buttons for each workspace if not occupied
            buttons=[WorkspaceButton(id=i, label=str(i)) for i in range(1, count + 1)]
            if not occupied
            else None,
            # Factory function to create buttons for each workspace
            buttons_factory=lambda ws_id: WorkspaceButton(id=ws_id, label=str(ws_id)),
        )
        # Add the HyperlandWorkspace widget as a child
        self.children = self.workspace
