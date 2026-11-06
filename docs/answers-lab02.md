# Lab 02 - Feature/Topic flow và Pull Request

## 1. Vì sao phải đồng bộ master trước khi gửi PR?

Nhánh tính năng có thể được tạo trước khi người khác hợp nhất thay đổi mới.
`git fetch origin` cập nhật thông tin remote, nhưng chưa thay đổi mã trong nhánh
đang làm. `git merge origin/master` đưa mã mới vào nhánh để phát hiện xung đột
và kiểm tra các phần thay đổi có hoạt động cùng nhau hay không.

Trong bài này, `feature/search-by-title` được tạo ở bản clone `aims-dev2` trước
khi PR in giỏ hàng vào `master`. Nhánh tìm kiếm nhận `origin/master` bằng merge
commit `c8ac76f` rồi chạy lại demo: giỏ có thể loại DVD, tổng tiền 63.89 $ và
kết quả tìm kiếm đúng. Không chỉ kiểm tra hai chức năng riêng lẻ, bước này còn
kiểm tra trạng thái tích hợp dự kiến trước khi gửi PR.

## 2. Khi nào không được rebase?

Không tự ý rebase lịch sử chung mà người khác đã dựa vào, đặc biệt là `master`,
`release/*` hoặc nhánh chia sẻ. Rebase tạo lại commit với SHA mới; force push
sau đó có thể làm mất công việc hoặc làm các bản clone lệch lịch sử.

Có thể rebase nhánh riêng chưa được người khác sử dụng. Muốn hoàn tác commit
đã công bố thì dùng `git revert` qua nhánh riêng và PR. Tùy chọn **Rebase and
merge** của GitHub tạo các commit mới trên nhánh đích từ một PR; đây khác với
việc tự viết lại các commit cũ của `master` rồi force push.

## 3. feature/* khác topic/* như thế nào?

`feature/*` dành cho hành vi/chức năng của sản phẩm, ví dụ in thông tin giỏ DVD
hoặc chuẩn hóa từ khóa tìm kiếm. `topic/*` dành cho một chủ đề khác như tài
liệu, mẫu PR hay quy trình. Cả hai đều là nhánh công việc sống ngắn, được tạo
từ `master`, có một mục đích rõ ràng và đưa vào `master` qua PR.

Tên nhánh là quy ước giúp người xem hiểu mục đích; Git không áp dụng cơ chế
khác nhau chỉ vì tiền tố tên nhánh khác nhau.

## 4. So sánh ba kiểu merge

| Cách hợp nhất | Commit chi tiết trên master | Đặc điểm |
|---|---|---|
| Merge commit | Giữ các commit nguồn | Thêm commit có hai parent, thể hiện điểm hợp nhất |
| Squash and merge | Gộp thay đổi thành một commit mới | Gọn theo PR, không giữ từng commit nguồn trong lịch sử master |
| Rebase and merge | Giữ từng thay đổi thành commit riêng với SHA mới | Lịch sử tuyến tính tại điểm tích hợp, không thêm merge commit |

Revert một merge commit cần chọn parent chính, thường là `git revert -m 1 SHA`.
Squash có thể được đảo bằng một revert cho commit squash; một PR rebase nhiều
commit có thể cần đảo nhiều commit. Sau squash/rebase, `git branch -d` có thể
không nhận ra nhánh đã được tích hợp; phải xác nhận PR đã Merged trước khi
xóa nhánh công việc bằng cách khác.

## 5. Bằng chứng trong repository

| Phần thực hành | Bằng chứng |
|---|---|
| Mẫu mô tả PR | [PR #6](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/6), `.github/pull_request_template.md` |
| In giỏ hàng, Merge commit | [PR #7](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/7), merge commit `f910d4d` |
| Tìm kiếm, Squash and merge | [PR #8](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/8), commit squash `943b0b4` |
| Tài liệu use case | [PR #9](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/9), [use-case.md](use-case.md) |
| Câu trả lời và liên kết tài liệu, Rebase and merge | [PR #10](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/10) |
| Bài nộp | Nhánh `release/lab02`, tạo từ master sau khi hoàn tất các PR Lab 02 |

Có thể đối chiếu hình dạng lịch sử bằng:

```bash
git fetch origin
git log --oneline --graph --all
git show -s --format="%h %p %s" f910d4d
git show -s --format="%h %p %s" 943b0b4
```

`f910d4d` có hai parent; `943b0b4` có một parent. Các commit tài liệu của PR #10
được tích hợp bằng Rebase and merge, nên SHA trên master khác SHA nhánh nguồn.

PR #9 được GitHub đánh dấu Merged khi commit `8165e78` của PR đang mở được
đưa vào master bằng fast-forward. SHA nguồn và SHA tích hợp của PR này giống
nhau, nên không dùng PR #9 làm bằng chứng cho Rebase and merge. PR #10 thực
hiện riêng thao tác Rebase and merge để thể hiện đúng sự khác biệt.

## 6. Cấu hình và cách làm một mình

- `master` bắt buộc Pull Request; quy tắc áp dụng cả với quản trị viên.
- Không cho force push, không cho xóa `master`.
- Bật cả ba cách merge và tự động xóa nhánh công việc sau khi PR được merge.
- Cấu hình hủy approval cũ khi diff thay đổi; số approval bắt buộc là **0**
  theo lựa chọn làm một mình của tài liệu.
- Hai bản clone `aims` và `aims-dev2` mô phỏng hai nơi làm việc độc lập cùng
  một remote; không tạo thêm một người review thật.
- Không có partner, nên không có vòng **Request changes -> Approve** của
  người thứ hai. Không ghi nhận hay giả lập approval không có thật.

Mã nền đã có sẵn các hàm in giỏ và tìm kiếm. Thay đổi thực tế của Lab 02 là
bổ sung thể loại vào kết quả in, gọi `print_cart()` trong demo, chuẩn hóa từ
khóa tìm kiếm và mô tả lại hành vi. Vì vậy lịch sử chức năng khác ví dụ bắt đầu
từ mã tối thiểu trong tài liệu; phần thao tác nhánh/PR vẫn được thực hiện.

## 7. Kiểm tra trước khi nộp

- Demo chạy được và giỏ mẫu có tổng **63.89 $**.
- Giỏ trống in `The cart is empty`.
- Tìm `"  LION  "` trả về `The Lion King`; từ khóa trống và không khớp trả `[]`.
- Danh sách đầu vào của tìm kiếm không bị thay đổi.
- Có mẫu PR, tài liệu use case, câu trả lời thảo luận và ba kiểu merge.
- Toàn repository có ít nhất 5 PR đã merge; xem tab Pull requests để kiểm tra.
- Nhánh `release/lab02` lưu mốc bài nộp; giữ nguyên nhánh bài nộp Lab 01.

Đã kiểm tra bảo vệ nhánh bằng cách thử push commit `81dca4f` lên master trước
khi mở PR #10. GitHub từ chối với lỗi `GH006: Protected branch update failed`
và `Changes must be made through a pull request`. Sau đó commit được đẩy lên
nhánh `topic/answers-lab02`, mở PR #10 và tích hợp qua PR.
