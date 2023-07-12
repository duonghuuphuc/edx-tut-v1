.. _first-xblock:

*******************
Tạo XBlock đầu tiên
*******************

Tạo XBlock mới
-------------------

Di chuyển đến thư mục **xblock_development**, chạy file **workbench-make-xblock** bằng lệnh python:

.. code-block:: console

  python xblock-sdk/bin/workbench-make-xblock

Sau khi chạy, cửa sổ Command yêu cầu chúng ta cung cấp các thông tin cấu hình cho XBlock:

.. code-block:: console

	Short name: myxblock
	Class name: MyXBlock

.. note::

  - Short name nên chỉ gồm một từ duy nhất, tất cả ký tự đều viết thường. Ví dụ, trong trường hợp muốn tạo Question Generation XBlock, chúng ta có thể đặt là “questgen”.

  - Class name là tên class hợp lệ trong ngôn ngữ Python và nên kết thúc bằng “XBlock”, cùng ví dụ ở trên, lúc này ta có thể đặt là “QuestGenXBlock”.

Sau khi nhập xong 2 thông tin trên, một thư mục mới được tạo ra nằm bên trong thư mục **xblock_development**. Thư mục mới này chứa các thư mục con và các tập tin để cài đăt XBlock.
Trong quá trình nhập thông tin, có thể bấm tổ hợp phím “Ctrl + C” để dừng và quay trở lại.

Cài đặt XBlock <myxblock>
-------------------------

Sau khi tạo mới XBlock, ta phải cài đặt vào trong XBlock-SDK.
Dùng lệnh **pip** để cài đặt **myxblock**:

.. code-block:: console

  pip install -e myxblock

Khởi tạo SQLite Database
------------------------

Chạy lệnh migrate để tạo database và các bảng:

.. code-block:: console

  python xblock-sdk/manage.py migrate

Chạy XBlock-SDK server
----------------------

Bây giờ chúng ta có thể khởi động XBlock SDK bằng câu lệnh sau:

.. code-block:: console

  python xblock-sdk/manage.py runserver

Nếu chúng ta không chỉ định cổng giao tiếp, server XBlock SDK mặc định sẽ sử dụng cổng 8000. Có thể truyền tham số trong câu lệnh runserver để chỉ định cổng nếu không muốn sử dụng cổng mặc định:

.. code-block:: console

  python xblock-sdk/manage.py runserver 3000

Lập trình viên có thể truy cập http://localhost:8000 (cổng mặc định) thông qua trình duyệt web để kiểm tra xem XBlock SDK có chạy thành công hay không.

.. raw:: html

  <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; gap: 20px; margin-bottom: 20px;">
    <img src="_static/images/sdk-success.png" alt="Giao diện server XBlock-SDK trên localhost khi thực thi thành công" style="max-width: 480px; width: 100%; object-fit: cover;"></img>
    <span style="font-weight: bold;">Giao diện server XBlock-SDK trên localhost khi thực thi thành công.
    </span>
  </div>
