"""Простой локальный HTTP-сервер с домашней страницей."""

# Импортируем стандартную библиотеку для работы с HTTP-сервером.
from http.server import BaseHTTPRequestHandler, HTTPServer


class HomePageHandler(BaseHTTPRequestHandler):
    """Обработчик запросов: отвечает HTML-страницей на путь /."""

    def do_GET(self):  # noqa: N802 (имя метода задано базовым классом)
        """Обрабатываем GET-запросы клиента."""
        if self.path == "/":
            # Подготавливаем HTML для домашней страницы.
            html = (
                "<!DOCTYPE html>"
                "<html lang='ru'>"
                "<head>"
                "  <meta charset='UTF-8'>"
                "  <title>Home Page</title>"
                "  <style>"
                "    body { font-family: Arial, sans-serif; margin: 40px; }"
                "    h1 { color: #2b6cb0; }"
                "  </style>"
                "</head>"
                "<body>"
                "  <h1>Добро пожаловать на Home Page!</h1>"
                "  <p>Этот сервер запущен локально на вашем компьютере.</p>"
                "</body>"
                "</html>"
            )

            # Отправляем успешный статус.
            self.send_response(200)
            # Указываем тип содержимого как HTML.
            self.send_header("Content-Type", "text/html; charset=utf-8")
            # Сообщаем длину ответа в байтах.
            self.send_header("Content-Length", str(len(html.encode("utf-8"))))
            # Завершаем заголовки.
            self.end_headers()
            # Пишем тело ответа.
            self.wfile.write(html.encode("utf-8"))
        else:
            # Для любых других путей возвращаем 404.
            self.send_error(404, "Страница не найдена")


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Запускаем HTTP-сервер на указанном адресе и порту."""
    server_address = (host, port)
    httpd = HTTPServer(server_address, HomePageHandler)
    print(f"Сервер запущен: http://{host}:{port}")
    print("Нажмите Ctrl+C, чтобы остановить сервер.")
    # Запускаем бесконечный цикл обработки запросов.
    httpd.serve_forever()


if __name__ == "__main__":
    # Точка входа при запуске файла напрямую.
    run_server()
