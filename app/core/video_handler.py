from pathlib import Path
from moviepy.editor import VideoFileClip
from .base_handler import BaseHandler

class VideoToGifHandler(BaseHandler):
    """视频转 GIF 处理模块。"""

    def process(self, input_path: Path, output_dir: Path) -> Path:
        output_path = output_dir / f"{input_path.stem}.gif"
        try:
            # 限制时长和尺寸以防内存溢出
            with VideoFileClip(str(input_path)) as clip:
                # 截取前 5 秒并缩小尺寸
                sub_clip = clip.subclip(0, min(5, clip.duration)).resize(width=480)
                sub_clip.write_gif(str(output_path), fps=10, logger=None)
            return output_path
        except Exception as e:
            raise RuntimeError(f"Video processing failed: {str(e)}")