import requests
import random
import os

# Configuración (se leerá de GitHub Secrets)
BLOG_ID = os.getenv("BLOG_ID")  # Ej: "1234567890123456789"
API_KEY = os.getenv("API_KEY")   # Clave API Google
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # Ej: "@tucanal"

# 1. Obtener posts de Blogger
response = requests.get(
    f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts?key={API_KEY}&maxResults=50"
)
posts = response.json().get('items', [])

if posts:
    # 2. Seleccionar post aleatorio
    post = random.choice(posts)
    mensaje = f"📢 **{post['title']}**\n\n{post['url']}\n\n#Blog #ContenidoDiario"
    
    # 3. Publicar en Telegram
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": mensaje,
            "parse_mode": "Markdown"
        }
    )
    print("✅ Post publicado en Telegram")
else:
    print("❌ No hay posts disponibles")
