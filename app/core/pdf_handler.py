import fitz  # PyMuPDF
from pathlib import Path
from .base_handler import BaseHandler

class PdfToImageHandler(BaseHandler):
    """将 PDF 页面转换为高质量图片。"""

    def process(self, input_path: Path, output_dir: Path) -> Path:
        output_path = output_dir / f"{input_path.stem}.png"
        try:
            doc = fitz.open(str(input_path))
            page = doc.load_page(0)  # 处理第一页
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2倍缩放保证清晰度
            pix.save(str(output_path))
            doc.close()
            return output_path
        except Exception as e:
            raise RuntimeError(f"PDF 转换失败: {e}")