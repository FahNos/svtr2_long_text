import pyautogui
import time

def click_between_points(point1, point2, interval, duration=0.25):
    """
    Di chuyển chuột giữa hai điểm và nhấp chuột trái tại mỗi điểm.

    Args:
        point1: Tọa độ điểm đầu tiên (x, y).
        point2: Tọa độ điểm thứ hai (x, y).
        interval: Khoảng thời gian giữa mỗi lần di chuyển (tính bằng giây).
        duration: Thời gian di chuyển chuột (tính bằng giây). Mặc định là 0.25s.
    """

    try:
        while True:
            # Di chuyển đến điểm 1 và nhấp chuột
            pyautogui.moveTo(point1[0], point1[1], duration=duration)
            pyautogui.click()
            time.sleep(interval)


            # Di chuyển đến điểm 2 và nhấp chuột
            pyautogui.moveTo(point2[0], point2[1], duration=duration)
            pyautogui.click()
            time.sleep(interval)



    except KeyboardInterrupt:
        print("Chương trình đã dừng.")


if __name__ == "__main__":
    # Lấy tọa độ hai điểm. Bạn có thể thay đổi các giá trị này.
    # Để lấy tọa độ hiện tại của chuột, sử dụng pyautogui.position()
    print("Di chuyển chuột đến điểm đầu tiên và nhấn Enter để lấy tọa độ...")
    input()
    point1 = pyautogui.position()
    print(f"Tọa độ điểm 1: {point1}")

    print("Di chuyển chuột đến điểm thứ hai và nhấn Enter để lấy tọa độ...")
    input()
    point2 = pyautogui.position()
    print(f"Tọa độ điểm 2: {point2}")



    # Khoảng thời gian giữa mỗi lần di chuyển (tính bằng giây)
    interval = 10  # Ví dụ: 2 giây

    # Thời gian di chuyển chuột. Thời gian càng ngắn, chuột di chuyển càng nhanh.
    duration = 0.25

    print(f"Chuột sẽ di chuyển giữa {point1} và {point2} mỗi {interval} giây.")
    print("Nhấn Ctrl+C để dừng chương trình.")

    click_between_points(point1, point2, interval, duration)