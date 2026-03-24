import pandas as pd
import tabula
from pathlib import Path
from .base_handler import BaseHandler


class TableConvertHandler(BaseHandler):
    """PDF/CSV 转 Excel 处理器。"""

    def process(self, input_path: Path, output_dir: Path, **kwargs) -> Path:
        output_path = output_dir / f"{input_path.stem}_converted.xlsx"
        suffix = input_path.suffix.lower()

        try:
            if suffix == ".pdf":
                # stream=True 适合结构化紧凑的表格
                tables = tabula.read_pdf(str(input_path), pages='all', multiple_tables=True)
                with pd.ExcelWriter(output_path) as writer:
                    for i, df in enumerate(tables):
                        df.to_excel(writer, sheet_name=f'Table_{i + 1}', index=False)

            elif suffix == ".csv":
                df = pd.read_csv(input_path)
                df.to_excel(output_path, index=False)

            return output_path
        except Exception as e:
            raise RuntimeError(f"表格转换失败: {str(e)}")