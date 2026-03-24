from abc import ABC, abstractmethod
from pathlib import Path


class BaseHandler(ABC):
    """文件处理抽象基类，所有新功能必须实现此接口。"""

    @abstractmethod
    def process(self, input_path: Path, output_dir: Path) -> Path:
        """
        处理逻辑。
        :param input_path: 输入文件路径
        :param output_dir: 结果存放目录
        :return: 生成的结果文件路径
        """
        pass