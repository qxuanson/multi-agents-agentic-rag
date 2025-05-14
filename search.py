from google.adk.tools import agent_tool
from google.adk.agents import Agent
from google.adk.tools import google_search

search_agent = Agent(
    model='gemini-2.5-pro-exp-03-25',
    name='SearchAgent',
    instruction=""",
    Trả lời câu hỏi của người dùng trực tiếp bằng công cụ tìm kiếm Google; Cung cấp câu trả lời ngắn gọn và súc tích.
    Không nhất thiết phải tìm kiếm toàn bộ câu hỏi của người dùng, chỉ cần tìm kiếm phần cần sử dụng Google.
    Thay vì câu trả lời chi tiết, hãy cung cấp thông tin hành động ngay lập tức cho khách hàng, trong một câu duy nhất.
    Đừng yêu cầu người dùng tự kiểm tra hoặc tìm kiếm thông tin, đó là vai trò của bạn; hãy cố gắng cung cấp thông tin hữu ích nhất có thể.
    QUAN TRỌNG:
    - Luôn trả lời bằng dạng gạch đầu dòng
    - Chỉ rõ thông tin này quan trọng với người dùng như thế nào
    """,
    tools=[google_search],
)

search_google_agent = Agent(
    name="search_google_agent",
    model="gemini-2.5-pro-exp-03-25",
    description="Search Agent",
    tools=[agent_tool.AgentTool(agent=search_agent)],
)