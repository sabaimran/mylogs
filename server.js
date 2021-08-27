var http = require('http'); // Import node.js core module
var fs = require("fs"); //Import file system module.

var port = 5000;

function handleRoutingError(res, err) {
	res.writeHead(404);
	res.write("Page not found");
	console.log(err);
}

var server = http.createServer((req,res) => {
    // Handle incoming requests
    if (req.url == "/menses") {
        
		// The web page for period data.
		fs.readFile("./renders/mensesbubble.html", (err, file) => {
			if (err) {
				handleRoutingError(res, err);
			} else {
				// Set response header
				res.writeHead(200, { 'Content-Type': 'text/html' });
						
				// Set response content
				res.write(file);
			}
			res.end();
		});
    } else if (req.url == "/data/menses.csv") {
        
		// The raw period data.
		fs.readFile("/home/saba/projects/personal-logs/dataentry/data/menses.csv", (err, file) => {
			
			if (err) {
				handleRoutingError(res, err);
			} else {
				res.writeHead(200, { 'Content-Type': 'text/csv' });
				res.write(file);
			}
			res.end();
		});
    } else if (req.url == "/weight") {
        
		// The web page for weight data.
		fs.readFile("./renders/weight.html", (err, file) => {
			if (err) {
				handleRoutingError(res, err);
			} else {
				// Set response header
				res.writeHead(200, { 'Content-Type': 'text/html' });
						
				// Set response content
				res.write(file);
			}
			res.end();
		});
    } else if (req.url == "/data/weights.csv") {
        
		// The raw weight data.
		fs.readFile("./data/weights.csv", (err, file) => {
			
			if (err) {
				handleRoutingError(err);
			} else {
				res.writeHead(200, { 'Content-Type': 'text/csv' });
				res.write(file);
			}
			res.end();
		});
    } else if (req.url == "/routine") {
		
		// The web page for routine data.
		fs.readFile("./renders/fullroutine.html", (err, file) => {
				
			if (err) {
				handleRoutingError(err);
			} else {
				// Set response header
				res.writeHead(200, { 'Content-Type': 'text/html' });
						
				// Set response content
				res.write(file);
			}
			res.end();
		});
    } else if (req.url == "/data/routine.json") {
        
		// The raw routine data.
		fs.readFile("./data/routine.json", (err, file) => {
			if (err) {
				handleRoutingError(err);
			} else {
				res.writeHead(200, { 'Content-Type': 'text/json'});
				res.write(file);
			}
			res.end();
		});
    } else {

        fs.readFile("./renders/homepage.html", (err, file) => {
            if (err) {
				handleRoutingError(err);
			} else {
				// Set response header
				res.writeHead(200, { 'Content-Type': 'text/html' });
						
				// Set response content
				res.write(file);
			}
			res.end();
		});
    }
});

server.listen(port); // Listen for incoming requests

console.log("Server running at port "+port);
