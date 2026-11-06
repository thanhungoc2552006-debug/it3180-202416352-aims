# Lab 04 - Release flow và phiên bản

## Vì sao release/* không merge ngược master?

Trong quy trình học phần, master tiếp tục phát triển; release/labXX lưu bài nộp
và bảo trì baseline cũ. Merge cả release ngược master có thể mang theo phiên bản,
CHANGELOG và thay đổi dành riêng bản cũ. Chuyển commit sửa lỗi cần thiết bằng
cherry-pick -x và giữ phiên bản riêng cho từng dòng. Đây là quy ước của học phần,
không phải hạn chế kỹ thuật của Git.

## So sánh với GitFlow

GitFlow có develop để tích hợp, main cho phát hành và nhánh release để chuẩn bị
phát hành; sửa lỗi thường được đưa lại các dòng dài hạn. Bài này dùng master làm
dòng phát triển, không có develop; release/labXX tồn tại như các dòng bài nộp
song song, không merge ngược master.

## Vì sao 1.0.0 thay vì 0.4.0?

0.y.z thể hiện giai đoạn phát triển ban đầu. Lab 04 chọn 1.0.0 làm mốc ổn định
để phát hành và bảo trì. MAJOR tăng khi phá tương thích, MINOR khi bổ sung tính
năng tương thích, PATCH khi sửa lỗi tương thích. Số lab không quyết định phiên bản.

## Tag khác nhánh release thế nào?

Annotated tag v1.0.0 định danh một commit cụ thể và không di chuyển sau khi công
bố. release/lab04 có thể tiến lên khi nhận bản vá qua PR. Tag và nhánh trùng nhau
ở lúc phát hành 1.0.0; sau hotfix, tag 1.0.0 vẫn ở baseline gốc.

## Chuẩn bị và kiểm toán

Phiên bản và CHANGELOG được sửa trên topic/prepare-release-1.0.0, qua PR vào
master trước khi tạo release/lab04. Các tag cũ v0.1.0, v0.2.0, v0.3.0 trỏ đúng
nhánh bài nộp tương ứng. Kiểm tra tag bằng git cat-file -t và git show; tái tạo
v1.0.0 bằng detached HEAD/worktree, chạy unittest, kiểm tra tệp rác và đóng gói
git archive. Các lệnh A..B liệt kê commit thuộc B mà không thuộc A.

```bash
git log --oneline release/lab04..master
git log --oneline master..release/lab04
git diff --stat v0.3.0 v1.0.0
git describe --tags
git worktree add ../aims-v1.0.0 v1.0.0
```

Mã nền đã có sort_by_title/sort_by_cost trước Lab 04. Sau khi đóng băng 1.0.0,
bài này mở rộng chúng với reverse=True và regression tests. Bằng chứng phân biệt
hai dòng là tham số reverse chỉ có trên dòng phát triển mới, không khẳng định
các hàm sort hoàn toàn vắng trên 1.0.0. Các sai khác với mã tối thiểu của đề được
ghi rõ, không xóa tính năng đang có để tạo lịch sử giả.
