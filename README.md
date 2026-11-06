# AIMS-mini - IT3180

Bài thực hành quản lý cấu hình phần mềm bằng Git và GitHub của sinh viên
**202416352**. AIMS-mini là chương trình demo dòng lệnh Python, chỉ sử dụng
thư viện chuẩn, dùng để thực hành nhánh, Pull Request, kiểm thử và phát hành.

## Chạy và kiểm thử

Yêu cầu **Python 3.10 trở lên**. Tại thư mục gốc repository, chạy:

```bash
python main.py
python -m unittest discover -s tests -v
```

Chương trình in phiên bản, giỏ DVD mẫu và kết quả tìm kiếm. Tổng tiền mẫu là
**63.89 $**. Phiên bản hiện tại trên `master` là **1.1.0**, có **20 unittest**.

Workflow [CI](.github/workflows/ci.yml) được cấu hình cho PR vào `master` hoặc
`release/**`, và push lên `master`. Nhánh `master` yêu cầu check `test` thành
công trước khi merge. Các tag phát hành cũ đã được kiểm thử trực tiếp khi kiểm toán.

## Báo cáo trả lời câu hỏi thảo luận

[Báo cáo tổng hợp Lab 03-05 và bằng chứng kiểm tra](docs/submission-report.md)
liên kết các PR, Issue, kết quả kiểm thử, bản phát hành và những điều chỉnh theo
mã nền thực tế.

| Lab | Nội dung | Câu trả lời |
|---|---|---|
| 01 | Thiết lập Git, refactor và baseline đầu tiên | [answers-lab01.md](docs/answers-lab01.md) |
| 02 | Feature/topic, Pull Request và ba kiểu merge | [answers-lab02.md](docs/answers-lab02.md) |
| 03 | Bugfix, xung đột và hoàn tác | [answers-lab03.md](docs/answers-lab03.md) |
| 04 | Release, SemVer, tag và kiểm toán cấu hình | [answers-lab04.md](docs/answers-lab04.md) |
| 05 | Hotfix, cherry-pick và bảo trì nhiều phiên bản | [answers-lab05.md](docs/answers-lab05.md) |

Tài liệu bổ sung: [sơ đồ và mô tả use case](docs/use-case.md),
[bằng chứng Lab 03](docs/evidence/lab03.json),
[kết quả kiểm toán các phiên bản](docs/evidence/final-audit.json).

## Các mốc bài nộp

| Lab | Nhánh bài nộp | Tag |
|---|---|---|
| 01 | `release/lab01` | `v0.1.0` |
| 02 | `release/lab02` | `v0.2.0` |
| 03 | `release/lab03` | `v0.3.0` |
| 04 | `release/lab04` | `v1.0.0`, `v1.0.1` (hotfix) |
| 05 | `release/lab05` | `v1.1.0` |

Các tag đều là annotated tag. Các bản phát hành **1.0.0**, **1.0.1** và **1.1.0**
nằm trong [GitHub Releases](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/releases).

`master` là dòng phát triển chính; `release/labXX` giữ mốc nộp và bảo trì của
từng lab. Thay đổi được đưa vào qua PR; không merge nhánh release ngược vào
`master` trong quy trình Lab 03-05.

## Nội dung triển khai thực tế

- Giỏ DVD hiển thị tên, thể loại, giá và tổng tiền; giỏ trống in `The cart is empty`.
- Tìm theo tiêu đề không phân biệt hoa thường, bỏ khoảng trắng ở hai đầu từ khóa;
  từ khóa trống trả về danh sách rỗng. Tìm theo thể loại dùng đối sánh chính xác.
- Giảm giá hỗ trợ phần trăm thập phân; sắp xếp theo tên hoặc giá có tùy chọn đảo chiều.
- Hotfix **1.0.1** sửa tìm kiếm giữa các chuỗi Unicode tương đương bằng chuẩn hóa NFC.
  Commit sửa được chuyển bằng `cherry-pick -x` sang `master` và `release/lab05`;
  commit nâng phiên bản 1.0.1 chỉ thuộc dòng bảo trì 1.0.x.

Mã nền đã có sẵn một số chức năng. Bài tập lỗi giới hạn giỏ hàng được ghi rõ
là tình huống seed trên nhánh riêng; hotfix Unicode thay cho lỗi hoa/thường đã
được sửa sẵn. Chi tiết và bằng chứng được trình bày trong báo cáo, không coi
những chức năng có sẵn là thay đổi mới. Bài làm theo phương án cá nhân, không
có review/approval từ partner.

## Cấu trúc repository

```text
.github/       Mẫu PR và workflow CI
aims/          Mã nguồn DVD, giỏ hàng và tìm kiếm
docs/          Use case, câu trả lời và báo cáo thực hành
tests/         Bộ kiểm thử unittest
CHANGELOG.md   Lịch sử thay đổi theo phiên bản
main.py        Chương trình demo
```
