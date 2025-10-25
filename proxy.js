const express = require("express");
const { createProxyMiddleware } = require("http-proxy-middleware");
const app = express();

// Target will be replaced to the Flask service URL during deploy (use env var)
const TARGET = process.env.FLASK_TARGET || "http://127.0.0.1:5000";

app.use("/proxy-ai", createProxyMiddleware({
  target: TARGET,
  changeOrigin: true,
  pathRewrite: { "^/proxy-ai": "/ai" }
}));

const PORT = process.env.PORT || 10000;
app.listen(PORT, () => console.log("Proxy berjalan di port", PORT, " -> target:", TARGET));
