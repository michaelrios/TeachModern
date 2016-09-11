/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');

function flipAnimation ($obj) {
    var flipClass = 'flip';
    var $child = $obj.find('.codewords-word');
    $obj.toggleClass(flipClass);
    $child.toggleClass('counter-flip');
    $obj.one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend',
    function () {
        $obj.toggleClass(flipClass);
        $child.toggleClass('counter-flip');
    });
}

function changeTeam($obj, fromClass, toClass) {
    if (fromClass) {
        $obj.removeClass(fromClass);
    }

    flipAnimation($obj);

    if (toClass) {
        $obj.addClass(toClass);
    }
}

var handleTransition = function ($obj) {
    var neutralTeamClass = 'neutral-team',
        redTeamClass = 'red-team',
        blueTeamClass = 'blue-team';

    if ($obj.hasClass(redTeamClass)) {
        changeTeam($obj, redTeamClass, blueTeamClass);
    } else if ($obj.hasClass(blueTeamClass)) {
        changeTeam($obj, blueTeamClass, neutralTeamClass);
    } else if ($obj.hasClass(neutralTeamClass)) {
        changeTeam($obj, neutralTeamClass, false);
    } else {
        changeTeam($obj, false, redTeamClass);
    }
};

function initCodeWords() {
    var cardClass = 'codewords-card',
        wordClass = 'codewords-word';

    var $card = $('.' + cardClass);

    var cardClickEvent = function (obj) {
        var $obj = $(obj.target);

        if ($obj.hasClass(wordClass)) {
            $obj = $obj.parent();
        }

        handleTransition($obj);
        handleTransition($obj.siblings(0));
    };

    $card.click(cardClickEvent);
}
