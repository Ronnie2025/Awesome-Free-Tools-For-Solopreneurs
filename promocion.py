import os
import sys
import webbrowser
import urllib.parse

# Marketing Automation Script for RG Digital
# Helps WenzoWich promote their new portal and repository to drive traffic and Web3 donations!

PORTAL_URL = "https://rg-digital-f115.netlify.app"
GUIDE_URL = "https://rg-digital-f115.netlify.app/guia.html"
REPO_URL = "https://github.com/WenzoWich/Awesome-Free-Tools-For-Solopreneurs"

REDDIT_SUBREDDITS = [
    "sidehustle",
    "solopreneur",
    "freelance",
    "digitalnomad"
]

TWEET_TEXT = f"""🚀 Acabo de lanzar un portal de recursos gratuitos para solopreneurs y creadores.

Incluye una Guía Definitiva de Monetización interactiva (sin rodeos, de 0 a $1,000/mes) y un repositorio Open Source con 30+ herramientas gratis.

¡Todo en producción y listo para usar!

👉 Repositorio GitHub: {REPO_URL}
👉 Guía Web: {GUIDE_URL}

Aprecia cualquier ⭐ en el repositorio si te sirve. ¡Éxito! ⚡"""

REDDIT_TITLE = "Recopilación de herramientas gratuitas y guía de monetización para Solopreneurs (0 a $1000/mes)"
REDDIT_BODY = f"""Hola a todos,

He estado recopilando las mejores herramientas y recursos gratuitos que cualquier solopreneur, freelancer o creador puede usar para lanzar y automatizar su negocio sin gastar un solo dólar.

He estructurado todo en un repositorio público y he diseñado una guía interactiva con estrategias reales:

📦 **Repositorio con 30+ herramientas:**
{REPO_URL}

⚡ **Guía de Monetización Interactiva:**
{GUIDE_URL}

**¿Qué incluye la guía?**
1. Estrategias de freelancing que funcionan hoy (templates de propuestas incluidos).
2. Lanzamiento rápido de productos digitales en 48 horas.
3. Canales de afiliación y CPA (sin necesidad de vender directamente).
4. Un plan de acción diario de 4 semanas.

Espero que les sirva de ayuda para lanzar sus proyectos. ¡Se agradece cualquier feedback o estrella ⭐ en el repositorio!"""

def print_banner():
    print("=" * 70)
    print("⚡ RG DIGITAL - AUTOMATIZACIÓN DE PROMOCIÓN Y MARKETING ⚡")
    print("=" * 70)
    print(f"Portal: {PORTAL_URL}")
    print(f"Guía:   {GUIDE_URL}")
    print(f"Repo:   {REPO_URL}")
    print("-" * 70)

def main():
    print_banner()
    print("Selecciona una opción para abrir las plataformas con el contenido listo:")
    print("1. Promocionar en Twitter / X (Abrirá el navegador con el tuit pre-cargado)")
    print("2. Promocionar en Reddit (Te dará las opciones para publicar en subreddits clave)")
    print("3. Abrir Portal y Guía en vivo en tu navegador")
    print("4. Salir")
    print("-" * 70)
    
    choice = input("Elige una opción (1-4): ").strip()
    
    if choice == '1':
        print("\n[+] Abriendo Twitter/X...")
        encoded_tweet = urllib.parse.quote(TWEET_TEXT)
        webbrowser.open(f"https://twitter.com/intent/tweet?text={encoded_tweet}")
        print("[!] Tuit pre-cargado en tu navegador. ¡Solo dale a Publicar!")
        
    elif choice == '2':
        print("\n[+] Selecciona un Subreddit:")
        for idx, sub in enumerate(REDDIT_SUBREDDITS, 1):
            print(f"{idx}. r/{sub}")
        print("5. Todos los anteriores")
        
        sub_choice = input("Elige (1-5): ").strip()
        
        print("\n" + "="*50)
        print("📋 COPIA ESTE TEXTO PARA TU POST:")
        print("="*50)
        print(f"TÍTULO:\n{REDDIT_TITLE}\n")
        print(f"CONTENIDO:\n{REDDIT_BODY}")
        print("="*50 + "\n")
        
        input("Presiona ENTER para abrir las pestañas de Reddit en tu navegador...")
        
        if sub_choice in ['1', '2', '3', '4']:
            sub = REDDIT_SUBREDDITS[int(sub_choice) - 1]
            webbrowser.open(f"https://www.reddit.com/r/{sub}/submit?title={urllib.parse.quote(REDDIT_TITLE)}&text={urllib.parse.quote(REDDIT_BODY)}")
        elif sub_choice == '5':
            for sub in REDDIT_SUBREDDITS:
                webbrowser.open(f"https://www.reddit.com/r/{sub}/submit?title={urllib.parse.quote(REDDIT_TITLE)}&text={urllib.parse.quote(REDDIT_BODY)}")
        print("[!] Pestañas de Reddit abiertas. ¡Pega el contenido y publica!")
        
    elif choice == '3':
        print("\n[+] Abriendo Portal y Guía en tu navegador...")
        webbrowser.open(PORTAL_URL)
        webbrowser.open(GUIDE_URL)
        webbrowser.open(REPO_URL)
        
    else:
        print("\nSaliendo... ¡Mucho éxito con la promoción de tu plataforma! 🚀")

if __name__ == "__main__":
    main()
