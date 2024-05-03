import os
import csv
import requests


def download_m3u(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)


def add_https_to_m3u(m3u_file):
    modified_lines = []
    with open(m3u_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("//"):
                modified_lines.append("https:" + line)
            else:
                modified_lines.append(line)
    with open(m3u_file, "w") as file:
        file.writelines(modified_lines)


# Path to the CSV file containing the URLs
csv_file = "urls.txt"

output_m3u_dir = "m3u_files"
os.makedirs(output_m3u_dir, exist_ok=True)

# Open the CSV file and read its contents
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if it exists
    for row in reader:
        name, url = row
        url = url.replace("https://linkads.xyz/www.phimmoivl.net/ads2video/embed.html?link=https://www.phimmoivl.net/jwplayer?source=",
                          "").replace("%2F", "/").replace("%3A", ":")
        filename = f"{name}.m3u"
        fpath = os.path.join(output_m3u_dir, filename)
        print(f"Downloading {filename} from {url}")
        download_m3u(url, fpath)
        add_https_to_m3u(fpath)

print("Download complete.")
