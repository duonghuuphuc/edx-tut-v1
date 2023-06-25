.. _tutor-settingup:

Cài đặt Open edX bằng Tutor
===========================

Yêu cầu trước khi cài đặt
-------------------------
 * Hệ điều hành được hỗ trợ: Tutor chạy tốt trên các hệ điều hành UNIX 64-Bit. Tutor cũng có thể hoạt động tốt trên Windows (với `WSL 2 <https://learn.microsoft.com/en-us/windows/wsl/install>`_).
 * Phần mềm bắt buộc:

       * `Docker <https://docs.docker.com/engine/install/>`_: v18.06.0+
    
       * `Docker Compose <https://docs.docker.com/compose/install/>`_: v1.22.0+

 * Đảm bảo các dịch vụ web khác không chạy trên các cổng 80 và 443.
 * Phần cứng:

       * Cấu hình tối thiểu: RAM 4 GB, 2 CPU, dung lượng đĩa 8 GB.
       * Cấu hình đề xuất: RAM 8 GB, 4 CPU, dung lượng đĩa 25 GB.

.. note::

   Chúng tôi khuyến khích nên cài đặt Tutor bằng việc sử dụng môi trường ảo Python. Một môi trường ảo là công cụ cho phép chúng ta lưu trữ các thành phần phụ thuộc theo yêu cầu của từng dự án khác nhau ở nhiều nơi riêng biệt.
   
   Bằng việc sử dụng môi trường ảo, chúng ta có thể cài đặt các gói và thư viện cần thiết mà không gây xung đột với các phiên bản và môi trường Python khác trên hệ thống. Điều này giúp đảm bảo rằng Open edX và các thành phần liên quan của phần mềm sẽ hoạt động đúng cách và không ảnh hưởng đến các ứng dụng khác trên máy tính. Bên cạnh đó, môi trường ảo hỗ trợ nhiều nền tảng khác nhau bao gồm Windows, macOS và Linux. Điều này giúp đơn giản hóa quá trình cài đặt và gỡ bỏ Open edX trên các hệ điều hành khác nhau mà không cần lo lắng về sự tương thích.
   
   Trong chuỗi bài viết về Open edX này, chúng tôi sẽ sử dụng môi trường ảo `Anaconda <https://www.anaconda.com/>`_ để cài đặt Tutor. Người đọc có thể tìm hiểu thêm về cách cài đặt và sử dụng Anaconda :ref:`tại đây <anaconda-settingup>`.

Tiến hành cài đặt
-----------------
Sau khi đã cài đặt Anaconda và kích hoạt thành công môi trường ảo, lúc này chúng ta có thể cài đặt Tutor bằng câu lệnh sau:

.. code-block:: console

    pip install "tutor[full]"

Chạy Open edX
-------------
Sau khi cài đặt thành công, tiến hành chạy Open edX bằng câu lệnh: 

.. code-block:: console

    tutor local launch

Ngay sau khi chạy câu lệnh trên, chúng ta sẽ được yêu cầu trả lời một số câu hỏi về các thông tin cấu hình cho việc quản lý hệ thống Open edX.

Tiếp đó hệ thống sẽ khởi tạo các file cấu hình, bắt đầu quá trình tải xuống các Docker image.

Kết quả của quá trình trên là một hệ thống Open edX hoàn chỉnh, sẵn sàng cho việc đẩy lên môi trường production (hiện tại mới nhất là phiên bản `Olive <https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/platform_releases/olive.html>`_).

Toàn bộ quá trình trên có thể mất đến 10 phút trên một máy chủ có băng thông tốt. 

.. note::

    Môi trường host sẽ không bị ảnh hưởng vì mọi thứ đều chạy bên trong Docker container. 

Tạo mới tài khoản người dùng với quyền truy cập nhân viên và quản trị viên
--------------------------------------------------------------------------
Sau khi chạy thành công server Open edX, chúng ta cần phải tạo mới tài khoản người dùng bằng câu lệnh:

.. code-block:: console

    tutor local do createuser --staff --superuser yourusername user@email.com

Ngay sau khi chạy câu lệnh trên, người dùng sẽ được hệ thống yêu cầu cài đặt mật khẩu tương ứng cho tài khoản.

Thêm khóa học vào hệ thống 
--------------------------------------
Nếu đây là lần đầu chúng ta cài đặt Open edX, hệ thống lúc này sẽ chưa có bất kỳ một khóa học nào. Để thêm mới một khóa học trải nghiệm mà Open edX đã cung cấp sẵn, chạy câu lệnh:

.. code-block:: console

    tutor local do importdemocourse

Cấu hình theme cho hệ thống
---------------------------
Theme (chủ đề/giao diện chính) của Open edX có thể được tùy chỉnh để phù hợp các nhu cầu thị giác khác nhau của tổ chức. Chúng ta có thể thực thi đoạn mã dưới đây để thay đổi theme của Open edX:

.. code-block:: console

    tutor local do settheme mytheme

Ngoài ra, Open edX cũng phát triển `Indigo <https://github.com/overhangio/tutor-indigo>`_, một mã nguồn mở có thể tùy chỉnh theme với Tutor.

Tổng kết
--------
LMS (Learning Management System) là một hệ thống quản lý dạy học trực tuyến được sử dụng để tổ chức và cung cấp các khóa học trực tuyến. Một trong những hệ thống LMS phổ biến và mạnh mẽ là Open edX.

Bằng cách sử dụng môi trường ảo Anaconda, người dùng, lập trình viên, người quản trị hệ thống thông tin có thể dễ dàng cài đặt và quản lý máy chủ Open edX.

Sau khi cài đặt thành công, người dùng có thể tạo tài khoản mới trên hệ thống Open edX và thêm khóa học trải nghiệm đã được cung cấp sẵn để kiểm tra và thử nghiệm.

Cuối cùng, người dùng có thể tùy chỉnh giao diện và theme cho hệ thống. Open edX cung cấp các công cụ để tùy chỉnh giao diện theo ý muốn, đồng thời đảm bảo thể hiện chính xác các đặc trưng thương hiệu của những đơn vị đang quản lý hệ thống như tổ chức hoặc trường học.

Với việc thực hiện các bước trên, người đọc có thể bắt đầu xây dựng và triển khai các khóa học trực tuyến trên nền tảng Open edX.

Trong các bài viết tiếp theo, chúng tôi sẽ làm rõ về kiến trúc và cách phát triển XBlock, một công cụ hỗ trợ tùy chỉnh các bài giảng của người học và người dạy. 

