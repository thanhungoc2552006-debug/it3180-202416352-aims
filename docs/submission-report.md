# Báo cáo thực hành Git/GitHub - Lab 03, 04 và 05

- Sinh viên/MSSV: **202416352**.
- Repository: [thanhungoc2552006-debug/it3180-202416352-aims](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims).
- Ngày hoàn thành: **06/11/2026** (Asia/Bangkok).
- Hình thức: làm một mình, bắt buộc PR, số approval bắt buộc bằng 0.

## Kết quả tổng hợp

| Phần | Kết quả |
|---|---|
| Lab 03 | Test FAIL/PASS; bugfix vào feature; xung đột thật; revert merge; reset/reflog riêng biệt |
| Lab 04 | SemVer, CHANGELOG, tag annotated, GitHub Release, bảo vệ release/*, tái tạo baseline và ZIP |
| Lab 05 | Hotfix từ bản phát hành, PATCH 1.0.1, hai cherry-pick -x, phiên bản 1.1.0, kiểm toán và CI |

## 1. Lab 03 - Sửa lỗi, xung đột và hoàn tác

Đã thực hiện bài tập giới hạn 20 DVD: commit seed được đánh dấu rõ trên nhánh riêng, test tái hiện FAIL rồi fix PASS. Mã baseline ban đầu đã đúng nên không khẳng định lỗi tồn tại trên Lab 02. Lỗi giảm giá thập phân là lỗi thực tế: Decimal nhân float gây TypeError; sau sửa, tổng 100 giảm 20.5% còn 79.5. PR bugfix có base feature/discount rồi feature mới vào master.

Hai nhánh sửa cùng dòng thông báo đã gây conflict thật. Đã kết hợp tiếng Việt với tên DVD, chạy lại test, rồi thực hiện revert -m 1 qua PR để quay về thông báo tiếng Việt trước đó. Reset soft/mixed/hard chỉ chạy trong worktree dùng riêng; reflog tìm lại commit và giữ nhánh phục hồi local. Không reset hay force push lịch sử chung.

Chi tiết: [answers-lab03.md](answers-lab03.md) và [evidence/lab03.json](evidence/lab03.json).

## 2. Lab 04 - Phát hành và tái tạo phiên bản

Chuẩn bị 1.0.0 và CHANGELOG qua PR vào master, sau đó tạo release/lab04, tag annotated v1.0.0 và GitHub Release. Các tag v0.1.0/v0.2.0/v0.3.0 trỏ về mốc lab tương ứng. Quy tắc release/* bắt buộc PR, áp dụng cho quản trị viên, chặn force push và xóa nhánh. Lần push thử lên release/lab04 trước khi có PR đã bị từ chối.

Đã tái tạo v1.0.0 trong worktree riêng và chạy 12 test đạt. Tệp ZIP được tạo bằng git archive từ chính tag. Sau đóng băng, mở rộng sort với reverse=True trên master; baseline 1.0.0 không có tham số mới. Các hàm sort tăng dần đã có từ mã nền nên không khẳng định chúng hoàn toàn vắng trên bản cũ.

Chi tiết: [answers-lab04.md](answers-lab04.md).

## 3. Lab 05 - Hotfix và bảo trì nhiều dòng

Dòng 1.1 bổ sung tìm theo thể loại và sắp xếp đảo chiều. release/lab05 được tạo trước hotfix nhưng chưa gắn tag. Lỗi gốc trong đề là tìm kiếm phân biệt hoa thường đã được sửa sẵn; bài này thay bằng lỗi Unicode thật: chuỗi Café dựng sẵn không khớp Cafe + dấu sắc tổ hợp. Test thất bại trên 1.0.0, thành công sau chuẩn hóa NFC.

- Commit sửa hành vi/test: `f2c2ee323a7d34a989a7204e9ec897b8636ac886`.
- Cherry-pick vào master: `a9aaef0cef86648be3185912b4243b9286900365`.
- Cherry-pick vào release/lab05: `be2a5070c32760a691ff983139326df91cb04348`.
- Commit nâng 1.0.1 tách riêng, không chuyển số phiên bản cũ sang dòng 1.1.
- Diff v1.0.0 -> v1.0.1 đúng 4 tệp: search.py, test_search.py, __init__.py, CHANGELOG.md.
- Hai commit chuyển bản sửa đều có trailer `cherry picked from commit`.
- Cả v1.0.1, v1.1.0 và master đều tìm lion và Unicode tương đương thành công.

Cherry-pick có xung đột và đã được giải quyết. git cherry vẫn hiện dấu + cho fix gốc do patch cũ còn thay newline cuối tệp; không dùng dấu + đơn lẻ để kết luận thiếu bản sửa. Đối chiếu trailer, diff mã và kiểm thử hành vi xác nhận bản sửa đã có.

Chi tiết: [answers-lab05.md](answers-lab05.md).

## 4. Các phiên bản đã kiểm tra

| Ref | Version trong mã | Số unittest đạt | Unicode tương đương |
|---|---|---:|---|
| `v0.1.0` | `0.1.0` | Chưa có bộ test | Chưa sửa |
| `v0.2.0` | `0.1.0` | Chưa có bộ test | Chưa sửa |
| `v0.3.0` | `0.1.0` | 12 | Chưa sửa |
| `v1.0.0` | `1.0.0` | 12 | Chưa sửa |
| `v1.0.1` | `1.0.1` | 13 | Khớp |
| `v1.1.0` | `1.1.0` | 20 | Khớp |
| `origin/master` | `1.1.0` | 20 | Khớp |

Mọi ref trong bảng chạy demo với tổng **63.89 $**. Các tag đều là annotated tag. Các tag lab đầu đánh dấu bài nộp; mã nền giữ __version__ 0.1.0 đến lúc chuẩn bị 1.0.0.

## 5. Pull Request và Issue

| Công việc | PR | Nhánh đích | Trạng thái |
|---|---|---|---|
| cart | [#13](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/13) | `master` | Merged |
| discount_bug | [#15](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/15) | `feature/discount` | Merged |
| discount_feature | [#16](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/16) | `master` | Merged |
| vietnamese | [#17](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/17) | `master` | Merged |
| show_title | [#18](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/18) | `master` | Merged |
| revert | [#19](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/19) | `master` | Merged |
| lab03_report | [#20](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/20) | `master` | Merged |
| prepare100 | [#21](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/21) | `master` | Merged |
| sort | [#22](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/22) | `master` | Merged |
| category | [#23](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/23) | `master` | Merged |
| prepare110 | [#24](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/24) | `master` | Merged |
| hotfix | [#26](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/26) | `release/lab04` | Merged |
| port_master | [#27](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/27) | `master` | Merged |
| port_lab05 | [#28](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/28) | `release/lab05` | Merged |
| ci | [#29](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/29) | `master` | Merged |
| ci_demo | [#30](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/pull/30) | `master` | Đóng, không merge (demo CI lỗi có chủ đích) |

Các Issue bài tập giỏ hàng, lỗi giảm giá và hotfix Unicode đều đã đóng.

## 6. CI và kiểm tra chặn lỗi

- Workflow: `.github/workflows/ci.yml`, Python 3.12, job `test`, quyền đọc contents.
- Trigger cấu hình: PR vào master/release/** và push vào master.
- Actions được ghim bằng commit SHA của bản phát hành chính thức.
- [CI thành công](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/actions/runs/42192605625): 20 test đạt trên GitHub Actions.
- [CI demo thất bại có chủ đích](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/actions/runs/42192690087): sai tổng tiền, merge bị chặn.
- PR demo đã đóng, không merge mã lỗi; master yêu cầu check test thành công trước khi merge.
- CI được bổ sung sau các tag sản phẩm; các tag cũ được kiểm thử trực tiếp trong worktree, không ghi nhận chúng có workflow từ trước.

## 7. Mốc nộp và phát hành

| Lab | Nhánh nộp | Tag |
|---|---|---|
| 03 | release/lab03 | v0.3.0 |
| 04 | release/lab04 | v1.0.0 và v1.0.1 |
| 05 | release/lab05 | v1.1.0 |

- [Release 1.0.0](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/releases/tag/v1.0.0)
- [Release 1.0.1](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/releases/tag/v1.0.1)
- [Release 1.1.0](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/releases/tag/v1.1.0)
- [ZIP tái tạo baseline 1.0.0](https://github.com/thanhungoc2552006-debug/it3180-202416352-aims/releases/download/v1.0.0/AIMS-mini-1.0.0.zip)

Nhánh release/lab01 và release/lab02 giữ nguyên SHA trước lần thực hành này. Không di chuyển tag đã công bố, không merge release ngược master trong Lab 03-05.

## 8. Phạm vi và sai khác với ví dụ trong đề

- Làm một mình nên không có Request changes/Approve của partner; không tạo bằng chứng review giả.
- Mã nền có sẵn nhiều tính năng. Lỗi seed được đánh dấu rõ và chỉ sống trên nhánh bài tập; các thay đổi bổ sung và hotfix thực tế được mô tả theo đúng code.
- Các số lượng test, SHA, PR, kết quả FAIL/PASS và CI trong báo cáo là dữ liệu đã kiểm tra, không dùng nguyên số minh họa của tài liệu.
- Bằng chứng máy đọc được: [evidence/final-audit.json](evidence/final-audit.json).
- Báo cáo không thay thế thao tác nộp link repository lên LMS của sinh viên.

Tài liệu đối chiếu: IT3180_0504_C5.4-Thuc-hanh-Git-GitHub, phần Lab 03-05 (trang 36-64).
