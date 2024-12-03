# YouTube AI Bot

YouTube AI Bot là một ứng dụng tiên tiến tích hợp Telegram và Website, cung cấp trải nghiệm thông minh với nội dung YouTube. Ứng dụng sử dụng các công nghệ AI tiên tiến và API để phân tích, tóm tắt và tải video hiệu quả.

## 1. Tổng Quan Dự Án

### 1.1 Giới Thiệu
Ứng dụng tích hợp AI để hỗ trợ người dùng làm việc với nội dung YouTube, giúp tiết kiệm thời gian và tối ưu hóa trải nghiệm.

### 1.2 Mục Tiêu
- Tối ưu hóa trải nghiệm người dùng với nội dung YouTube.
- Cung cấp các công cụ phân tích và xử lý thông minh.
- Đơn giản hóa việc trích xuất thông tin từ video.

## 2. Chức Năng Chính
1. **Tóm Tắt Nội Dung Video**:
   - Trích xuất và tóm tắt nội dung video bằng AI, tiết kiệm thời gian.
2. **Phân Tích Chỉ Số Video YouTube**:
   - Phân tích các chỉ số như lượt xem, lượt thích, bình luận, và đánh giá chất lượng video.
3. **Tải Video YouTube**:
   - Tải video YouTube dễ dàng với liên kết.
4. **Lấy Thumbnail Video**:
   - Tải hình ảnh thumbnail từ video nhanh chóng.

## 3. Kiến Trúc và Công Nghệ
- **Telegram Bot API**: Giao tiếp qua Telegram bằng thư viện `python-telegram-bot`.
- **YouTube Data API**: Lấy dữ liệu video sử dụng `google-api-python-client`.
- **Transcript API**: Lấy phụ đề video với `youtube-transcript-api`.
- **GPT-4, Llama AI**: Tóm tắt nội dung video bằng AI tiên tiến.
- **Video Downloading**: Tải video sử dụng thư viện `youtube-dl`.
- **Poetry**: Quản lý dependencies hiện đại, dễ sử dụng.
- **.env Variables**: Quản lý biến môi trường bằng `python-dotenv`.
- **FASTAPI**: Xây dựng và triển khai RESTful API.
- **ReactJS với TypeScript**: Tạo giao diện frontend chuyên nghiệp, dễ bảo trì.

## 4. Quy Trình Hoạt Động
1. **Khởi tạo Bot**: Gửi lệnh `/start` để bắt đầu.
2. **Tóm Tắt Video**: Sử dụng lệnh `/summary [url]` để tóm tắt nội dung.
3. **Phân Tích Chỉ Số Video**: Dùng lệnh `/analyze [url]` để nhận thông tin chi tiết.
4. **Tải Video**: Gửi lệnh `/download [url]` để tải video.
5. **Tải Thumbnail**: Tải thumbnail video bằng liên kết.


## 5. Cách Chạy Dự Án

### 5.1. Chạy API Backend
```bash
poetry shell
poetry install
cd src
uvicorn main:app
```

### 6.2. Chạy Bot Telegram
```bash
poetry shell
poetry install
cd src
python bot.py
```

## 7. Source Code
- **Backend và Bot**: [YouTube AI Bot Repository](https://github.com/thanhphandev/youtube-bot)
- **Website Frontend**: [YouTube Tool Web Repository](https://github.com/thanhphandev/youtube_tool_web)
