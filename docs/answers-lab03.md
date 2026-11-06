# Lab 03 - Bugfix, xung đột và hoàn tác

## Merge base là gì?

Merge base là tổ tiên chung tốt nhất của hai nhánh. Git dùng bản gốc này cùng hai đầu nhánh để so sánh ba chiều; các sửa đổi không tương thích trên cùng vùng có thể gây xung đột.

Bài tập xung đột có merge base `cfd3402d53033789e50d2833103f9525c21d7326`. Hai nhánh thêm thông báo vào cùng vị trí trong `Cart.add_dvd()`. Đã tạo xung đột thật, kết hợp tiếng Việt với tên DVD, xóa các marker, chạy lại test rồi hoàn tất merge.

## Vì sao master và release/* dùng revert?

`revert` tạo commit đảo ngược mới nên giữ được lịch sử chung và dấu vết kiểm toán. `reset`, amend hoặc rebase có thể thay đổi SHA hoặc bỏ commit khỏi nhánh, chỉ dùng trên lịch sử chưa chia sẻ. Với merge commit cần chọn parent chính; bài này dùng `git revert -m 1 SHA` trên nhánh bugfix rồi mở PR.

## Các tình huống đã làm

- Issue #12: mã nền đã đúng giới hạn 20. Một commit được ghi rõ là **seed bài tập trên nhánh riêng**, sau đó commit test tái hiện FAIL, rồi commit sửa PASS. Không phát hành trạng thái có lỗi lên master. Final diff bổ sung regression test; không khẳng định lỗi có sẵn trên baseline Lab 02.
- Issue #14: lỗi thật khi giảm giá 20.5% do nhân Decimal với float; sửa trên `bugfix/discount-calculation` tạo từ và PR vào `feature/discount`, trước khi feature vào master. Tổng 100 giảm 20.5% còn 79.5; 20% còn 80; dữ liệu không hợp lệ bị từ chối.
- Xung đột: hai nhánh cùng gốc, một nhánh thông báo tiếng Việt, một nhánh thêm tên DVD. Hợp nhất tiếng Việt trước, nhánh còn lại merge origin/master và giải quyết xung đột.
- Hoàn tác merge hiển thị tên DVD bằng commit `52b05ddff17aeccb409ec63ca3c96177c398f0eb`; giữ lại thông báo tiếng Việt trước đó.
- Luyện reset soft/mixed/hard và reflog trong worktree dùng riêng cho bài tập; không reset nhánh chia sẻ. Vì tệp scratch là tệp mới, mixed reset đưa nó về trạng thái untracked. Commit mất khỏi nhánh được tìm lại qua reflog và giữ ở nhánh local topic/undo-recovered.

## Bằng chứng PR

- [cart: PR #13](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/13), base `master`, merge `66301a38b674af1ef351202d48f9576bf356014b`.
- [discount_bug: PR #15](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/15), base `feature/discount`, merge `0345740368f5a0247d3568b64e0ebe646c0e0873`.
- [discount_feature: PR #16](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/16), base `master`, merge `cfd3402d53033789e50d2833103f9525c21d7326`.
- [vietnamese: PR #17](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/17), base `master`, merge `0c3e5e446f19dc22381ed4ed1dabbaed5ccdfdc8`.
- [show_title: PR #18](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/18), base `master`, merge `923f5d3e33c22d780e76d784034a34fd4fa90a61`.
- [revert: PR #19](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/19), base `master`, merge `99205d5c81d64a5fe792cb94597b00d5ccd88011`.

Test giới hạn: `d367890e77c20c947769985450c3c274c185b737` đứng trước fix `d850a1adc9e07965db35ea55fa64cb6f0c79271a`.
Test giảm giá: `ac0c94747065e10a22056a433fbd4e9ef2a2f4a5` đứng trước fix `43debe314db111f1da1726fabdcc5c837543030b`.

Chạy `python -m unittest discover -s tests -v`: 12 test PASS. Các lần FAIL có chủ đích và kết quả chi tiết nằm trong [evidence/lab03.json](evidence/lab03.json).

Làm một mình: PR bắt buộc, số approval bắt buộc bằng 0; không giả lập review của partner. Mốc bài nộp là `release/lab03`.
