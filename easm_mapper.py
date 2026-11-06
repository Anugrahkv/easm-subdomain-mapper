import requests
import concurrent.futures

def get_subdomains(domain):
    print(f"[*] Querying HackerTarget API for: {domain}")
    
    # Using HackerTarget as a reliable alternative to crt.sh
    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    
    try:
        response = requests.get(url, timeout=15)
        
        if response.status_code != 200:
            print(f"[-] API returned status code: {response.status_code}")
            return []
            
        subdomains = set()
        # HackerTarget returns plain text in the format: subdomain,IP
        lines = response.text.strip().split('\n')
        
        for line in lines:
            if ',' in line:
                subdomain = line.split(',')[0].strip()
                subdomains.add(subdomain)
                
        return list(subdomains)
    except Exception as e:
        print(f"[-] Error querying HackerTarget: {e}")
        return []

def check_alive(subdomain):
    url = f"http://{subdomain}"
    try:
        response = requests.get(url, timeout=5)
        return f"[+] ALIVE: {url} (Status: {response.status_code})"
    except requests.exceptions.RequestException:
        # We don't print dead subdomains to keep the output clean
        return f"[-] DEAD : {url}"

if __name__ == "__main__":
    # Target domain
    target_domain = "bugcrowd.com" 
    
    subdomains = get_subdomains(target_domain)
    
    if len(subdomains) > 0:
        print(f"[+] Found {len(subdomains)} unique subdomains.")
        print("[*] Probing for live cloud assets and web servers (Testing top 50)...\n")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # We limit to 50 so it runs fast for this test
            results = executor.map(check_alive, subdomains[:50]) 
            
            for result in results:
                if "[+] ALIVE" in result:
                    print(result)
    else:
        print("[-] No subdomains found.")