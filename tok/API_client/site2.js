const http = require('http');

const message = 'green';
const options = {
  hostname: '192.168.148.87', // Replace with your Arduino IP
  port: 81,
  path: '/',
  method: 'POST',
  headers: {
    'Content-Type': 'text/plain',
    'Content-Length': Buffer.byteLength(message),
  }
};

const req = http.request(options, res => {
  console.log(`Status: ${res.statusCode}`);
  res.setEncoding('utf8');
  res.on('data', chunk => console.log('Body:', chunk));
});

req.on('error', e => {
  console.error(`Problem: ${e.message}`);
});

req.write(message);
req.end();