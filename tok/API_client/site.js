const express = require('express');
const http = require('http');
const app = express();
const port = 82;

app.use(express.text());

app.post('/send-to-arduino', (req, res) => {
  const message = req.body;

  const options = {
    hostname: '192.168.148.190', // Arduino IP
    port: 81,
    path: '/',
    method: 'POST',
    headers: {
      'Content-Type': 'text/plain',
      'Content-Length': Buffer.byteLength(message)
    }
  };

  const arduinoReq = http.request(options, arduinoRes => {
    let responseData = '';
    arduinoRes.on('data', chunk => responseData += chunk);
    arduinoRes.on('end', () => res.send(responseData));
  });

  arduinoReq.on('error', e => res.status(500).send(e.message));
  arduinoReq.write(message);
  arduinoReq.end();
});

app.listen(port, () => {
  console.log(`Proxy server running at http://localhost:${port}`);
});
