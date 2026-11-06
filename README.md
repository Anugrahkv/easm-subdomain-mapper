# External Attack Surface Mapper (EASM)

## Overview
This Python-based Threat Intelligence tool automates External Attack Surface Management (EASM) reconnaissance. It integrates with OSINT sources (HackerTarget API) to enumerate subdomains for a given target and utilizes concurrent multi-threading to probe for live web servers and cloud assets. 

This project simulates the initial infrastructure hunting phase used by enterprise security platforms to identify potential attack vectors, dangling DNS records, and exposed administrative portals.

## Features
* **OSINT Integration:** Automatically queries external APIs to discover forgotten or undocumented subdomains.
* **Concurrent Probing:** Uses Python's `concurrent.futures` ThreadPoolExecutor to rapidly scan discovered infrastructure for HTTP/HTTPS responses.
* **Triage-Ready Output:** Categorizes infrastructure based on HTTP status codes to prioritize vulnerability scanning (e.g., flagging 404s for potential Subdomain Takeovers or 401/403s for exposed login panels).

## How to Run
1. Clone this repository.
2. Install the required libraries: `pip install requests`
3. Edit the `target_domain` variable in the script to your authorized target (e.g., a bug bounty program).
4. Run the script: `python easm_mapper.py`

*Disclaimer: This tool is intended for defensive security research and authorized bug bounty hunting only. Ensure you have permission to scan the target domain.*
