var http = require('http'); // Import node.js core module
var fs = require("fs"); //Import file system module.
var port = 5000;

var server = http.createServer((req,res) => {
    // Handle incoming requests
    if (req.url == "/menses") {
        
	fs.readFile("./renders/mensesbubble.html", (err, file) => {
            if (err) {
		res.writeHead(404);
		res.write("Page not found");
		console.log(err);
	    } else {
		// Set response header
		res.writeHead(200, { 'Content-Type': 'text/html' });
                
		// Set response content
		res.write(file);
	    }
	    res.end();
	});
    } else if (req.url == "/data/menses.csv") {
        
	fs.readFile("./lifedata/menses.csv", (err, file) => {
	    
	    if (err) {
		res.writeHead(404);
		res.write("Menses not found");
		console.log(err);
	    } else {
		res.writeHead(200, { 'Content-Type': 'text/csv' });
		res.write(file);
	    }
	    res.end();
	});
    } else if (req.url == "/weight") {
        
	fs.readFile("./renders/weight.html", (err, file) => {
            if (err) {
		res.writeHead(404);
		res.write("Page not found");
		console.log(err);
	    } else {
		// Set response header
		res.writeHead(200, { 'Content-Type': 'text/html' });
                
		// Set response content
		res.write(file);
	    }
	    res.end();
	});
    } else if (req.url == "/data/weights.csv") {
        
	fs.readFile("./lifedata/weights.csv", (err, file) => {
	    
	    if (err) {
		res.writeHead(404);
		res.write("Weights not found");
		console.log(err);
	    } else {
		res.writeHead(200, { 'Content-Type': 'text/csv' });
		res.write(file);
	    }
	    res.end();
	});
    }else if (req.url == "/routine") {
        
	fs.readFile("./renders/fullroutine.html", (err, file) => {
            
	    if (err) {
		res.writeHead(404);
		res.write("Page not found");
		console.log(err);
	    } else {
		// Set response header
		res.writeHead(200, { 'Content-Type': 'text/html' });
                
		// Set response content
		res.write(file);
	    }
	    res.end();
	});
    } else if (req.url == "/data/routine.json") {
        
	fs.readFile("./lifedata/routine.json", (err, file) => {
	    if (err) {
		res.writeHead(404);
		res.write("Routine not found");
		console.log(err);
	    } else {
		res.writeHead(200, { 'Content-Type': 'text/json'});
		res.write(file);
	    }
	    res.end();
	});
    } else {
        fs.readFile("./renders/homepage.html", (err, file) => {
            if (err) {
		res.writeHead(404);
		res.write("Page not found");
		console.log(err);
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
