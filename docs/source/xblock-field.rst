.. _xblock-field:

*******************
XBlock Fields
*******************

Sau các bước tạo **CounterXBlock**, ở trong tập tin **counter.py**, chúng ta tiến hành tạo một trường dữ liệu(sau đay gọi là field) với tên gọi là **count**.

.. code-block:: python

    count = Integer(
        default=0,
        scope=Scope.user_state,
        help="A simple counter, to show something happening")

Có thể truy cập giá trị count để hiện thị ra UI trong tập tin counter.html ở thư mục static

.. code-block:: html

    <div id="counter-value">{self.count}</div>

Các trường dữ liệu là những thuộc tính của của XBlock để lưu trữ và truy xuất dữ liệu.

Khi khởi tạo một trường XBlock, cần xác định ba tham số quan trọng

.. raw:: html

  <div class="table-wrapper">
    <table class="csv">
      <thead>
        <tr>
          <th>Tham số</th>
          <th>Mô tả</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>help</td>
          <td>Để mô tả field</td>
        </tr>
        <tr>
          <td>default</td>
          <td>Xác định giá trị khởi tạo của field</td>
        </tr>
        <tr>
          <td>scope</td>
          <td>Xác định phạm vi field</td>
        </tr>
      </tbody>
    </table>
  </div>

User Scope
-------------------
User Scope là phạm vi truy cập của người dùng.

Một field có thể có các scope sau:

.. raw:: html

  <div class="table-wrapper">
    <table class="csv">
      <thead>
        <tr>
          <th style="white-space: nowrap;">Phạm vi</th>
          <th>Mô tả</th>
          <th>Ví dụ</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="white-space: nowrap;">No user</td>
          <td>Field có thể không phụ thuộc vào bất kì user nào</td>
          <td>Field <strong>count</strong> đếm số lượng học viên hiện đang truy cập trang web<br>(mọi người đều nhìn thấy và không một ai có thể sửa được)</td>
        </tr>
        <tr>
          <td style="white-space: nowrap;">One user</td>
          <td>Field dành riêng cho một người dùng cụ thể.</td>
          <td>Một field <strong>id</strong> thì chỉ có một user có</td>
        </tr>
        <tr>
          <td style="white-space: nowrap;">All users</td>
          <td>Field chứa dữ liệu chung cho tất cả người dùng.</td>
          <td>Tổng số học viên trả lời một câu hỏi là như nhau đối với tất cả người dùng.</td>
        </tr>
      </tbody>
    </table>
  </div>

XBlock Scope
-------------------

XBlock Scope là phạm vi truy cập của XBlock.

Hiểu được phạm vi của XBlock, giúp lập trình có thể bảo vệ dữ liệu nhạy cảm, cũng như tái sử dụng hoặc chia sẻ các XBlock với nhau.

Field có thể tương tác XBlock qua bốn kiểu phạm vi:

.. raw:: html

  <div class="table-wrapper">
    <table class="csv">
      <thead>
        <tr>
          <th style="white-space: nowrap;">Phạm vi</th>
          <th>Mô tả</th>
          <th>Ví dụ</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="white-space: nowrap;">Block usage</td>
          <td>Field thuộc về một thực thể khi sử dụng XBlock trong một khóa học cụ thể. Trong hầu hết các trường hợp, nên sử dụng phạm vi này.</td>
          <td>Nếu người sử dụng tạo XBlock thăm dò ý kiến, các tùy chọn câu hỏi và câu trả lời của cuộc thăm dò ý kiến ​sẽ cụ thể theo cách sử dụng, vì có thể có các cuộc thăm dò khác nhau trong các phần khác nhau của khóa học</td>
        </tr>
        <tr>
          <td style="white-space: nowrap;">Block definition</td>
          <td>Field được định nghĩa một lần khi XBlock được khởi tạo. Có thể chia sẻ qua các khóa học và được tái sử dụng nhiều lần.</td>
          <td>Người sử dụng có thể tạo XBlock cho trình phát video và đặt các tùy chọn mặc định như tự động phát, phụ đề, v.v. trong định nghĩa. Tất cả các phiên bản của trình phát video đó sẽ sử dụng các giá trị mặc định.</td>
        </tr>
        <tr>
          <td style="white-space: nowrap;">Block type</td>
          <td>Là kiểu dữ liệu Python của field (ví dụ: Integer, String, ...)</td>
          <td>Nhà phát triển có thể có một field lưu trữ tên tác giả cho một loại XBlock cụ thể.</td>
        </tr>
        <tr>
          <td style="white-space: nowrap;">All</td>
          <td>Khi field có phạm vi kiểu All, mọi XBlock đều có thể truy cập và sử dụng dữ liệu.</td>
          <td>Nhà phát triển có thể tạo XBlock để hiển thị thời gian hiện tại. Khi mỗi phiên bản của XBlock được tải, field <strong>current_datetime</strong> sẽ được chia sẻ và hiển thị giá trị đó.</td>
        </tr>
      </tbody>
    </table>
  </div>

.. note::
    Khi sử dụng phạm vi kiểu All, có khả năng xảy ra xung đột giữa các field với nhau: trùng tên, rối loạn kiểu dữ liệu, …

Mối liên hệ giữa phạm vi người dùng và phạm vi block:

.. csv-table::
   :header: "", "UserScope.NONE", "UserScope.ONE", "UserScope.ALL"
   :widths: 60, 50, 50, 50
   :class: wordwrap

   BlockScope.DEFINITION, Scope.content, ,
   BlockScope.USAGE, Scope.settings, Scope.user_state, Scope.user_summary
   BlockScope.TYPE, , Scope.preferences,
   BlockScope.ALL, , Scope.user_info,

Fields and Data Storage
--------------------------------------
Mối quan hệ Field and Data Storage: các field được ghi và truy xuất dưới dạng các thực thể (instance) đơn lẻ, nên không thể lưu trữ một lượng lớn dữ liệu trong cùng một field. Do đó, ta nên chia nhỏ dữ liệu thành nhiều field nhỏ hơn để lưu trữ.

Ví dụ: nếu ta có một XBlock lưu trữ thông tin về học viên bao gồm tên, địa chỉ, và số điện thoại, thay vì lưu trữ tất cả thông tin trong một field, ta có thể chia thành các field nhỏ hơn như "name", "address" và "phone_number". Điều này giúp chúng ta quản lý dữ liệu một cách dễ dàng và tiết kiệm không gian lưu trữ.

Field and OLX
-------------------
Các field của XBlock tương ứng với các thuộc tính trong định nghĩa OLX (open learning XML).

Ví dụ: chúng ta có thể cấu hình field **count** trong XBlock **CounterXBlock** như trong đoạn code sau đây:

.. code-block:: python

    class CounterXBlock(XBlock):
        count = Integer(
            default=0, scope=Scope.user_state,
            help="A simple counter, to show something happening",
        )

Mặc định, XBlock **CounterXBlock** được đại diện trong OLX như ví dụ sau đây:

.. code-block:: html

    <counter count = 0/>

Chúng ta có thể tùy chỉnh cách XBlock được biểu diễn trong OLX bằng cách sử dụng các phương thức **xblock.parse_xml()** và **xblock.add_xml_to_node()**.

Kết luận
-------------------
Các field trong XBlock đóng vai trò quan trọng trong việc quản lý trạng thái, thuộc tính và dữ liệu liên quan đến một XBlock. Field cung cấp cho người sử dụng một cách linh hoạt và có cấu trúc để lưu trữ và truy cập dữ liệu.
