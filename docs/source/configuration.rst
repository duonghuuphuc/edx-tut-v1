.. _configuration:

Cài đặt và chạy Open edX
=========================
Trước khi cài đặt Open edX, chúng ta cần phải xác định:
  * **Phiên bản phần mềm**
  * **Phương thức cài đặt**

Phiên bản phần mềm
-------------------
Hiện tại Open edX cung cấp 2 lựa chọn về phiên bản:
 * **Master**: có thể hiểu là phiên bản mã nguồn mới nhất, thậm chí còn mới hơn cả phiên bản mã nguồn mà tên miền `edx.org <https://www.edx.org/>`_ đang chạy ổn định.
 * **Release**: là phiên bản mã nguồn được đánh dấu và thử nghiệm cho mục đích sử dụng rộng rãi. Các phiên bản này được đặt tên theo thứ tự bảng chữ cái tên các loài cây: Juniper, Koa, Lilac, ...

.. note:: 

   Độc giả chỉ nên cân nhắc chọn phiên bản Master trong trường hợp có nhu cầu điều chỉnh và phát triển mã nguồn hoặc khi cần trải nghiệm tính năng/ bản sửa lỗi mới nhưng chưa được chính thức áp dụng ở phía người dùng cuối.

Phương thức cài đặt
-------------------
Các phương thức cài đặt hiện đang được Open edX hỗ trợ là:
 * **Tutor**: Một môi trường dựa trên `Docker <https://www.docker.com/>`_ được cộng đồng hỗ trợ phù hợp cho môi trường production và development.
 * **Native**: Cung cấp phương thức cài đặt có thể được dùng cho cả phiên bản **Master** và **Release**, hệ thống sau khi được cài đặt sẵn sàng đẩy lên môi trường production cho mục đích kiểm thử.
 * **Devstack**: Môi trường phát triển dựa trên `Docker <https://www.docker.com/>`_, sẽ hữu ích nếu chúng ta muốn sữa đổi mã nguồn Open edX trên các thiết bị cục bộ, chẳng hạn như máy tính cá nhân hoặc máy chủ trong mạng nội bộ.
Việc chọn phương thức cài đặt tùy thuộc vào mục đích của chúng ta:

   =============================================== ========= ==================
   Mục đích/Kịch bản                               Phiên bản Phương thức
   =============================================== ========= ==================
   Chạy môi trường production                      Release   Tutor hoặc Native
   Cài đặt môi trường kiểm thử tương tự production Release   Tutor hoặc Native
   Cài đặt môi trường kiểm thử tương tự production Master    Native
   Sửa đổi mã nguồn                                Master    Devstack
   =============================================== ========= ==================
.. note::
   **Lưu ý rằng tất cả các phương thức cài đặt đều yêu cầu một số kỹ năng nền tảng:**
    * Kiến thức cơ bản đối với hệ điều hành đã cài đặt.
    * Biết sử dụng command line terminal để thực hiện các tác vụ.
    * Có khả năng chẩn đoán và giải quyết vấn đề xảy ra với phần mềm hệ thống.

Trong phạm vi bài viết này, chúng tôi sẽ :ref:`cài đặt hệ thống Open edX bằng Tutor <tutor-settingup>`. `Tutor <https://docs.tutor.overhang.io/>`_ là bản phân phối hay phần mềm từ Open edX phát triển cho người dùng cuối dựa trên nền Docker, cho cả môi trường production và phát triển cục bộ trên máy tính của chúng ta. Mục tiêu của Tutor là giúp dễ dàng triển khai, tùy chỉnh, nâng cấp và mở rộng Open edX. Tutor đáng tin cậy, nhanh chóng, có thể mở rộng và phương thức này đã được sử dụng để triển khai hàng trăm nền tảng Open edX trên khắp thế giới.

Một số tính năng, đặc điểm nổi bật của Tutor mà chúng tôi đã cân nhắc để sử dụng phương thức này cho việc cài đặt Open edX:
 * 100% `mã nguồn mở <https://github.com/overhangio/tutor>`_.
 * Chạy hoàn toàn trên `Docker <https://www.docker.com/>`_
 * Kiến trúc có thể mở rộng với các `plugins <https://docs.tutor.overhang.io/plugins/index.html>`_.
 * Có thể hoạt động tương thích với `Kubernetes <https://docs.tutor.overhang.io/k8s.html>`_.

.. toctree::

   tutor
