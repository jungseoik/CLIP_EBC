import gradio as gr
from custom.clip_ebc import ClipEBC
import numpy as np

# 모델 초기화
model = ClipEBC()

def predict_crowd(image):
    """
    이미지를 받아서 군중 수를 예측하고 시각화 결과를 반환합니다.
    
    Args:
        image: Gradio에서 받은 이미지 (numpy array)
        
    Returns:
        tuple: (예측된 군중 수, 밀도 맵 시각화, 점 시각화)
    """
    # 예측 수행
    count = model.predict(image)
    
    # 시각화 생성
    _, density_map = model.visualize_density_map()
    _, dot_map = model.visualize_dots()
    
    return (
        f"예측된 군중 수: {count:.1f}명",
        density_map,
        dot_map
    )

# Gradio 인터페이스 생성
with gr.Blocks(title="CLIP-EBC Crowd Counter") as app:
    gr.Markdown("# CLIP-EBC Crowd Counter")
    gr.Markdown("이미지를 업로드하여 군중 수를 예측하고 시각화합니다.")
    
    with gr.Row():
        input_image = gr.Image(type="numpy", label="입력 이미지")
    
    with gr.Row():
        predict_btn = gr.Button("예측", variant="primary")
    
    with gr.Row():
        count_text = gr.Textbox(label="예측 결과")
    
    with gr.Row():
        with gr.Column():
            density_output = gr.Image(label="밀도 맵")
        with gr.Column():
            dots_output = gr.Image(label="점 시각화")
    
    predict_btn.click(
        fn=predict_crowd,
        inputs=input_image,
        outputs=[count_text, density_output, dots_output]
    )

# 앱 실행
if __name__ == "__main__":
    app.launch(share=True)