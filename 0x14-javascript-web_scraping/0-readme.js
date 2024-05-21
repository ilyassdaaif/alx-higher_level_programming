#!/usr/bin/node
// Importing the file system module from Node.js
const fs = require('fs');

// Getting the file path from the command line arguments
const filePath = process.argv[2];

// Reading the file content
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
	// If an error occurs, print the error object
	console.error(err);
    } else {
	// If no error, print the file content
	console.log(data);
    }
});
