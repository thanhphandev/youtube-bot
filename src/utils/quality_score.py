from datetime import datetime, timezone

def calculate_quality_score(views, likes, comments, upload_date, weights=(0.4, 0.5, 0.1)):
    """
    Tính điểm chất lượng video dựa trên lượt xem, lượt thích, lượt bình luận và ngày đăng tải.
    
    Args:
    - views: Số lượt xem video.
    - likes: Số lượt thích (likes).
    - comments: Số lượt bình luận (comments).
    - upload_date: Ngày đăng tải video (chuỗi định dạng ISO).
    - weights: Trọng số cho like_rate, engagement, age_factor).

    Returns:
    - Điểm chất lượng video (trên thang 100).
    """
    #like_rate: Đo mức độ quan tâm của người xem đối với video. Nếu số lượt thích cao so với lượt xem, điểm chất lượng sẽ tăng.
    #engagement: Đo mức độ tương tác chung của người xem với video (bao gồm cả bình luận), giúp đánh giá mức độ phổ biến và sự hấp dẫn của video.
    #age_factor: Giảm dần theo thời gian, khuyến khích các video mới có điểm cao hơn.

    if isinstance(upload_date, str):
        upload_date = datetime.fromisoformat(upload_date.replace("Z", "+00:00"))

    # Lấy ngày hiện tại
    current_date = datetime.now(timezone.utc)

    # Tính số ngày kể từ khi video được đăng tải
    age_in_days = (current_date - upload_date).days

    # Chuyển views, likes, comments thành số nguyên
    likes = int(likes)
    views = int(views)
    comments = int(comments)

    # Tính tỷ lệ lượt thích và tỷ lệ tương tác
    like_rate = likes / views if views > 0 else 0
    engagement = (likes + comments) / views if views > 0 else 0

    # Tính yếu tố thời gian
    age_factor = max(0, 1 - age_in_days / 365)  # Giảm dần theo năm

    # Trọng số cho các yếu tố
    W1, W2, W3 = weights

    # Tính điểm chất lượng
    quality_score = W1 * like_rate + W2 * engagement + W3 * age_factor

    return round(quality_score * 100, 2)
