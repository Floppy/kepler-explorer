$(document).ready(function () {
    console.log('ready');
    $('.planet').each(function () {
        var planet = $(this);
        // canvas
        var canvas = planet.find('canvas.planetCanvas').get(0),
            size_in_sky = $(this).data('size'), // radius of sky
            color = $(this).data('color'),
            radius = size_in_sky/90*canvas.width;
        drawSky(canvas);
        drawStar(canvas, {radius: radius, color: color});

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
                            this.weight_on_planet = (this.weight_on_earth / 9.81) * gravity; 
                        }
        });


    });
});


// Draw the sky with radial gradient from the center of the canvas
function drawSky(canvas) {
    var context = canvas.getContext("2d");

    var centerX = canvas.width / 2;
    var centerY = canvas.height / 2;

    // Rectangle for gradient
    context.beginPath();
    context.rect(0, 0, canvas.width, canvas.height);

    // Gradient
    var outerRadius =  Math.min(canvas.width, canvas.height);
    var grd = context.createRadialGradient(centerX, centerY, 0, centerX, centerY, outerRadius);
    grd.addColorStop(0, "#8ED6FF"); // light blue
    grd.addColorStop(1, "#004CB3"); // dark blue
    context.fillStyle = grd;
    context.fill();
}
// Draw a circle with the given radius and color.
// drawStar(canvas, {x: 200, y: 100, radius: 70, color:'#FFFFFF'});
function drawStar(canvas, options) {
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
    context.fillStyle = options.color
    context.fill();
    context.lineWidth = 1;
    context.strokeStyle = options.color
    context.stroke();

    return arc;
}
