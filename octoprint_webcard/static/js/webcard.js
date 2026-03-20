$(function() {
    function WebCardViewModel(parameters) {
        var self = this;
        // The settingsViewModel input parameter is injected by OctoPrint
        self.settings = parameters[0];

        console.log("--- WebCard --- WebCardViewModel created");
        console.log("--- WebCard --- Initial URL:", self.settings.settings.plugins.webcard.webpage_url());

        // Observable for the current URL, loaded from the plugin settings
        self.currentUrl = ko.observable(self.settings.settings.plugins.webcard.webpage_url());

        // Watch for changes to the URL in the settings and update the observable
        self.settings.settings.plugins.webcard.webpage_url.subscribe(function(newVal) {
            console.log("--- WebCard --- URL changed to:", newVal);
            self.currentUrl(newVal);
        });
    }

    OCTOPRINT_VIEWMODELS.push([
        WebCardViewModel,
        ["settingsViewModel"],
        ["#tab_plugin_webcard"]
    ]);
});
