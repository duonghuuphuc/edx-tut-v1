.. _xblock-sdk-configuration:

*******************
Cài đặt XBlock-SDK
*******************

Trước khi đi tiếp ở phần này, lập trình viên đảm bảo rằng đã làm quen và cài đặt đầy đủ trên máy tính các công nghệ trong phần :ref:`điều kiện <xblock_requirements>` khi xây dựng XBlock.

Đầu tiên, tiến hành tạo một thư mục mới có tên là **xblock_development**. Trong thư mục này sẽ lưu trữ tất cả mọi thứ chúng ta sẽ làm việc liên quan đến XBlock, gồm có môi trường ảo, XBlock SDK và các XBlock sẽ phát triển.

Anaconda Command Prompt:

.. code-block:: console

  mkdir xblock_development

Truy cập đến thư mục vừa tạo:

.. code-block:: console

  cd xblock_development

Tạo môi trường có tên "venv" đồng thời cài đặt Python phiên bản 3.8:

.. code-block:: console

  conda create -n venv python=3.8

Kích hoạt môi trường vừa được tạo:

.. code-block:: console

  conda activate venv

Sau khi tạo và kích hoạt môi trường ảo thành công, thực hiện các bước sau để tiến hành clone XBlock SDK, và cài đặt các thư viện, các package theo yêu cầu.

Clone Xblock SDK repository từ GitHub qua lệnh git:

.. code-block:: console

  git clone https://github.com/edx/xblock-sdk.git

Sau khi clone thành công XBlock-SDK, tạo thư mục var:

.. code-block:: console

  mkdir var

Truy cập thư mục xblock-sdk:

.. code-block:: console

  cd xblock-sdk

Cài đặt các thư viện theo yêu cầu:

.. code-block:: console

  pip install -qr requirements/dev.txt --exists-action w

Hoặc

.. code-block:: console

  make install

Trở về thư mục gốc “xblock_development” bằng câu lệnh:

.. code-block:: console

  cd ..

Sau khi thực hiện các bước trên xong, chúng ta có thể khởi động XBlock-SDK với câu lệnh:

.. code-block:: console

  python xblock-sdk/manage.py runserver 3000

Ở phần :ref:`tiếp theo <first-xblock>` của bài viết, chúng ta sẽ cùng nhau tạo một XBlock đầu tiên.
