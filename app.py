from pathlib import Path
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
from app.core.image_handler import WatermarkHandler
from app.core.video_handler import VideoToGifHandler

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

# 配置工程化路径
BASE_DIR = Path(__file__).parent
UPLOAD_FOLDER = BASE_DIR / "uploads"
DOWNLOAD_FOLDER = BASE_DIR / "downloads"

# 确保目录存在
UPLOAD_FOLDER.mkdir(exist_ok=True)
DOWNLOAD_FOLDER.mkdir(exist_ok=True)

# 简单的模块映射：后缀名 -> 处理类
HANDLERS = {
    ".png": WatermarkHandler(),
    ".jpg": WatermarkHandler(),
    ".jpeg": WatermarkHandler(),
    ".mp4": VideoToGifHandler(),
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    # 获取文件和功能类型
    file = request.files.get("file")
    tool_type = request.form.get("tool_type", "extract_img")
    custom_params = request.form.to_dict()  # 接收前端传来的所有参数

    if not file: return jsonify({"error": "No file"}), 400

    filename = secure_filename(file.filename)
    input_path = UPLOAD_FOLDER / filename
    file.save(input_path)

    # 这里的逻辑从“看后缀”改为“看用户选了什么功能”
    handler = HANDLERS.get(tool_type)

    try:
        # 将 custom_params 传给 handler
        output_path = handler.process(input_path, DOWNLOAD_FOLDER, **custom_params)
        return jsonify({"message": "Success", "filename": output_path.name})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/download/<filename>")
def download_file(filename: str):
    target_path = DOWNLOAD_FOLDER / filename
    if target_path.exists():
        return send_file(target_path, as_attachment=True)
    return "File not found", 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)