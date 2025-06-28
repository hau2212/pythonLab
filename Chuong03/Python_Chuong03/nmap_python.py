import nmap

scanner = nmap.PortScanner()

target = "scanme.nmap.org"

scanner.scan(ports=target, arguments="-A")

print(scanner.scaninfo())