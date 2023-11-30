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


def fetch_download_details(url, **kwargs) -> Dict[str, Union[List[str], Any]]:
    yt = PyTubeYoutube(url, use_oauth=False, allow_oauth_cache=True)
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
                "resolution": s.resolution,
            }
            for s in stream
        ],
    }

    return data
