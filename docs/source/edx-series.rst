Series tìm hiểu XBlock
=============================

Tổng quan về XBlock
-------------------
XBlock là một trong những thành phần của nền tảng Open edX với mục đích xây dựng giáo trình và bài giảng. XBlock được thiết kế theo mô hình kiến trúc các thành phần (**Component-based Architecture**) nhằm mục tiêu xây dựng các khối chức năng độc lập, có thể tái sử dụng và tích hợp vào các khóa học trực tuyến. XBlock cho phép cộng đồng lập trình viên xây dựng và phát triển chức năng riêng để tích hợp vào khóa học và vẫn hoạt động tốt với các khối chức năng khác. Người quản lý khóa học có thể kết hợp các XBlock khác nhau, từ video, văn bản đến môi trường học tập cộng tác để nâng cao trải nghiệm học viên và giảng viên trong quá trình dạy-học.

.. raw:: html

  <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; gap: 20px; margin-bottom: 20px;">
    <video controls width="640" height="320">
      <source src="_static/xblock-intro.mp4" type="video/mp4">
      Introduction video about XBlock
      <br>
      Source: <a href="https://www.youtube.com/watch?v=xVz5l8E_-Z8">XBlock: Courseware Components from edX - YouTube</a>
    </video>
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; gap: 5px; font-weight: bold;">
        <span>
          Video giới thiệu sơ lược về XBlock
        </span>
          <span>Nguồn: <a href="https://www.youtube.com/watch?v=xVz5l8E_-Z8">XBlock: Courseware Components from edX - YouTube</a>
          </span>
    </div>
  </div>

Một số XBlock phổ biến được duy trì và sử dụng rộng rãi có thể thêm vào các khóa học:

- Các bài tập kéo thả đối tượng.
- Tích hợp Google Drive và Google Calendar.
- Hiển thị các tập tin PDF.
- Tạo biểu mẫu thăm dò ý kiến và khảo sát.

Tìm hiểu thêm tại `Open edX XBlocks available in Tahoe - Appsembler Knowledge Base <https://help.appsembler.com/article/229-open-edx-xblocks-deployed-in-tahoe?_gl=1*12xwjp9*_ga*MTc2NjEwMzQxMy4xNjg4MjkzMDk4*_ga_NMMW6FJLDX*MTY4ODI5MzA5OC4xLjEuMTY4ODI5MzE5OC4wLjAuMA..&_ga=2.85817177.1130629218.1688293098-1766103413.1688293098/>`_

.. raw:: html

  <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; gap: 20px; margin-bottom: 20px;">
    <video controls width="640" height="320">
      <source src="_static/in-video-xblock.mp4" type="video/mp4">
      Introduction video about XBlock
      <br>
      Source: <a href="https://www.youtube.com/watch?v=xVz5l8E_-Z8">XBlock: Courseware Components from edX - YouTube</a>
    </video>
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; gap: 5px; font-weight: bold;">
        <span>
          Video demo XBlock của Open edX
        </span>
          <span>Nguồn: <a href="https://www.youtube.com/watch?v=xVz5l8E_-Z8">XBlock: In-Video Quiz XBlock - Open edX</a>
          </span>
    </div>
  </div>

.. _xblock_requirements:

Điều kiện
---------

Bài viết này hướng đến các lập trình viên. Do đó, độc giả nên có kiến thức cơ bản các công nghệ sau:

- Python
- JavaScript
- HTML và CSS
- Môi trường ảo Python
- Git

Cài đặt môi trường lập trình
----------------------------

Để xây dựng một XBlock, chúng ta cần phải có các công cụ sau trên thiết bị:

Python
^^^^^^

  Để chạy môi trường ảo và XBlock SDK, cũng như để xây dựng XBlock, lập trình viên phải cài đặt Python phiên bản >= 3.8 trên máy tính. Tham khảo thêm tại `đây <https://www.python.org/downloads/>`_

Git
^^^

  Các edX repository, bao gồm XBlock và XBlock SDK hiện nay được lưu trữ phổ biến trên GitHub. Chúng tôi khuyến nghị nên sử dụng Git nhằm dễ dàng kiểm soát mã nguồn trong quá trình phát triển XBlock, đồng thời, thuận tiện cho việc cài đặt và triển khai. Nếu chưa cài đặt Git hoặc chưa được làm quen với công cụ này, người đọc có thể tham khảo thêm `tại đây <https://docs.github.com/en/get-started/quickstart/set-up-git>`_

Môi trường ảo
^^^^^^^^^^^^^

  Việc sử dụng môi trường ảo Python giúp cách ly và quản lý các dependencies của dự án. Người đọc có thể tìm hiểu về thông tin và ưu điểm khi sử dụng môi trường ảo Python trong tài liệu :ref:`Cài đặt và sử dụng Anaconda <anaconda-settingup>`.

Các bước cài đặt XBlock SDK sẽ được mô tả trong phần :ref:`tiếp theo<xblock-sdk-configuration>` của bài viết.

Cài đặt và triển khai XBlock-SDK
--------------------------------

.. toctree::
    :hidden:
    :maxdepth: 2

    xblock-sdk-configuration

Tổng kết
--------

Trong bài viết này, chúng ta đã tìm hiểu về XBlock và cách sử dụng XBlock SDK để xây dựng và phát triển các XBlock. Qua quá trình tạo XBlock, chúng ta đã có cái nhìn tổng quan về quy trình và công cụ cần thiết để tạo ra các phần mở rộng tùy chỉnh trong hệ thống Open edX.

Ở bài viết tiếp theo, chúng tôi sẽ hướng dẫn cài đặt và tích hợp các XBlock phổ biến, cung cấp khả năng tùy chỉnh và mở rộng tính năng của nền tảng học tập trực tuyến để đáp ứng nhu cầu cụ thể của người dùng và tổ chức sử dụng.
