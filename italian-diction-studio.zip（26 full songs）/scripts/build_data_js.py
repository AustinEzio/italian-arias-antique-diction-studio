#!/usr/bin/env python3
"""将 data/*.json 打包为 web/data.js，并将 audio/*.wav 复制到 web/audio/。
web/ 目录由此脚本生成、自包含，可直接部署到 GitHub Pages。
用法：python3 scripts/build_data_js.py
"""
import json
import glob
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
AUDIO_DIR = os.path.join(ROOT, "audio")
WEB_DIR = os.path.join(ROOT, "web")
OUT_JS = os.path.join(WEB_DIR, "data.js")
OUT_AUDIO = os.path.join(WEB_DIR, "audio")


def main():
    songs = []
    for f in glob.glob(os.path.join(DATA_DIR, "*.json")):
        with open(f, encoding="utf-8") as fh:
            songs.append(json.load(fh))
    songs.sort(key=lambda s: s.get("number", 0))
    payload = json.dumps(songs, ensure_ascii=False, indent=2)
    with open(OUT_JS, "w", encoding="utf-8") as fh:
        fh.write("// 由 scripts/build_data_js.py 自动生成，请勿手改。\n")
        fh.write("window.SONGS = " + payload + ";\n")
    print(f"已打包 {len(songs)} 首 -> {OUT_JS}")

    os.makedirs(OUT_AUDIO, exist_ok=True)
    copied = 0
    for wav in sorted(glob.glob(os.path.join(AUDIO_DIR, "*.wav"))):
        shutil.copy2(wav, os.path.join(OUT_AUDIO, os.path.basename(wav)))
        copied += 1
    print(f"已复制 {copied} 个音频 -> {OUT_AUDIO}")


if __name__ == "__main__":
    main()
