me3 = function() {
    me3 = {};

    me3.down = function down(d, i) {
	if (!d.children || this.__transition__) return;
	var end = duration + d.children.length * delay;

	// Mark any currently-displayed bars as exiting.
	var exit = svg.selectAll(".enter").attr("class", "exit");

	// Entering nodes immediately obscure the clicked-on bar, so hide it.
	exit.selectAll("rect").filter(function(p) { return p === d; })
	    .style("fill-opacity", 1e-6);

	// Enter the new bars for the clicked-on data.
	// Per above, entering bars are immediately visible.
	var enter = this.bar(d)
	    .attr("transform", this.stack(i))
	    .style("opacity", 1);

	// Have the text fade-in, even though the bars are visible.
	// Color the bars as parents; they will fade to children if appropriate.
	enter.select("text").style("fill-opacity", 1e-6);
	enter.select("rect").style("fill", z(true));

	// Update the x-scale domain.
	x.domain([d3.min(d.children, function(d) {return d.d3_value; }), d3.max(d.children, function(d) { return d.d3_value; })]).nice();

	// Update the x-axis.
	svg.selectAll(".x.axis").transition().duration(duration).call(xAxis);

	// Transition entering bars to their new position.
	var enterTransition = enter.transition()
	    .duration(duration)
	    .delay(function(d, i) { return i * delay; })
	    .attr("transform", function(d, i) { return "translate(0," + y * i * 1.2 + ")"; });

	// Transition entering text.
	enterTransition.select("text").style("fill-opacity", 1);

	// Transition entering rects to the new x-scale.
	enterTransition.select("rect")
	    .attr("width", function(d) { return x(d.d3_value); })
	    .style("fill", function(d) { return z(!!d.children); });

	// Transition exiting bars to fade out.
	var exitTransition = exit.transition()
	    .duration(duration)
	    .style("opacity", 1e-6)
	    .remove();

	// Transition exiting bars to the new x-scale.
	exitTransition.selectAll("rect").attr("width", function(d) { return x(d.d3_value); });

	// Rebind the current node to the background.
	svg.select(".background").data([d]).transition().duration(end); d.index = i;
    }

    me3.up = function up(d) {
	if (!d.parent || this.__transition__) return;
	var end = duration + d.children.length * delay;

	// Mark any currently-displayed bars as exiting.
	var exit = svg.selectAll(".enter").attr("class", "exit");

	// Enter the new bars for the clicked-on data's parent.
	var enter = bar(d.parent)
	    .attr("transform", function(d, i) { return "translate(0," + y * i * 1.2 + ")"; })
	    .style("opacity", 1e-6);

	// Color the bars as appropriate.
	// Exiting nodes will obscure the parent bar, so hide it.
	enter.select("rect")
	    .style("fill", function(d) { return z(!!d.children); })
	    .filter(function(p) { return p === d; })
	    .style("fill-opacity", 1e-6);

	// Update the x-scale domain.
	x.domain([0, d3.max(d.parent.children, function(d) { return d.d3_value; })]).nice();

	// Update the x-axis.
	svg.selectAll(".x.axis").transition().duration(duration).call(xAxis);

	// Transition entering bars to fade in over the full duration.
	var enterTransition = enter.transition()
	    .duration(end)
	    .style("opacity", 1);

	// Transition entering rects to the new x-scale.
	// When the entering parent rect is done, make it visible!
	enterTransition.select("rect")
	    .attr("width", function(d) { return x(d.d3_value); })
	    .each("end", function(p) { if (p === d) d3.select(this).style("fill-opacity", null); });

	// Transition exiting bars to the parent's position.
	var exitTransition = exit.selectAll("g").transition()
	    .duration(duration)
	    .delay(function(d, i) { return i * delay; })
	    .attr("transform", this.stack(d.index));

	// Transition exiting text to fade out.
	exitTransition.select("text")
	    .style("fill-opacity", 1e-6);

	// Transition exiting rects to the new scale and fade to parent color.
	exitTransition.select("rect")
	    .attr("width", function(d) { return x(d.d3_value); })
	    .style("fill", z(true));

	// Remove exiting nodes when the last child has finished transitioning.
	exit.transition().duration(end).remove();

	// Rebind the current parent to the background.
	svg.select(".background").data([d.parent]).transition().duration(end);;
    }

    // Creates a set of bars for the given data node, at the specified index.
    me3.bar = function bar(d) {
	var bar = svg.insert("svg:g", ".y.axis")
	    .attr("class", "enter")
	    .attr("transform", "translate(0,5)")
	    .selectAll("g")
	    .data(d.children)
	    .enter().append("svg:g")
	    .style("cursor", function(d) { return !d.d3_value ? null : "pointer"; })
	    .on("click", this.down);

	bar.append("svg:text")
	    .attr("x", -6)
	    .attr("y", y / 2)
	    .attr("dy", ".35em")
	    .attr("text-anchor", "end")
	    .text(function(d) { return d.d3_name; });

	bar.append("svg:rect")
	    .attr("width", function(d) { return x(d.d3_value); })
	    .attr("height", y);

	return bar;
    }

    // A stateful closure for stacking bars horizontally.
    me3.stack = function stack(i) {
	var x0 = 0;
	return function(d) {
	    var tx = "translate(" + x0 + "," + y * i * 1.2 + ")";
	    x0 += x(d.d3_value);
	    return tx;
	};
    }
    return me3;
}();
