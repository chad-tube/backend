from typing import Dict, List, Any, Union

from pytube import YouTube


def fetch_download_details(url, **kwargs) -> Dict[str, Union[List[str], Any]]:
    yt = YouTube(url)
    stream = yt.streams.filter(**kwargs)
    data = {
        "title": yt.title,
        "streams": [
            {
                "itag": s.itag,
                "mime_type": s.mime_type,
                "abr": s.abr,
                "file_size": s.filesize,
                "url": s.url,
            }
            for s in stream
        ],
    }

    return data
