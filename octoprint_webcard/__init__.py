import octoprint.plugin

class WebCardPlugin(octoprint.plugin.StartupPlugin,
                    octoprint.plugin.TemplatePlugin,
                    octoprint.plugin.SettingsPlugin,
                    octoprint.plugin.AssetPlugin):

    def on_after_startup(self):
        url = self._settings.get(["webpage_url"])
        self._logger.info("WebCardPlugin spuštěn. Zobrazuje stránku: %s" % url)

    def get_settings_defaults(self):
        return dict(
            show_title=True,           # pokud True, zobrazí se titulek
            title_text="Moje Web Karta", # text titulku
            show_icon=False,           # pokud True, zobrazí se FontAwesome ikona místo textu
            icon_class="fa-globe",     # třída FontAwesome ikony
            webpage_url="https://example.com"  # URL stránky, která se má zobrazit
        )

    def get_template_configs(self):
        return [
            # Konfigurace nové karty (tab) v UI
            dict(type="tab",
                 custom_bindings=False,
                 template="webcard_tab.jinja2",
                 tab_slug="webcard",
                 title="Web Karta"),
            # Konfigurace nastavení pluginu
            dict(type="settings",
                 custom_bindings=False,
                 template="webcard_settings.jinja2",
                 tablename="Web Karta")
        ]

    def get_assets(self):
        return dict(
            js=["js/webcard.js"]
        )

__plugin_name__ = "Web Card Plugin"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Plugin, který přidává kartu s nastavitelnou webovou stránkou do UI OctoPrint. V nastavení lze vybrat, zda se zobrazí titulek či FontAwesome ikona, a nastavit URL."
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = WebCardPlugin()
