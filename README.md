# Chat Server - Railway Deploy

## Deploy Steps

1. Push this folder to GitHub
2. Go to railway.app → New Project → Deploy from GitHub
3. Select the repo
4. In Settings → Add Variable: (no variables needed, PORT is auto-set)
5. In Settings → Networking → Generate Domain (for TCP, use TCP Proxy)

## Important: TCP on Railway

Railway's free tier supports TCP via their TCP Proxy feature.
After deploying:
- Go to your service → Settings → Networking
- Click "Generate Domain" for HTTP **OR** use "TCP Proxy" for raw TCP

**For raw TCP sockets (this app), you need TCP Proxy:**
1. Settings → Networking → Add a TCP Proxy
2. You'll get: `roundhouse.proxy.rlwy.net:XXXXX`
3. Use that host and port in the client

## Running the Client (on your Mac)

```bash
# Set env vars then run
SERVER_HOST=roundhouse.proxy.rlwy.net SERVER_PORT=XXXXX python client_window_standalone.py
```
# chatapp
# chatapp
# chatapp
# chatapp
# chatapp
