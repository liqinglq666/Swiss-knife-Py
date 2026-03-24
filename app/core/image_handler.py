from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from .base_handler import BaseHandler

class WatermarkHandler(BaseHandler):
    """图像水印处理模块。"""

    def process(self, input_path: Path, output_dir: Path) -> Path:
        output_path = output_dir / f"watermarked_{input_path.name}"
        try:
            with Image.open(input_path) as img:
                draw = ImageDraw.Draw(img)
                # 简单水印示例
                draw.text((10, 10), "OpenSource-Swiss-Knife", fill=(255, 255, 255))
                img.save(output_path)
            return output_path
        except Exception as e:
            raise RuntimeError(f"Failed to add watermark: {e}")