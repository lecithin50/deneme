import cv2
import numpy as np
import streamlit as st
from camera_input_live import camera_input_live

# Başlık ve açıklama
st.title("QR Kod Okuyucu")
st.write("QR kodu kameraya gösterin ve çözümleme işlemini izleyin.")

# Kamera girişini al
image = camera_input_live()

# Eğer bir görüntü yakalandıysa, görüntüyü işleyin
if image is not None:
    # Görüntüyü ekranda göster
    st.image(image)

    # Görüntüyü bytes formatından OpenCV formatına dönüştür
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # QR kodu çözümlemek için OpenCV QRCodeDetector'u kullan
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    # Eğer QR kodu bulunursa, veriyi göster
    if data:
        st.write("# QR Kodu Bulundu")
        st.write("### QR Kod Verisi:", data)
        with st.expander("Detayları Göster"):
            st.write("BBox:", bbox)
            st.write("Düzeltilmiş QR kodu:", straight_qrcode)
    else:
        st.write("QR kodu bulunamadı. Lütfen tekrar deneyin.")

