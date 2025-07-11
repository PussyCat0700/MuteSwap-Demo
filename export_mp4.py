import os
import shutil
import subprocess
from pathlib import Path

# 设置目录路径

base_dir_str = "speakers_imgs/"
base_dir = Path(base_dir_str)
source_wav_dir_str = "/data0/yfliu/voxceleb2/audio/test/mp4"
source_mp4_dir_str = "/data0/yfliu/voxceleb2/video/test/mp4"
target_mp4_dir_str = "all_converted/vox2"

files = [
"id01000/CspIoS3ZZy4/00020.mp4",
"id01066/7B-KDiAofNk/00030.mp4",
"id01298/i8N_VPTGLis/00324.mp4",
"id01041/eMRxqsB3ghc/00358.mp4",
"id01437/jrXvutBWU8k/00205.mp4",
"id01106/8NsKqf8qdIE/00049.mp4",
"id01224/9gx7Y_kleU0/00064.mp4",
"id01228/FiIjEyg3qe0/00108.mp4",
"id01460/GKUwDs0BwGQ/00091.mp4",
"id01066/7B-KDiAofNk/00030.mp4",
"id01041/eMRxqsB3ghc/00358.mp4",
"id01298/i8N_VPTGLis/00324.mp4",
"id01066/7B-KDiAofNk/00030.mp4",
"id01106/8NsKqf8qdIE/00049.mp4",
"id01224/9gx7Y_kleU0/00064.mp4",
"id01228/FiIjEyg3qe0/00108.mp4",
]

for mp4_file in files:
    source_mp3_file = (Path(source_wav_dir_str) / mp4_file).with_suffix('.wav')
    source_mp4_file = (Path(source_mp4_dir_str) / mp4_file).with_suffix('.mp4')
    target_mp4_file = Path(target_mp4_dir_str) / mp4_file
    target_tmp_file = target_mp4_file.with_name(target_mp4_file.stem + "_temp.mp4")
    os.makedirs(target_mp4_file.parent, exist_ok=True)
    print(f"🔄 Processing {target_mp4_file.name}")

    try:
        # 调用 ffmpeg 替换音轨并重新编码
        subprocess.run([
            "ffmpeg", "-y",
            "-i", str(source_mp4_file),
            "-i", str(source_mp3_file),
            "-c:v", "libx264",
            "-preset", "veryfast",
            "-crf", "23",
            "-c:a", "aac",
            "-b:a", "128k",
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-shortest",
            "-movflags", "+faststart",
            str(target_tmp_file)
        ], check=True)
        
        target_tmp_file.replace(target_mp4_file)

        print(f"✅ Exported: {target_mp4_file.name}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to process: {target_mp4_file.name}")
