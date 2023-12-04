from typing import Dict, List, Any, Union

from pytube import YouTube
from pytube import exceptions
from pytube.innertube import InnerTube


class PyTubeYoutube(YouTube):
    def bypass_age_gate(self):
        """Attempt to update the vid_info by bypassing the age gate."""
        innertube = InnerTube(
            client="ANDROID",
            use_oauth=self.use_oauth,
            allow_cache=self.allow_oauth_cache,
        )
        innertube_response = innertube.player(self.video_id)

        playability_status = innertube_response["playabilityStatus"].get("status", None)

        # If we still can't access the video, raise an exception
        # (tier 3 age restriction)
        if playability_status == "UNPLAYABLE":
            raise exceptions.AgeRestrictedError(self.video_id)

        self._vid_info = innertube_response


def convert_size(size_in_bytes):
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB"]
    unit_index = 0
    size = float(size_in_bytes)
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    return f"{size:.2f} {units[unit_index]}"


def fetch_download_details(
    url, type_=None, **kwargs
) -> Dict[str, Union[List[str], Any]]:
    yt = PyTubeYoutube(url, use_oauth=False, allow_oauth_cache=True)
    if type_ == "video":
        stream = yt.streams.filter(progressive=True)
    elif type_ == "audio":
        stream = yt.streams.filter(only_audio=True)
    else:
        stream = yt.streams.filter()
    data = {
        "title": yt.title,
        "thumbnail_url": yt.thumbnail_url,
        "streams": [
            {
                "itag": s.itag,
                "mime_type": s.mime_type,
                "abr": s.abr,
                "file_size": convert_size(s.filesize),
                "url": s.url,
                "resolution": s.resolution,
            }
            for s in stream
        ],
    }

    return data
