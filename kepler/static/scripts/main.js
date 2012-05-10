$(document).ready(function () {
    // planet tabs
    $(".planets" ).tabs();

    function drawCanvas() {
        $('.planet').each(function () {
            var planet = $(this);
            // canvas
            var canvas = planet.find('canvas.planetCanvas').get(0),
                size_in_sky = $(this).data('size'), // radius of sky
                color = $(this).data('color'),
                radius = size_in_sky/90*(canvas.width*1.5);
                size_of_sol = 0.53/90*(canvas.width*1.5);

            canvas.getContext("2d").clearRect(0,0,canvas.width,canvas.height);
            drawSky(canvas, {
                startRadius: radius,
                endRadius: radius*15
            });
            drawStar(canvas, {radius: radius, color: color});
            drawOutline(canvas, {radius: size_of_sol});

        });
    }

    // resize the canvas
    $(window).resize(function () {
        var planets = $('.planet');
        planets.find('canvas.planetCanvas').width(planets.filter(':visible:first').width())
        //planets.find('canvas.planetCanvas').height($(window).height()-planets.filter(':visible:first').offset().top)
        drawCanvas();
    }).resize();

    // initialise planet
    $('.planet').each(function () {
        var planet = $(this);

        // Age
        var period = $(this).data('period'),
            period_tangle = new Tangle(planet.get(0), {
            initialize: function () { 
                            this.age_on_earth = 15; 
                        },
            update:     function () {
                            this.age_on_planet = this.age_on_earth * (365.256363 / period); 
                        }
        });

        // Gravity
        var gravity = $(this).data('gravity'),
            gravity_tangle = new Tangle(planet.get(0), {
            initialize: function () { 
                            this.weight_on_earth = 50; 
                        },
            update:     function () {
                            this.vertical_jump = 35 * (9.81/gravity);
                            this.weight_on_planet = Math.round((this.weight_on_earth / 9.81) * gravity);
                            // A cow weighs 360kg, a chicken weighs 1.5 kg
                            this.weight_in_cows = (this.weight_on_planet / 360);
                            this.extra_weight_in_chickens = (this.weight_on_planet % 360) / 1.5
                            this.weight_in_babies = this.weight_on_planet / 3.3
                            if(this.weight_in_cows > 1){
                                this.equiv_weight = Math.floor(this.weight_in_cows) + " cow"
                                if(this.weight_in_cows > 2){
                                    this.equiv_weight = this.equiv_weight + "s"
                                }
                                if(Math.floor(this.extra_weight_in_chickens) > 0){
                                    this.equiv_weight = this.equiv_weight + " and " +
                                        Math.floor(this.extra_weight_in_chickens) + " chickens"
                                }

                            } else {
                                this.equiv_weight = Math.round(this.weight_in_babies) + " newborn babies"
                            }
                         }
        });


    });
});


// Draw the sky with radial gradient from the center of the canvas
// Options: 
//  startX, startY, startRadius, endX, endY, endRadius
function drawSky(canvas, options) {
    var context = canvas.getContext("2d");

    var centerX = canvas.width / 2;
    var centerY = canvas.height / 2;

    // 
    options = options || {};
    if (options.startX == null) { options.startX = centerX; }
    if (options.startY == null) { options.startY = centerY; }
    if (options.startRadius == null) { options.startRadius = 0; }
    if (options.startColor == null) { options.startColor = "#8ED6FF"; }  // light blue
    if (options.endX == null) { options.endX = centerX; }
    if (options.endY == null) { options.endY = centerY; }
    if (options.endRadius == null) { options.endRadius = Math.max(canvas.width, canvas.height);; }
    if (options.endColor == null) { options.endColor = "#004CB3"; }  // dark blue

    // Rectangle for gradient
    context.beginPath();
    context.rect(0, 0, canvas.width, canvas.height);

    // Gradient
    var outerRadius =  Math.min(canvas.width, canvas.height);
    var grd = context.createRadialGradient(
            options.startX, options.startY, options.startRadius, 
            options.endX, options.endY, options.endRadius);
    grd.addColorStop(0, options.startColor);
    grd.addColorStop(1, options.endColor); 
    context.fillStyle = grd;
    context.fill();
}
// Draw a circle with the given radius and color.
// drawStar(canvas, {x: 200, y: 100, radius: 70, color:'#FFFFFF'});
function drawStar(canvas, options) {
    var context = canvas.getContext("2d");

    var centerX = canvas.width / 2;
    var centerY = canvas.height / 2;

    options = options || {};
    if (options.x==null) {
        options.x = centerX;
    }

    if (options.y == null) {
        options.y = centerY;
    }

    // circle
    context.beginPath();
    var arc  = context.arc(options.x, options.y, options.radius, 0, 2 * Math.PI, false);
    context.fillStyle = options.color
    context.fill();
    context.lineWidth = 1;
    context.strokeStyle = options.color
    context.stroke();

    return arc;
}

// Draw a circle with the given radius (outline only).
// drawOutline(canvas, {radius: 70, color:'#FFFFFF'});
function drawOutline(canvas, options) {
    var context = canvas.getContext("2d");

    var centerX = canvas.width / 2;
    var centerY = canvas.height / 2;

    if (options.x==null) {
        options.x = centerX;
    }

    if (options.y == null) {
        options.y = centerY;
    }

    // circle
    context.beginPath();
    var arc  = context.arc(options.x, options.y, options.radius, 0, 2 * Math.PI, false);
    context.fillStyle = "None";
    context.lineWidth = 1;
    context.strokeStyle = "#000000"
    context.stroke();

    return arc;
}
