# CLIP-EBC: Crowd Counting with CLIP

CLIP-EBC 추론파트를 가져왔습니다.
이미지 내의 군중 수를 계산하고 시각화해주는 레포입니다.

## 설치 방법

```bash
pip install -r requirements.txt
```

## Gradio
```bash
python app.py
```

## 주요 기능

- 이미지 내 군중 수 예측
- 밀도 맵 시각화
- 점 형태의 군중 위치 시각화
- 이미지 파일 또는 넘파이 배열 입력 지원
- 시각화 결과 저장 기능


## 매개변수 설정
- `sliding_window`: use the sliding window prediction method or not in evaluation. Could be useful for transformer-based models.
- `window_size`: the size of the sliding window.
- `stride`: the stride of the sliding window.
- `strategy`: how to handle overlapping regions. Choose from `"average"` and `"max"`.
- `resize_to_multiple`: resize the image to the nearest multiple of `window_size` before sliding window prediction.
- `zero_pad_to_multiple`: zero-pad the image to the nearest multiple of `window_size` before sliding window prediction.

**Note**: When using sliding window prediction, if the image size is not a multiple of the window size, then the last stride will be smaller than `stride` to produce a complete window.


```python
model = ClipEBC(
    truncation=4,          # 잘라내기 매개변수
    reduction=8,           # 축소 비율
    granularity="fine",    # 세분화 수준
    window_size=224,       # 슬라이딩 윈도우 크기
    stride=224,            # 슬라이딩 윈도우 이동 간격
    # 기타 매개변수...
)
```


## 사용 방법

### Python 코드에서 사용
```python
from custom.clip_ebc import ClipEBC

model = ClipEBC()

# 이미지에서 군중 수 예측
count = model.predict("path/to/image.jpg")
print(f"예측된 군중 수: {count}")

# 밀도 맵 시각화
fig, density_map = model.visualize_density_map(
    alpha=0.5,  # 투명도 설정
    save=True,  # 이미지 저장
    save_path="density_map.png"  # 저장 경로 지정 (선택사항)
)

# 점 형태로 시각화
fig, dot_map = model.visualize_dots(
    dot_size=20,  # 점 크기
    sigma=1,      # Gaussian 필터 설정
    percentile=97, # 임계값 백분위수
    save=True,    # 이미지 저장
    save_path="dot_map.png"  # 저장 경로 지정 (선택사항)
)
```

### 명령줄 인터페이스(CLI) 사용

main.py를 사용하여 명령줄에서 CLIP-EBC를 실행할 수 있습니다.

#### 기본 사용법

```bash
python main.py --image path/to/image.jpg
```

#### 시각화 옵션

시각화 타입을 선택할 수 있습니다:
```bash
# 밀도 맵만 시각화
python main.py --image path/to/image.jpg --visualize density

# 점 형태로만 시각화
python main.py --image path/to/image.jpg --visualize dots

# 모든 시각화 수행
python main.py --image path/to/image.jpg --visualize all
```

#### 시각화 매개변수 설정

```bash
# 밀도 맵 투명도 설정
python main.py --image path/to/image.jpg --visualize density --alpha 0.7

# 점 시각화 설정
python main.py --image path/to/image.jpg --visualize dots --dot-size 30 --sigma 1.5 --percentile 95
```

#### 결과 저장

```bash
# 기본 디렉토리에 저장
python main.py --image path/to/image.jpg --visualize all --save

# 사용자 지정 디렉토리에 저장
python main.py --image path/to/image.jpg --visualize all --save --output-dir my_results
```

#### CLI 매개변수 설명

| 매개변수 | 설명 | 기본값 |
|----------|------|---------|
| `--image` | 입력 이미지 경로 (필수) | - |
| `--visualize` | 시각화 타입 ('density', 'dots', 'all', 'none') | 'none' |
| `--save` | 결과 저장 여부 | False |
| `--output-dir` | 결과 저장 디렉토리 | 'results' |
| `--alpha` | 밀도 맵 투명도 (0~1) | 0.5 |
| `--dot-size` | 점 크기 | 20 |
| `--sigma` | Gaussian 필터 시그마 값 | 1.0 |
| `--percentile` | 점 시각화 임계값 백분위수 (0~100) | 97 |


