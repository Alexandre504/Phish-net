const http = require('http');
const https = require('https');

const proxyServer = http.createServer((req, res) => {
    const options = {
        hostname: req.headers.host.split(":")[0], //This handles the change in hostname
        path: req.url,
        method: req.method,
        headers: req.headers,
    };

  let proxyRequest;
  if (options.hostname.includes('virustotal.com')) {
    proxyRequest = https.request(options, (proxyRes) => {
      proxyRes.pipe(res);
    });
  } else {
    proxyRequest = http.request(options, (proxyRes) => {
      proxyRes.pipe(res);
    });
  }


  proxyRequest.on('error', (error) => {
    console.error('Error:', error);
    res.writeHead(500, { 'Content-Type': 'text/plain' });
    res.end('Proxy error');
  });

  req.pipe(proxyRequest);
});

const port = 3000; // Choose a port
proxyServer.listen(port, () => {
  console.log(`Proxy server listening on port ${port}`);
});
