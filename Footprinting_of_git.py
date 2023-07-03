import requests

def dork_check(domain):
    dork = "site:{} intext:”index of /.git” (“parent directory”) {}".format(domain, domain)
    response = requests.get(dork)
    if response.status_code == 200:
        return f"[+] Potential Git directory found for: {domain}"
    else:
        return f"[-] No Git directory found for: {domain}"

def perform_dork_check(domains):
    print("== Git Directory Dork Checker ==")
    print("Checking for potential Git directories...\n")
    
    results = []
    for domain in domains:
        result = dork_check(domain.strip())  # Remove leading/trailing whitespace
        results.append(result)
    
    print("\nDork checking completed.")
    return results

if __name__ == "__main__":
    # Read domains from the file
    with open("domains.txt", "r") as file:
        domains = file.readlines()
    
    output = perform_dork_check(domains)
    
    # Save output to file
    with open("output.txt", "w") as file:
        for line in output:
            file.write(line + "\n")
    
    print("Output saved to 'output.txt' file.")
