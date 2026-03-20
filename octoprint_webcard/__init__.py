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
            title_text="Web Page", # title text
            show_icon=False,           # if True, a FontAwesome icon will be displayed instead of text
            icon_class="fa-globe",     # FontAwesome icon class
            webpage_url="https://example.com"  # URL of the page to be displayed
        )

    def get_template_configs(self):
        return [
            # Configuration of the new tab in the UI
            dict(type="tab",
                 custom_bindings=True,
                 template="webcard_tab.jinja2",
                 tab_slug="webcard",
                 title="Web Page"),
            # Plugin settings configuration
            dict(type="settings",
                 custom_bindings=False,
                 template="webcard_settings.jinja2",
                 tablename="Web Page")
        ]

    def get_assets(self):
        return dict(
            js=["js/webcard.js"]
        )

__plugin_name__ = "Web Card Plugin"
__plugin_version__ = "1.0.0"
__plugin_description__ = "A plugin that adds a tab with a configurable web page to the OctoPrint UI. In the settings, you can choose whether to display a title or a FontAwesome icon, and set the URL."
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = WebCardPlugin()
