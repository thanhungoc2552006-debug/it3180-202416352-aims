# AIMS-mini - IT3180

Dự án Python nhỏ dùng để thực hành Git/GitHub và quản lý cấu hình phần mềm.
Chương trình demo tạo giỏ DVD mẫu, in chi tiết giỏ hàng và tìm kiếm theo tiêu đề.

## Yêu cầu và cách chạy

- Python 3.10 trở lên.
- Chỉ sử dụng thư viện chuẩn Python, không cần cài gói bổ sung.
- Chạy lệnh từ thư mục gốc của repository:

```bash
python main.py
```

Giỏ hàng mẫu gồm The Lion King, Star Wars và Aladdin; tổng tiền là **63.89 $**.
Mỗi dòng hiển thị tên DVD, thể loại và giá. Giỏ trống hiển thị `The cart is empty`.

## Tìm kiếm theo tiêu đề

`search_by_title(items, keyword)` trả về danh sách DVD có tiêu đề chứa từ khóa:

- Không phân biệt chữ hoa và chữ thường.
- Bỏ khoảng trắng ở đầu và cuối từ khóa, ví dụ `"  LION  "` tìm được The Lion King.
- Từ khóa rỗng hoặc chỉ chứa khoảng trắng trả về danh sách rỗng.
- Không có kết quả phù hợp thì trả về danh sách rỗng.

## Cấu trúc

```text
.github/       Mẫu mô tả Pull Request
aims/          Các lớp DVD, giỏ hàng và hàm tìm kiếm
docs/          Tài liệu thực hành và câu trả lời thảo luận
main.py        Chương trình demo
```

## Quy trình làm việc

Tạo nhánh riêng cho mỗi mục đích, kiểm tra thay đổi rồi mở Pull Request vào
`master`. Đồng bộ nhánh với `origin/master` trước khi tích hợp. Các nhánh
`release/labXX` lưu bài nộp từng lab; không merge ngược nhánh release vào `master`.

## Tài liệu Lab 02

- [Use case và sơ đồ hành vi](docs/use-case.md)
- [Câu trả lời thảo luận và bằng chứng thực hành](docs/answers-lab02.md)
- Mốc bài nộp: nhánh `release/lab02`.


## Báo cáo tổng hợp và các mốc còn lại

- [Báo cáo Lab 03-05 và bằng chứng](docs/submission-report.md)
- [Lab 03](docs/answers-lab03.md), [Lab 04](docs/answers-lab04.md), [Lab 05](docs/answers-lab05.md)
- Bài nộp: release/lab03, release/lab04, release/lab05.
- Phát hành: v1.0.0, v1.0.1 (hotfix), v1.1.0.
- Kiểm thử: `python -m unittest discover -s tests -v` (20 tests).
