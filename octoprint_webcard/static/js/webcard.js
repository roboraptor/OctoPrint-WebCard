$(function() {
    function WebCardViewModel(parameters) {
        var self = this;
        // Vstupní parametr settingsViewModel je injektován OctoPrintem
        self.settings = parameters[0];
        // Observable pro aktuální URL, načtenou z nastavení pluginu
        self.currentUrl = ko.observable(self.settings.settings.plugins.webcard.webpage_url());

        // Sleduj změny URL v nastavení a aktualizuj observable
        self.settings.settings.plugins.webcard.webpage_url.subscribe(function(newVal) {
            self.currentUrl(newVal);
        });
    }

    OCTOPRINT_VIEWMODELS.push([
        WebCardViewModel,
        ["settingsViewModel"],
        ["#tab_plugin_webcard"]
    ]);
});
