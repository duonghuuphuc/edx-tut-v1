.. _xblock-fragment:

*******************
XBlock Fragments
*******************

Fragment đại diện cho các đoạn mã HTML, JavaScript và CSS được sử dụng để tạo nội dung và giao diện của một XBlock, fragment đảm nhận một vai trò cụ thể trong việc hiển thị và hoạt động của XBlock.

`Mỗi XBlock có thể chứa nhiều fragment, Ví dụ:`

- Fragment chứa mã HTML để hiển thị giao diện của XBlock

- Fragment chứa mã JavaScript để xử lý sự kiện và tương tác của người dùng

- Fragment chứa mã CSS để tùy chỉnh giao diện của XBlock.

Fragment Contents
------------------

**static/html/counter.html**: Nội dung trong một fragment thường là mã HTML, trong một số trường hợp, runtime có thể yêu cầu các view trả về các loại mime-type khác nhau như JSON hoặc XML.

.. code-block:: HTML

  <div class="counter_block">
    <h1>Counter App</h1>
    <div class="container">
      <div class="counter">
        <button id="increment-btn">+</button>
        <div id="counter-value">{self.count}</div>
        <button id="decrement-btn">-</button>
      </div>
      <button id="reset">Reset</button>
    </div>
  </div>

**static/css/counter.css**: Fragment có thể chứa external CSS hoặc inline CSS.

.. code-block:: HTML

  /* CSS for CounterXBlock */
  * {
    box-sizing: border-box;
    margin: 0px;
    padding: 0px;
  }
  .container {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
  }
  .container h1 {
      margin: 30px;
  }
  .counter {
      width: 30%;
      display: flex;
      justify-content: center;
  }
  #increment-btn,
  #decrement-btn,
  #reset {
      height: 50px;
      width: 120px;
      padding: 0 40px;
      border-radius: 10px;
      font-size: 40px;
      background-color: #2e8d46;
      border: 2px solid #2e8d46;
      color: white;
      margin: 20px;
      cursor: pointer;
  }

  #increment-btn:hover,
  #decrement-btn:hover,
  #reset:hover {
      background-color: #3c8b50;
      border: 2px solid #3c8b50;
      color: white;
      opacity: 0.8;
  }

  #reset {
      font-size: 20px;
      width: unset;
  }
  #counter-value {
      height: 50px;
      min-width: 120px;
      border-radius: 10px;
      background-color: rgba(255, 0, 0, 0.187);
      margin-top: 20px;
      font-size: 30px;
      display: flex;
      justify-content: center;
      align-items: center;
  }

**static/js/src/counter.js**: Một fragment chứa các tài nguyên JavaScript cần thiết để chạy XBlock, có thể bao gồm cả các tệp tin ngoài để liên kết và mã nguồn ngắn trong tài liệu. Khi các fragment được sắp xếp, các liên kết JavaScript bên ngoài sẽ được tạo thành duy nhất để tránh việc tải lại các tệp tin nhiều lần.

.. code-block:: javascript
  :linenos:

    function CounterXBlock(runtime, element) {
    const handlerUrlUpdateCount = runtime.handlerUrl(element, 'update_count');
      $('#increment-btn', element).click(function (eventObject) {
        $.ajax({
          type: 'POST',
          url: handlerUrlUpdateCount,
          data: JSON.stringify({ count: 1 }),
          success: updateCount,
        });
      });
    }

Hàm **CounterXBlock** trên có tác dụng tăng số đếm, thông qua việc gọi đến method **update_count** ở phía server. Khi người dùng nhấp vào các nút như "Tăng" hoặc "Giảm", chúng ta sẽ gửi yêu cầu AJAX tới server thông qua các URL đã xác định trước đó. Kết quả trả về từ server sẽ được sử dụng để cập nhật giá trị đếm trên giao diện người dùng.


Kết luận
----------------
Sử dụng fragment, chúng ta có thể tổ chức, quản lí giao diện và chức năng của XBlock theo ý muốn. Người phát triển có thể thêm, sửa đổi hoặc xóa bỏ các thành phần HTML, JavaScript và CSS trong fragment để tạo ra trải nghiệm người dùng tốt nhất cho khóa học.
