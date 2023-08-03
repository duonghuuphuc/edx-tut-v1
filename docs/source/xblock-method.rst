.. _xblock-method:

*******************
XBlock Methods
*******************

XBlock cung cấp một tập hợp các phương thức giúp người sử dụng có thể tương tác và điều khiển hành vi của XBlock.

Phương thức xem (view methods)
---------------------------------------------------------

Các phương thức xem được dùng để xác định cách một XBlock có thể hiển thị cho từng người dùng theo các cách khác nhau.

.. note::

    Một XBlock có thể có một hoặc nhiều phương thức xem. XBlock có thể kiểm tra các ngữ cảnh hiện tại của người sử dụng và trả về một :ref:`fragment<xblock-fragment>` phù hợp.

Tiếp tục với ví dụ **counter**, ta định nghĩa phương thức xem hiển thị nội dung của người học:

.. code-block:: python

    def student_view(self, context=None):
        """
        The primary view of the CounterXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/counter.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/counter.css"))
        frag.add_javascript(self.resource_string("static/js/src/counter.js"))
        frag.initialize_js('CounterXBlock')
        return frag

Phương thức **student_view** sẽ tạo và trả về một fragment từ các tập tin HTML, JavaScript và CSS tĩnh. Trang web sẽ hiển thị fragment này cho người học (fragment như một phần html giúp hiển thị trên trang web).

Phương thức xử lý (handler methods)
---------------------------------------------------------

Handler methods là những phương thức xử lý business logic phía server. Handler được gọi bởi một URL nhất định.

Với **counter** XBlock, ta định nghĩa một phương thức xử lý để lấy nội dung file tĩnh phía server.

.. code-block:: python

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

Đoạn mã trên nhận vào một chuỗi đường dẫn rồi trả về nội dung file tĩnh với định dạng `utf-8 <https://vi.wikipedia.org/wiki/UTF-8>`__.

Các phương thức xử lý JSON **update_count** và **reset_count** trong file **counter.py** là những phương thức xử lý trong XBlock, được chú thích bằng **@XBlock.json_handler**. Những phương thức này xử lý các yêu cầu từ phía client và thực hiện các thay đổi liên quan đến giá trị đếm.

-  Phương thức **update_count** tăng giá trị đếm dựa trên dữ liệu đầu vào và
   trả về kết quả mới cho client.

-  Phương thức **reset_count** được sử dụng để đặt lại giá trị đếm về 0 và
   trả về giá trị mới của đếm cho client.

Nhờ vào annotation **@XBlock.json_handler**, XBlock có thể nhận biết và
gọi những phương thức này khi cần thiết.

.. code-block:: python

    @XBlock.json_handler
    def update_count(self, data, suffix=''):
            """
            An example handler, which increments the data.
            """
            # Just to show data coming in...
            self.count += data['count'] if data['count'] is not None else 0
            return {"count": self.count}
    @XBlock.json_handler
    def reset_count(self, data, suffix=''):
            """
            An example handler, which resets the data.
            """
            self.count = 0
            return {"count": self.count}

Kết luận
-------------------
XBlock methods là thành phần không thể thiếu để xử lý business logic phía server, cho phép ta xác định hành vi và chức năng của XBlock. Bằng cách triển khai các phương thức trong lớp XBlock, nhà phát triển có thể tạo ra những trải nghiệm tương tác linh hoạt trong việc dạy-học trên nền tảng Open edX.
