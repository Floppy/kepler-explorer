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

