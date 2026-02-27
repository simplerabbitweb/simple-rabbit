import http.server, os
os.chdir("/Users/leannfrank/Desktop/simple rabbit")
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=3456, bind="")
