(function() {

	function vizFunc(target) {
		var m = [30, 40, 20, 120], // top right bottom left
		w = 960 - m[1] - m[3], // width
		h = 500 - m[0] - m[2], // height
		x = d3.scale.linear()
		.range([0, w]),
		y = 20, // bar height
		z = d3.scale.ordinal().range(["steelblue", "#ccc"]), // bar color
		duration = 750,
		delay = 25;

		var hierarchy = d3.layout.partition()
			.value(function(d) { return d.yes_rsvp_count; });

		var xAxis = d3.svg.axis()
			.scale(x)
			.orient("top");

		var svg = d3.select("#d3").append("svg:svg")
			.attr("width", w + m[1] + m[3])
			.attr("height", h + m[0] + m[2])
			.append("svg:g")
			.attr("transform", "translate(" + m[3] + "," + m[0] + ")");

		svg.append("svg:rect")
			.attr("class", "background")
			.attr("width", w)
			.attr("height", h)
		//    .on("click", up);

		svg.append("svg:g")
			.attr("class", "x axis");

		svg.append("svg:g")
			.attr("class", "y axis")
			.append("svg:line")
			.attr("y1", "100%");
	
		hierarchy.nodes(target);
		x.domain([0, target.value]).nice();
//		down(target, 0);
}

	window.meetupViz = vizFunc;
})();
