var gridrsr = Raphael('grid', '490', '490');

var rect_a = gridrsr.rect(5, 5, 150, 150);
//rect_a.attr({x: '10',y: '10',rx: '20',ry: '20'});

var rect_b = gridrsr.rect(170, 10, 150, 150);
//rect_b.attr({x: '170',y: '10',rx: '20',ry: '20'});

var rect_c = gridrsr.rect(330, 10, 150, 150);
//rect_c.attr({x: '330',y: '10',rx: '20',ry: '20'});

var rect_d = gridrsr.rect(10, 170, 150, 150);
//rect_d.attr({x: '10',y: '170',rx: '20',ry: '20'});

var rect_e = gridrsr.rect(170, 170, 150, 150);
//rect_e.attr({x: '170',y: '170',rx: '20',ry: '20'});

var rect_f = gridrsr.rect(330, 170, 150, 150);
//rect_f.attr({x: '330',y: '170',rx: '20',ry: '20'});

var rect_g = gridrsr.rect(5, 335, 150, 150);
//rect_g.attr({x: '10',y: '330',rx: '20',ry: '20'});

var rect_h = gridrsr.rect(170, 330, 150, 150);
//rect_h.attr({x: '170',y: '330',rx: '20',ry: '20'});

var rect_i = gridrsr.rect(330, 330, 150, 150);
//rect_i.attr({x: '330',y: '330',rx: '20',ry: '20'});


var grid = [];
grid.push(rect_a)
grid.push(rect_b)
grid.push(rect_c)
grid.push(rect_d)
grid.push(rect_e)
grid.push(rect_f)
grid.push(rect_g)
grid.push(rect_h)
grid.push(rect_i)


// Iterate through the regions & change Yorkshire's fill colour to gold
for (
	var i = 0; i < grid.length; i++) {

	grid[i].node.style.fill = "0000FF";
    // Showing off
    grid[i].mouseover(function(e){
		this.node.style.stroke = "#0000FF";
		//document.getElementById('region-name').innerHTML = this.data('region');
	});

	grid[i].mouseout(function(e){
		this.node.style.opacity = 1;
	});

	console.log("hello")
}