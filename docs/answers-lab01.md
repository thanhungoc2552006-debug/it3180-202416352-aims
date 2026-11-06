# Lab 01 — Thiết lập Git và refactor flow

### Cấu hình `--global` nằm ở đâu? Khác `--local` thế nào?

`git config --global` ghi cấu hình cấp người dùng, thường vào `~/.gitconfig` (hoặc tệp XDG tương ứng). Nó áp dụng cho các repository của cùng tài khoản. `--local` ghi vào `.git/config` của repository hiện tại, chỉ áp dụng ở đó và được ưu tiên hơn giá trị global trùng tên. Có thể xem nguồn gốc từng giá trị bằng `git config --list --show-origin`.

### Vì sao dùng `git mv`?

`git mv` đổi đường dẫn và đưa việc đổi tên vào staging trong một bước, giúp thao tác rõ ràng, giảm nguy cơ quên thêm hoặc xóa tệp. Git thực chất nhận diện rename bằng cách so sánh nội dung; dùng `mv` rồi `git add -A` cũng có thể cho cùng kết quả. `git log --follow -- aims/cart.py` giúp theo dõi lịch sử qua lần đổi tên.

### `release/lab01` có phải baseline không?

Có, nếu nhánh được tạo từ trạng thái `master` đã được kiểm tra và được dùng làm bài nộp Lab 01. Đó là mốc cấu hình được thống nhất. Tuy nhiên đầu nhánh có thể di chuyển khi sửa bài; commit SHA hoặc tag mới xác định một trạng thái bất biến. Có thể kiểm tra mốc ban đầu bằng cách so sánh SHA của `master` và `release/lab01` ngay khi tạo nhánh.

### Vì sao không commit thẳng lên `master` dù làm một mình?

Pull Request lưu mục đích, phạm vi thay đổi và bằng chứng kiểm thử; nó cũng cho cơ hội xem diff trước khi hợp nhất. Quy tắc một đường vào `master` giúp quy trình có thể kiểm toán và giữ nhất quán khi sau này có thêm cộng tác viên. Khi làm một mình, có thể đặt số approval bắt buộc là 0 nhưng vẫn mở PR để duy trì thói quen kiểm thử và kiểm tra lại toàn bộ thay đổi.