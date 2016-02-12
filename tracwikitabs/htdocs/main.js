($.documentReady || $.ready)(function($) {
    var containers = $('.tracwikitabs');
    containers.each(function(tabs_idx) {
        var container = $(this);
        var list = $('<ul></ul>');
        container.children('div.wikipage').each(function(tab_idx) {
            var id = this.id;
            if (!id) {
                this.id = id = 'tracwikitabs-' + tabs_idx + '-' + tab_idx;
            }
            var title = this.title || 'No title';
            this.removeAttribute('title');
            var anchor = $('<a></a>').attr('href', '#' + id).text(title);
            list.append($('<li></li>').append(anchor));
        });
        container.prepend(list);
        container.tabs();
    });
});
