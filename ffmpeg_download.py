import os
import subprocess
from concurrent.futures import ThreadPoolExecutor


def download_m3u(url, output_file, log_file):
    # Command to download M3U file using ffmpeg
    command = [
        "ffmpeg",
        "-protocol_whitelist", "file,http,https,tcp,tls,crypto",
        "-i", url,
        "-c", "copy",
        output_file
    ]

    # Open subprocess and log output to a file
    with open(log_file, "a") as log:
        subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)


if __name__ == "__main__":
    m3u_dir = "m3u_files"
    output_video_dir = "videos"
    log_dir = "logs"

    os.makedirs(output_video_dir, exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)

    m3u_files = os.listdir(m3u_dir)

    # Function to download each M3U file
    def download_m3u_wrapper(m3u_file):
        m3u_path = os.path.join(m3u_dir, m3u_file)
        output_file = os.path.join(output_video_dir, f"{m3u_file}.mp4")
        log_file = os.path.join(log_dir, f"{m3u_file}.log")

        print(f"Downloading video from {m3u_file}")
        download_m3u(m3u_path, output_file, log_file)

    # Use a thread pool to download M3U files concurrently
    with ThreadPoolExecutor(4) as executor:
        executor.map(download_m3u_wrapper, m3u_files)

    print("Download complete.")
