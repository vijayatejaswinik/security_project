# analyzer.py — log analyzer

failed_attempts = {}  # dictionary

with open("logs/sample.log", "r") as f:
    for line in f:
        if "FAILED" in line:
            ip = line.split()[-1]  # last word is the IP
            if ip not in failed_attempts:
                failed_attempts[ip] = 0
            failed_attempts[ip] += 1

# Find suspicious IPs (more than 2 failures)
suspicious = [ip for ip, count in failed_attempts.items() if count > 2]

# Save report
with open("report.txt", "w") as r:
    r.write("Failed Attempts:\n")
    r.write(str(failed_attempts) + "\n\n")
    r.write("Suspicious IPs:\n")
    r.write(str(suspicious))

print("Report generated: report.txt")
