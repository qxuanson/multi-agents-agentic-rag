# Multi-Agent Agentic RAG Systems

---

![An Overview of Multi-Agent Agentic RAG Systems](System.png)
_Sơ đồ tổng quan về Hệ thống Đa Tác Tử Agentic RAG_

---

## Kiến Trúc Hệ Thống

Kiến trúc của Multi-Agent Agentic RAG Systems được thiết kế để tối ưu hóa sự hợp tác giữa các agent chuyên biệt, mỗi agent đóng góp vào quy trình tổng thể từ việc hiểu yêu cầu đến việc tạo ra kết quả cuối cùng.

Dưới đây là các thành phần chính của hệ thống:

1.  **User Interface / Input Handler (Giao diện Người dùng / Bộ xử lý Đầu vào):**
    *   Tiếp nhận yêu cầu từ người dùng.
    *   Tiền xử lý yêu cầu và chuyển đến Orchestrator Agent.

---

## Cài đặt

1.  **Prerequisites (Yêu cầu tiên quyết):**
    *   Python (phiên bản 3.8 trở lên được khuyến nghị)
    *   Pip (trình quản lý gói Python)
    *   Git
    *   (Tùy chọn nhưng khuyến nghị) Một môi trường ảo (virtual environment) như `venv` hoặc `conda`.

2.  **Clone the Repository (Sao chép Kho lưu trữ):**
    ```bash
    git clone https://github.com/TEN_NGUOI_DUNG_CUA_BAN/TEN_KHO_LUU_TRU_CUA_BAN.git
    cd TEN_KHO_LUU_TRU_CUA_BAN
    ```
    *(Thay thế `TEN_NGUOI_DUNG_CUA_BAN/TEN_KHO_LUU_TRU_CUA_BAN` bằng URL kho lưu trữ GitHub của bạn)*

3.  **Create and Activate Virtual Environment (Tạo và Kích hoạt Môi trường ảo - Khuyến nghị):**
    ```bash
    python -m venv venv
    # Trên Windows
    # venv\Scripts\activate
    # Trên macOS/Linux
    source venv/bin/activate
    ```

4.  **Install Dependencies (Cài đặt các Gói phụ thuộc):**
    Tạo một tệp `requirements.txt` liệt kê tất cả các thư viện cần thiết (ví dụ: `openai`, `langchain`, `streamlit`, `pinecone-client`, `fastapi`, `uvicorn`, v.v.).
    ```bash
    pip install -r requirements.txt
    ```
    *(Ví dụ nội dung tệp `requirements.txt`):*
    ```
    # openai
    # langchain
    # langchain-openai
    # python-dotenv
    # streamlit
    # pinecone-client
    # beautifulsoup4
    # ... các thư viện khác
    ```

5.  **Set Up Environment Variables (Thiết lập Biến Môi trường):**
    Nhiều thành phần (đặc biệt là LLMs và Vector Stores) yêu cầu API keys hoặc các thông tin cấu hình khác.
    Tạo một tệp `.env` trong thư mục gốc của dự án từ tệp `.env.example` (nếu có) và điền các giá trị cần thiết.
    Ví dụ tệp `.env`:
    ```env
    OPENAI_API_KEY="sk-YOUR_OPENAI_API_KEY"
    PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
    PINECONE_ENVIRONMENT="YOUR_PINECONE_ENVIRONMENT"
    # ... các biến môi trường khác
    ```
    Đảm bảo rằng tệp `.env` được thêm vào `.gitignore` để tránh rò rỉ thông tin nhạy cảm.

6.  **Prepare Knowledge Base (Chuẩn bị Cơ sở Tri thức - Nếu cần):**
    *   Nếu bạn đang sử dụng RAG, bạn cần chuẩn bị và xử lý (ví dụ: chunking, embedding) tài liệu của mình.
    *   Chạy các script cần thiết để nạp dữ liệu vào Vector Store hoặc cơ sở dữ liệu của bạn.
    *   *(Mô tả các bước cụ thể hoặc liên kết đến tài liệu hướng dẫn cho việc này)*
    ```bash
    # Ví dụ: python ingest_data.py
    ```

7.  **Run the Application (Chạy Ứng dụng):**
    *(Cung cấp lệnh để khởi chạy ứng dụng, ví dụ như một ứng dụng Streamlit hoặc một API FastAPI)*
    Ví dụ cho Streamlit:
    ```bash
    streamlit run app.py
    ```
    Ví dụ cho FastAPI:
    ```bash
    uvicorn main:app --reload
    ```
