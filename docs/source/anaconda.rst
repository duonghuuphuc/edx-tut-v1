.. _anaconda-settingup:

Cài đặt và sử dụng Anaconda
===========================

Giới thiệu
----------
Anaconda là một bản phân phối phần mềm mã nguồn mở phát triển trên nền 2 ngôn ngữ lập trình Python và R dành cho người dùng cuối. Anaconda cung cấp một môi trường phát triển tích hợp (IDE) và một bộ công cụ mạnh mẽ cho việc quản lý các gói phần mềm và môi trường ảo Python.

Anaconda bao gồm Python, các thư viện phổ biến như NumPy, Pandas, Matplotlib và Scikit-learn, cũng như các công cụ quản lý package như Conda. Anaconda giúp người dùng dễ dàng cài đặt, quản lý và cập nhật các gói phần mềm phức tạp trong môi trường Python. Ngoài ra, Anaconda còn hỗ trợ việc tạo và quản lý môi trường ảo để phát triển và triển khai các dự án Python một cách độc lập.

Với tính năng linh hoạt, đa nền tảng và khả năng tích hợp mạnh mẽ, Anaconda đã trở thành một công cụ quan trọng trong lĩnh vực khoa học máy tính (khoa học dữ liệu, ứng dụng học máy, xử lý dữ liệu lớn, phân tích dự đoán số liệu, …).

Cài đặt Anaconda
----------------
Bước đầu tiên, hãy `cài đặt Anaconda <https://www.anaconda.com/download/>`_.

Sau khi cài đặt thành công, bước tiếp theo chúng ta cần tạo một môi trường ảo mới bên trong Anaconda Prompt (hoặc bên trong terminal trên Linux/macOS).

* **Windows**: Mở Start, tìm kiếm và chọn Anaconda Prompt.
* **macOS**: Mở Launchpad, sau đó mở terminal hoặc iTerm.
* **Linux-CentOS**: Mở Applications - System Tools - terminal.
* **Linux-Ubuntu**: Mở Dash bằng cách click vào biểu tượng Ubuntu ở góc trên bên trái màn hình, sau đó nhập từ khóa "terminal".

Tạo mới môi trường ảo
---------------------
Để tạo một môi trường ảo mới có tên là py310, đồng thời cài đặt python phiên bản 3.10.6, ta sử dụng câu lệnh:

.. code-block:: console

    conda create –-name py310 python=3.10.6

Nếu muốn tìm hiểu thêm về các câu lệnh được sử dụng trong Anaconda, người đọc có thể tham khảo `tại đây <https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf>`_.

Kích hoạt môi trường ảo
------------------------
Sau khi đã tạo mới thành công, để có thể sử dụng môi trường ảo này ta cần kích hoạt bằng câu lệnh:

.. code-block:: console

    conda activate py310

.. note:: 
    py310 ở đây chính là tên của môi trường mà chúng ta đã tạo ở trên.

    Khi môi trường đã được kích hoạt, Anaconda Prompt sẽ hiển thị tên của môi trường vừa được kích hoạt nằm trong cặp ngoặc đơn.
