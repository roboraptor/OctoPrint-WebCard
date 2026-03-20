import octoprint.plugin

class WebCardPlugin(octoprint.plugin.StartupPlugin,
                    octoprint.plugin.TemplatePlugin,
                    octoprint.plugin.SettingsPlugin,
                    octoprint.plugin.AssetPlugin):

    def on_after_startup(self):
        url = self._settings.get(["webpage_url"])
        self._logger.info("WebCardPlugin started. Displaying page: %s" % url)

    def get_settings_defaults(self):
        return dict(
            show_title=True,           # if True, the title will be displayed
            title_text="Printables", # title text
            show_icon=True,           # if True, a FontAwesome icon will be displayed instead of text
            icon_class="fa-globe",     # FontAwesome icon class
            webpage_url="http://www.printables.com"  # URL of the page to be displayed
        )

    def get_template_configs(self):
        return [
            # Configuration of the new tab in the UI
            dict(type="tab",
                 custom_bindings=False,
                 template="webcard_tab.jinja2",
                 tab_slug="webcard",
                 title="Web Page"),
            # Plugin settings configuration
            dict(type="settings",
                 custom_bindings=False,
                 template="webcard_settings.jinja2",
                 tablename="Web Page")
        ]

    def get_template_vars(self):
        return dict(
            plugin_webcard_show_title=self._settings.get(["show_title"]),
            plugin_webcard_title_text=self._settings.get(["title_text"]),
            plugin_webcard_show_icon=self._settings.get(["show_icon"]),
            plugin_webcard_icon_class=self._settings.get(["icon_class"])
        )

    def get_assets(self):
        return dict(
            js=["js/webcard.js"]
        )

__plugin_name__ = "Web Card Plugin"
__plugin_version__ = "1.0.0"
__plugin_description__ = "A plugin that adds a tab with a configurable web page to the OctoPrint UI. In the settings, you can choose whether to display a title or a FontAwesome icon, and set the URL."
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = WebCardPlugin()
