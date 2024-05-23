class TestResult:
    def __init__(self, success: bool, messages: list = None):
        if not success and not messages:
            raise ValueError("At least one message must be provided if success is False.")
        self.success = success
        self.messages = messages if messages is not None else []

    def __repr__(self):
        return f"TestResult(success={self.success}, messages={self.messages})"

    def add_message(self, message: str):
        self.messages.append(message)