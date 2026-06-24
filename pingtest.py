import subprocess

host = input("Enter IP or Domain: ")

result = subprocess.run(
    ["ping", "-c", "4", host],
    capture_output=True,
    text=True
)

print(result.stdout)
