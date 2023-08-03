TÀI LIỆU HƯỚNG DẪN CÀI ĐẶT VÀ TRIỂN KHAI OPEN EDX
=================================================

Giới thiệu về LMS
-----------------
Hệ thống quản lý dạy-học (**Learning Management System - LMS**) là phần mềm được sử dụng để quản lý các hoạt động dạy-học trên môi trường số, chẳng hạn, hỗ trợ cung cấp và quản lý các khóa học, chương trình đào tạo, tài nguyên dạy-học, theo dõi tiến độ dạy-học. Bên cạnh đó, LMS còn cho phép người dùng tương tác và giao tiếp với nhau thông qua diễn đàn, tin nhắn, và hỗ trợ đánh giá kết quả học tập và xuất báo cáo đánh giá tự động.

Khái niệm về hệ thống quản lý dạy học phát triển từ e-Learning, trải qua sự phát triển lớn về nhu cầu tập trung vào việc học từ xa trong thời gian đại dịch COVID-19, đến nay LMS đang chiếm phần lớn trong thị trường hệ thống học tập. Theo một báo cáo được thống kê bởi `Grand View Research, Inc <https://www.grandviewresearch.com/industry-analysis/learning-management-systems-market?utm_source=prnewswire&utm_medium=referral&utm_campaign=ICT_14-June-23&utm_term=learning_management_systems_market&utm_content=rd>`_, quy mô thị trường toàn cầu của LMS dự kiến ​​sẽ đạt 70,83 tỷ USD vào năm 2030, với mức tăng trưởng hàng năm trung bình (**Compound Annual Growth Rate - CAGR**) là 19,5% từ năm 2023 đến năm 2030. Các yếu tố chính thúc đẩy sự phát triển thị trường bao gồm dữ liệu lớn (**Big Data**), trí tuệ nhân tạo (**Artificial Intelligence - AI**), học trực tuyến (**E-Learning**), phương pháp học tập tích hợp (**Blended Learning**) và học trên các thiết bị di động (**M-Learning**).

Gần đây, sự tăng trưởng của lĩnh vực thực tế ảo tăng cường, đặc biệt là sự ra đời của các phần cứng dành cho người dùng cuối, sẽ là động lực thúc đẩy vai trò của LMS trong việc tạo ra những trải nghiệm mới cho hoạt động dạy và hoạt động học. Chẳng hạn, sự phát triển của công nghệ hình ảnh 3D giúp minh họa các cơ quan, bộ phận bên trong vật thể, cùng với công nghệ tương tác trực tuyến giúp nâng cao hiệu suất dạy-học thông qua mạng Internet.

.. raw:: html

  <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; gap: 20px; margin-bottom: 20px;">
    <img src="_static/images/edx-ar.jpg" alt="Thực tế ảo tăng cường cho phép người học tương tác với môi trường xung quanh theo một phương pháp hoàn toàn mới" style="max-width: 480px; width: 100%; object-fit: cover;"></img>
    <span style="font-weight: bold; max-width: 520px; word-wrap: break-word; white-space: wrap; text-align: center;">Thực tế ảo tăng cường cho phép người học tương tác với môi trường xung quanh theo một phương pháp hoàn toàn mới. Nguồn: <a href="https://www.apple.com/in/education/k12/docs/ar-in-edu-lesson-ideas.pdf" alt="Thực tế ảo">Apple Inc</a>
    </span>
  </div>

Trong chuỗi bài này, chúng tôi sẽ sử dụng Open edX làm nền tảng chính để minh họa cho hoạt động dạy-học trên nền tảng số. Trong phần thứ nhất của chuỗi bài, chúng tôi sẽ trình bày cách thức cài đặt và triển khai nền tảng Open edX. Tiếp theo đó, trong phần hai, chúng tôi sẽ trình bày cách khai thác hiệu quả nền tảng Open edX. Chúng tôi sẽ thể hiện đối tượng người đọc trong mỗi bài viết để người dùng dễ tiếp cận các nội dung bài viết, chẳng hạn, lập trình viên, người dạy, người học, người quản lý giáo dục.

Đăng ký theo dõi
----------------
Các bài đăng trên Website sẽ được đăng tải và cập nhật thường xuyên. Bạn đọc hãy đăng ký theo dõi chúng tôi qua địa chỉ email, bằng cách ghi nhận thông tin theo biểu mẫu `tại đây <https://www.google.com/>`_.

.. toctree::
  	:hidden:
	:maxdepth: 2
	:caption: Tài liệu hướng dẫn sử dụng

	edx-introduce
	edx-series
	xblock-sdk-series
	anaconda
	contributors
