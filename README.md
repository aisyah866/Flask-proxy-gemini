# Flask + Proxy (Google Gemini) - Ready to Deploy

Paket ini berisi contoh **Flask backend** yang memanggil **Google Gemini (Gen AI)** dan **Node.js proxy** yang meneruskan permintaan dari frontend (blog) ke Flask.

## Isi paket
- `flask_ai_server.py` - Flask app yang memanggil Google GenAI (Gemini).
- `proxy.js` - Node.js proxy (express + http-proxy-middleware) meneruskan `/proxy-ai` -> `/ai`.
- `blog.html` - Contoh frontend (ubah PROXY_URL).
- `requirements.txt` - Dependencies Python.
- `package.json` - Dependencies Node.js.
- `Procfile` - Contoh start command untuk deploy (Render/Heroku).

## Cara cepat menjalankan (lokal / Termux)
1. Pasang Python deps:
   ```
   pip install -r requirements.txt
   ```

2. Set API key Google Gemini:
   - Di local: `export GOOGLE_API_KEY='PASTE_YOUR_KEY_HERE'`
   - Di Render: gunakan Secrets/Environment variables `GOOGLE_API_KEY`.

3. Jalankan Flask:
   ```
   python flask_ai_server.py
   ```

4. Di terminal lain jalankan proxy:
   ```
   npm install
   node proxy.js
   ```

5. Ubah `blog.html` `PROXY_URL` ke alamat proxy Anda.
   - Jika pakai ngrok: `https://xxxxxx.ngrok.io/proxy-ai`
   - Jika deploy di Render: `https://proxy-imron.onrender.com/proxy-ai`

## Cara deploy ke Render (saran)
Untuk **online 24/7**, buat dua Web Services (satu Flask, satu Proxy) atau pisahkan repo.
1. Deploy Flask:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python flask_ai_server.py`
   - Set `GOOGLE_API_KEY` dalam Environment.
2. Deploy Proxy:
   - Build Command: `npm install`
   - Start Command: `node proxy.js`
   - Set env var `FLASK_TARGET` ke URL Flask (misal `https://flask-ai-server.onrender.com`)

## Catatan penggunaan Gemini API
- Anda butuh API key dari Google AI Studio / Google Cloud.
- Anda bisa menentukan model lewat env var `GENAI_MODEL` (default: `gemini-2.5-flash`).
- Untuk quota/billing dan penggunaan di lokasi tertentu, periksa kebijakan Google (beberapa region perlu billing).

