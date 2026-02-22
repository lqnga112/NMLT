import product_manager
import sys
import io

# -- PHẦN 1: MODULE HÓA MÃ NGUỒN --
# Thiết lập UTF-8 để hiển thị tiếng Việt trên Terminal Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except Exception:
        pass

def hien_thi_menu():
    """
    Hàm hiển thị menu chính của ứng dụng POLY-LAP.
    """
    print("\n" + "*"*35)
    print("   QUẢN LÝ CỬA HÀNG LAPTOP POLY-LAP")
    print("*"*35)
    print("1. Xem danh sách sản phẩm")
    print("2. Thêm mới một sản phẩm")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa một sản phẩm")
    print("5. Tìm kiếm sản phẩm theo tên")
    print("6. Thoát chương trình")
    print("*"*35)

def main():
    """
    Hàm khởi chạy chính (Main Luồng).
    - Bước 1: Gọi load_data() để tải dữ liệu khi mở máy.
    - Bước 2: Dùng vòng lặp while True để chạy menu.
    - Bước 3: Lưu dữ liêu khi thoát.
    """
    # Tải dữ liệu từ file JSON vào biến
    danh_sach_sp = product_manager.load_data()
    
    while True:
        hien_thi_menu()
        lua_chon = input("Mời bạn chọn chức năng (1-6): ")
        
        if lua_chon == '1':
            product_manager.display_all_products(danh_sach_sp)
            
        elif lua_chon == '2':
            danh_sach_sp = product_manager.add_product(danh_sach_sp)
            
        elif lua_chon == '3':
            danh_sach_sp = product_manager.update_product(danh_sach_sp)
            
        elif lua_chon == '4':
            danh_sach_sp = product_manager.delete_product(danh_sach_sp)
            
        elif lua_chon == '5':
            product_manager.search_product_by_name(danh_sach_sp)
            
        elif lua_chon == '6':
            # Lưu dữ liệu trước khi thoát (Yêu cầu Phần 3)
            product_manager.save_data(danh_sach_sp)
            print("Cảm ơn bạn đã sử dụng POLY-LAP! Hẹn gặp lại.")
            break
            
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại từ 1 đến 6.")

if __name__ == "__main__":
    main()

