#!/usr/bin/env python3
import http.server, cgi, os, shutil

class UploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type']})
        fileitem = form['file']
        filename = os.path.basename(fileitem.filename)
        save_path = os.path.join('images', filename)
        os.makedirs('images', exist_ok=True)
        with open(save_path, 'wb') as f:
            shutil.copyfileobj(fileitem.file, f)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f'<script>alert("Uploaded: {filename}"); window.location="dishes.html";</script>'.encode())

    def log_message(self, *args):
        pass

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Server running at http://localhost:8080")
print("Upload page: http://localhost:8080/upload.html")
http.server.HTTPServer(('0.0.0.0', 8080), UploadHandler).serve_forever()
