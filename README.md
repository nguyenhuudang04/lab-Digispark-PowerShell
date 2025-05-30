# lab-Digispark-PowerShell
Khám phá bài 🤩: Lab Digital Forensics: Điều khiển máy tính từ Digispark & PowerShell 
Một bài lab đơn giản mà mình đã tìm hiểu nó chỉ là bài lab basic cho những người mới như mình thích khám phá về mảng này 😁 😁
- Các công nghệ và bước mình thực hiện:
✅ Dựng C2 server bằng Python trên VPS Ubuntu (port 8080).

✅ Viết script PowerShell chạy ẩn và gửi lệnh tới server.

✅ Nạp mã vào Digispark để mô phỏng thiết bị USB tấn công.

✅ Theo dõi tương tác: gửi lệnh (`whoami`, `ipconfig`,...) từ VPS về máy nạn nhân.

✅Phân tích Forensics về hệ thống điều tra xem tấn công từ đâu.


![image](https://github.com/user-attachments/assets/c215df16-0e51-4257-8fde-78f2089ec033)

Các bước làm 

✅ Bước 1: Tạo C2 Server trên VPS

Tạo file control_server.py với mã Python server:

python3 control_server.py

✅ Bước 2: Nạp code vào mạch 

✅ Bước 3: Tạo script.ps1 và chạy

cd /var/www/html

sudo python3 -m http.server 80


và Test thử thôi curl "http://localhost:8080/cmd?c=whoami"

