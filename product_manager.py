import json
import os

# Đường dẫn tệp dữ liệu
DATA_FILE = "products.json"

# --- PHẦN 2: XÂY DỰNG CÁC CHỨC NĂNG CỐT LÕI ---

def load_data():
    """
    Hàm đọc dữ liệu từ file products.json.
    - Xử lý trường hợp file chưa tồn tại (FileNotFoundError).
    - Trả về danh sách rỗng nếu không có dữ liệu.
    """
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        # Trả về danh sách rỗng nếu có lỗi hoặc file chưa có
        return []

def save_data(products):
    """
    Hàm nhận vào danh sách sản phẩm và ghi vào file products.json.
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(products, f, ensure_ascii=False, indent=4)
        print("\n[Hệ thống] Lưu dữ liệu thành công!")
    except Exception as e:
        print(f"\n[Lỗi] Không thể lưu dữ liệu: {e}")

def add_product(products):
    """
    Hàm thêm sản phẩm mới.
    - Tự động tạo mã ID dạng LT01, LT02... dựa vào số lượng hiện có.
    """
    print("\n--- THÊM SẢN PHẨM MỚI ---")
    
    # Tạo mã ID tự động (Ví dụ: LT + số lượng hiện tại + 1)
    next_id_number = len(products) + 1
    new_id = f"LT{next_id_number:02d}"
    
    name = input("Nhập tên sản phẩm: ")
    brand = input("Nhập thương hiệu: ")
    
    while True:
        try:
            price = int(input("Nhập giá sản phẩm: "))
            quantity = int(input("Nhập số lượng tồn kho: "))
            break
        except ValueError:
            print("Lỗi: Giá và số lượng phải là số nguyên!")

    # Tạo dictionary cho sản phẩm mới (Yêu cầu Phần 1)
    new_product = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }
    
    products.append(new_product)
    print(f"Đã thêm sản phẩm thành công với mã: {new_id}")
    return products

def update_product(products):
    """
    Hàm cập nhật thông tin sản phẩm theo mã ID.
    - Nếu không tìm thấy, thông báo lỗi.
    """
    id_to_update = input("\nNhập mã sản phẩm cần cập nhật (ví dụ: LT01): ").upper()
    found = False
    
    for p in products:
        if p['id'].upper() == id_to_update:
            found = True
            print(f"--- Đang sửa sản phẩm: {p['name']} ---")
            
            # Cho phép sửa thông tin
            p['name'] = input(f"Tên mới ({p['name']}): ") or p['name']
            p['brand'] = input(f"Thương hiệu mới ({p['brand']}): ") or p['brand']
            
            while True:
                price_input = input(f"Giá mới ({p['price']}): ")
                if not price_input: break
                try:
                    p['price'] = int(price_input)
                    break
                except ValueError:
                    print("Lỗi: Giá phải là số nguyên!")
            
            while True:
                qty_input = input(f"Số lượng mới ({p['quantity']}): ")
                if not qty_input: break
                try:
                    p['quantity'] = int(qty_input)
                    break
                except ValueError:
                    print("Lỗi: Số lượng phải là số nguyên!")
            
            print("Cập nhật thành công!")
            break
            
    if not found:
        print(f"Lỗi: Không tìm thấy sản phẩm có mã {id_to_update}.")
    return products

def delete_product(products):
    """
    Hàm xóa sản phẩm theo mã ID.
    """
    id_to_delete = input("\nNhập mã sản phẩm cần xóa: ").upper()
    original_count = len(products)
    
    # Sử dụng list comprehension để lọc sản phẩm
    products[:] = [p for p in products if p['id'].upper() != id_to_delete]
    
    if len(products) < original_count:
        print(f"Đã xóa thành công sản phẩm {id_to_delete}.")
    else:
        print(f"Lỗi: Không tìm thấy mã sản phẩm {id_to_delete} để xóa.")
    return products

def search_product_by_name(products):
    """
    Hàm tìm kiếm sản phẩm theo từ khóa tên (không phân biệt hoa/thường).
    """
    keyword = input("\nNhập từ khóa tìm kiếm sản phẩm: ").lower()
    results = [p for p in products if keyword in p['name'].lower()]
    
    if results:
        print(f"\n--- Tìm thấy {len(results)} sản phẩm khớp với từ khóa '{keyword}' ---")
        display_all_products(results)
    else:
        print(f"\nKhông tìm thấy sản phẩm nào có từ khóa '{keyword}'.")

def display_all_products(products):
    """
    Hàm hiển thị toàn bộ sản phẩm dưới dạng bảng.
    - Nếu kho rỗng, hiển thị thông báo "Kho hàng trống."
    """
    if not products:
        print("\n--- KHO HÀNG TRỐNG ---")
        return

    print("\n" + "="*80)
    print(f"{'Mã ID':<10} | {'Tên sản phẩm':<25} | {'Thương hiệu':<15} | {'Giá':<12} | {'SL':<5}")
    print("-" * 80)
    for p in products:
        print(f"{p['id']:<10} | {p['name']:<25} | {p['brand']:<15} | {p['price']:<12,} | {p['quantity']:<5}")
    print("="*80)
