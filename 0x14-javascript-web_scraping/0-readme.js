#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 3) {
    console.error('Usage: node 0-readme.js <filepath>');
    process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
	// Print the error object as a JSON string
	console.error(JSON.stringify(err, Object.getOwnPropertyNames(err)));
    } else {
	console.log(data);
    }
});
