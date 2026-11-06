# Lab 05 - Hotfix và bảo trì nhiều phiên bản

## Upstream first và release first

Upstream first sửa master trước rồi backport bản sửa về release. Ưu điểm là
dòng phát triển không bị quên, dễ chạy bộ test mới nhất; nhược điểm là mã mới có
thể khác bản cũ và làm việc tái hiện/backport khó hơn.

Release first sửa đúng baseline đang gặp lỗi, phát hành PATCH nhanh rồi chuyển
commit sửa sang các dòng khác. Ưu điểm là tái hiện và kiểm tra trên bản người
dùng đang chạy; nhược điểm là phải theo dõi mọi dòng chịu ảnh hưởng để không
quên chuyển bản sửa. Bài này dùng release first từ release/lab04.

## Điều chỉnh theo mã nền thực tế

Lỗi tìm "lion" không ra "The Lion King" trong ví dụ đề đã được sửa sẵn từ mã
nền. Không làm hỏng lại một bản phát hành để tạo bằng chứng giả. Hotfix thực tế
là hai chuỗi Unicode có cùng cách hiển thị nhưng dạng tổ hợp khác nhau không
khớp nhau: Cafe + dấu sắc tổ hợp không tìm được tiêu đề Café ở dạng dựng sẵn.
Chuẩn hóa NFC trước khi casefold sửa lỗi; kiểm tra thêm chiều đảo lại. Tìm
"lion" vẫn phải thành công trên cả v1.0.1, v1.1.0 và master.

## Vì sao tách commit sửa lỗi và nâng phiên bản?

Commit FIX_SHA chỉ gồm aims/search.py và tests/test_search.py. Commit phiên bản
chỉ đổi __version__ và CHANGELOG thành 1.0.1 trên dòng 1.0.x. Cherry-pick -x
FIX_SHA sang master và release/lab05 giữ được số 1.1.0 của dòng mới; không merge
cả nhánh hotfix để đưa nhầm phiên bản cũ vào master.

## Phát hiện khi quên đưa bản sửa sang release/lab05

```bash
git cherry -v origin/release/lab05 origin/release/lab04
git cherry -v origin/master origin/release/lab04
git log --all --oneline --grep="cherry picked from commit"
git tag --contains FIX_SHA
```

Với git cherry, đối số đầu là dòng nhận để đối chiếu; dấu '-' ở commit sửa lỗi
nghĩa là đã có patch tương đương dù SHA khác. Dấu '+' ở commit nâng số 1.0.1 là
đúng chủ đích, vì không chuyển số bản cũ sang dòng mới. tag --contains kiểm tra
quan hệ tổ tiên, không nhận diện hai patch tương đương có SHA khác.

Trong lần thực hành này, cherry-pick sang dòng mới có xung đột tại dòng chuẩn
hóa tiêu đề. Đã giải quyết và giữ chức năng tìm theo thể loại. `git cherry`
vẫn có thể hiển thị '+' cho bản sửa gốc: patch trên bản cũ còn bổ sung newline
cuối tệp, trong khi dòng mới đã có newline từ trước. Vì patch không hoàn toàn
giống nhau, phải đối chiếu trailer `cherry picked from commit`, mã nguồn và test
hành vi; không kết luận đã quên bản sửa chỉ từ dấu '+' trong trường hợp này.

## Khi nào gắn tag 1.1.0?

Tạo release/lab05 từ trạng thái chuẩn bị 1.1.0, chưa gắn tag. Sau khi chuyển
hotfix vào release/lab05 và kiểm tra xong mới gắn v1.1.0. Nếu tag đã công bố rồi
thì không di chuyển; phát hành PATCH mới, ví dụ v1.1.1.

## CI mở rộng

Workflow CI chạy unittest cho PR vào master/release/** và push lên master.
Job test phải thành công trước khi merge vào master. Bài thử CI cố ý làm sai
tổng tiền chỉ nằm trên nhánh demo riêng, không merge mã lỗi vào bản phát hành.
Các URL PR, SHA hotfix, kết quả kiểm toán và CI thực tế nằm trong báo cáo tổng hợp.
