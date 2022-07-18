
$(document).ready(function() {
    animateDiv($('.amongus'));
    animateDiv($('.esther'));
});

function makeNewPosition($container) {
    // Get viewport dimensions (remove the dimension of the div)
    var h = window.innerHeight - 200;
    var w = window.innerWidth - 200;
    // console.log(h + " " + w);

    var nh = Math.floor(Math.random() * h);
    var nw = Math.floor(Math.random() * w);

    return [nh, nw];

}

function animateDiv($target) {
    var newq = makeNewPosition($target.parent());
    var oldq = $target.offset();
    var speed = calcSpeed([oldq.top, oldq.left], newq);
    $target.animate({
        top: newq[0],
        left: newq[1]
    }, speed, function() {
        animateDiv($target);
    });

};

function calcSpeed(prev, next) {
    // 3v3ryth1ng_sh3_d03s}
    var x = Math.abs(prev[1] - next[1]);
    var y = Math.abs(prev[0] - next[0]);

    var greatest = x > y ? x : y;

    var speedModifier = 0.5;

    var speed = Math.ceil(greatest / speedModifier);

    return speed;

}

window.addEventListener('scroll', () => {
    const {
        scrollTop,
        scrollHeight,
        clientHeight
    } = document.documentElement;
    if(Math.random() < 0.5) $("#container").append('<button class="secretButton"><a href="https://www.youtube.com/watch?v=iik25wqIuFo&ab_channel=Rickroll%2Cbutwithadifferentlink" class="secret">Click here to see my biggest secret</a></button>');
}, {
    passive: true
});

