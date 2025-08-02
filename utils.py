# modules/utils.py
import yt_dlp

async def yt_stream_link(query, video=False):
    try:
        ydl_opts = {
            "format": "bestaudio[ext=m4a]/bestaudio/best",
            "quiet": True,
            "noplaylist": True,
            "default_search": "ytsearch",
            "skip_download": True,
        }

        if video:
            ydl_opts["format"] = "best[height<=720]"

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            if "entries" in info:
                info = info["entries"][0]
            return info["url"]

    except Exception as e:
        print(f"[ERROR] yt_stream_link: {e}")
        return None