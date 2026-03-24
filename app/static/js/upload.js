// 功能切换逻辑
document.querySelectorAll('#tool-selector .tool-item').forEach(item => {
    item.addEventListener('click', function() {
        // 移除旧的激活态，添加新的激活态
        document.querySelector('#tool-selector .active').classList.remove('active');
        this.classList.add('active');

        // 切换参数面板显示
        const type = this.dataset.type;
        document.querySelectorAll('#param-fields > div').forEach(div => div.classList.add('d-none'));
        const activeField = document.getElementById(`field-${type}`);
        if(activeField) activeField.classList.remove('d-none');
    });
});

// 拖拽视觉反馈增强
dropZone.ondragover = (e) => {
    e.preventDefault();
    dropZone.classList.add('border-solid'); // 添加蓝色虚线高亮
};

dropZone.ondragleave = () => dropZone.classList.remove('border-solid'); // 移出时还原

dropZone.ondrop = (e) => {
    e.preventDefault();
    dropZone.classList.remove('border-solid'); // 释放时还原
    const files = e.dataTransfer.files;
    if (files.length) handleUpload(files[0]);
};