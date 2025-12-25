from flask import Flask, request, jsonify
from flask_cors import CORS # 必须导入这个
import os

app = Flask(__name__)
CORS(app) # 必须启用这个，否则网页连不上 Python

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"status": "error", "message": "没有收到图片"}), 400
    
    file = request.files['image']
    
    # 自动创建 uploads 文件夹
    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    # 保存图片
    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)
    
    print(f"成功保存图片到: {file_path}")
    
    # 返回给前端的消息
    return jsonify({
        "status": "success", 
        "message": f"图片 {file.filename} 已同步到后端",
        "result": "CNV (后端预诊断)", 
        "confidence": "99.2%"
    })

if __name__ == '__main__':
    # 确保在 5000 端口运行
    app.run(port=5000, debug=True)