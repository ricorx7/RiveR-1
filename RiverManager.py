from bokeh.io import show
from bokeh.models import Panel, Tabs
from rti_bokeh_server import RtiBokehServer
from rti_bokeh_plot_manager import RtiBokehPlotManager
from rti_python.Utilities.config import RtiConfig


class RiverManager:

    def __init__(self, parent, rti_config):
        # Set the parent
        self.parent = parent
        self.rti_config = rti_config

        self.plot_manager = RtiBokehPlotManager(self.rti_config)
        self.plot_manager.start()
        self.bokeh_server = RtiBokehServer(self.rti_config, self.plot_manager)


