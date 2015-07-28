<script>

// Tooltips
var tip = d3.tip()
    .attr('class', 'd3-tip')
    .offset([-10, 0])
    .html(function(d) {
        return "<strong>Example: </strong><span style='color:tomato'>" + d.example + "</span><br><strong>Lemmas: </strong><span style='color:yellow'>" + d.lemmanames + "</span><br><strong>LexName: </strong><span style='color:orange'>" + d.lexname + "</span><br><strong>Part of Speech: </strong><span style='color:cornflowerBlue'>" + d.pos + "</span><br><strong>Similar Words:</strong><span style='color:blue'> " + d.similartos + "</span>";
})


// D3

var width = 200,
    height = 200,
    padding = 1, // separation between same-color circles
    clusterPadding = 2, // separation between different-color circles
    maxRadius = 12;

var n = {{ n }}; // number of distinct clusters (classes)
var m = {{ m }}; // total objects
 
// Colors to match nipy logo
var colors = ["#000000","#FFFFCE","#AAA89","#669900","#CCCCCC"]

// The largest node for each cluster.
var clusters = new Array(m);

var nodes = [
    {% for project in projects %}
        {% for name, tag, class in project["project"] %}
            {% if project["count"] != "{{ n }}" %}
                {"cluster": {{ project["count"] }}, radius: "10", color: colors[{{ project["count"]}} ]},
            {% else %}
                {"cluster": {{ project["count"] }}, radius: "10", color: colors[{{ project["count"]}}}
            {% endif %}
        {% endfor %}
    {% endfor %}
    ];

var nodes = d3.range(m).map(function(ii) {
  var i = nodes[ii].cluster,
      r = Math.sqrt((i + 1) / m * -Math.log(Math.random())) * maxRadius,
      d = {cluster: i, radius: 40, color:nodes[ii].color};
  if (!clusters[i] || (r > clusters[i].radius)) clusters[i] = d;
  return d;
});

var force = d3.layout.force()
    .nodes(nodes)
    .size([width, height])
    .gravity(0)
    .charge(0)
    .on("tick", tick)
    .start();

var svg = d3.select("#brain").append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("background-image",'url("static/img/nipy.svg")')

// Call tooltips function
//svg.call(tip);

var rect = svg.selectAll("rect")
    .data(nodes)
  .enter().append("rect")
    .attr("width", function(d) { return d.radius; })
    .attr("height", function(d) { return d.radius; })
    .style("fill", function(d,i) { return d.color; })
    .call(force.drag);

function tick(e) {
  rect
      .each(cluster(10 * e.alpha * e.alpha))
      .each(collide(.5))
      .attr("x", function(d) { return d.x; })
      .attr("y", function(d) { return d.y; });
}

// Move d to be adjacent to the cluster node.
function cluster(alpha) {
  return function(d) {
    var cluster = clusters[d.cluster],
        k = 1;

    // For cluster nodes, apply custom gravity.
    if (cluster === d) {
      cluster = {x: width / 2, y: height / 2, radius: -d.radius};
      k = .1 * Math.sqrt(d.radius);
    }

    var x = d.x - cluster.x,
        y = d.y - cluster.y,
        l = Math.sqrt(x * x + y * y),
        r = d.radius + cluster.radius;
    if (l != r) {
      l = (l - r) / l * alpha * k;
      d.x -= x *= l;
      d.y -= y *= l;
      cluster.x += x;
      cluster.y += y;
    }
  };
}

// Resolves collisions between d and all other circles.
function collide(alpha) {
  var quadtree = d3.geom.quadtree(nodes);
  return function(d) {
    var r = d.radius + maxRadius + Math.max(padding, clusterPadding),
        nx1 = d.x - r,
        nx2 = d.x + r,
        ny1 = d.y - r,
        ny2 = d.y + r;
    quadtree.visit(function(quad, x1, y1, x2, y2) {
      if (quad.point && (quad.point !== d)) {
        var x = d.x - quad.point.x,
            y = d.y - quad.point.y,
            l = Math.sqrt(x * x + y * y),
            r = d.radius + quad.point.radius + (d.cluster === quad.point.cluster ? padding : clusterPadding);
        if (l < r) {
          l = (l - r) / l * alpha;
          d.x -= x *= l;
          d.y -= y *= l;
          quad.point.x += x;
          quad.point.y += y;
        }
      }
      return x1 > nx2 || x2 < nx1 || y1 > ny2 || y2 < ny1;
    });
  };
}    
</script>    

