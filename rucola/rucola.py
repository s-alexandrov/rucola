import requests
from typing import Callable, Any


class ConfigurationError(Exception):
    """Исключение, если max_retries не целое число или меньше 1."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return "max_retries не корректен: " + str(self.message)


def blossom(max_retries=1):
    if max_retries < 1 and not max_retries % 2:
        raise ConfigurationError("должен быть целым числом и не менее 1")

    def decoration(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = dict()
            result[func.__name__] = {}
            result[func.__name__]["run"] = []
            for i in range(max_retries):
                try:
                    result[func.__name__]["is_success"] = True
                    x = func(*args, **kwargs)
                    result[func.__name__]["run"].append({"exception": None, "return": {x}})
                    break
                except BaseException as exc:
                    result_exception = exc.__doc__
                    result[func.__name__]["is_success"] = False
                    result[func.__name__]["run"].append({"exception": {result_exception}, "return": None})
            return result
        return wrapper
    return decoration


@blossom(2)
def get_page_content(url):
    resp = requests.get(url)
    return resp.content


content_with_retry = get_page_content("http://very_fake_address.com")
print(content_with_retry)
