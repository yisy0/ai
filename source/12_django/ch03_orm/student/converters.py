# 기본 converter 참조
class MyConverter:
    regex = r"\d{1,3}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)