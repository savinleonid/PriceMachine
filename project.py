import os


class PriceMachine:
    def __init__(self):
        self.data = []  # Список для хранения данных
        self.result = ''
        self.name_length = 0

    def load_prices(self, file_path=''):
        '''
        Сканирует указанный каталог. Ищет файлы со словом price в названии.
        В файле ищет столбцы с названием товара, ценой и весом.
        '''
        print('Загрузка прайс-листов...')
        if not file_path:
            file_path = './'
        files = [f for f in os.listdir(file_path) if "price" in f.lower() and f.endswith(".csv")]

        for file in files:
            file_path_full = os.path.join(file_path, file)
            try:
                with open(file_path_full, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                # Определяем заголовки
                headers = lines[0].strip().split(",")
                product_col, price_col, weight_col = self._search_product_price_weight(headers)

                if product_col is None or price_col is None or weight_col is None:
                    print(f"Файл {file} не содержит необходимых столбцов.")
                    continue

                # Обрабатываем строки данных
                for line in lines[1:]:
                    parts = line.strip().split(",")
                    try:
                        product_name = parts[product_col].strip()
                        price = float(parts[price_col])
                        weight = float(parts[weight_col])
                        self.data.append({
                            "product_name": product_name,
                            "price": price,
                            "weight": weight,
                            "file_name": file,
                            "price_per_kg": price / weight
                        })
                    except (IndexError, ValueError):
                        continue
            except Exception as e:
                print(f"Ошибка обработки файла {file}: {e}")

        print("Прайс-листы успешно загружены!.\n" if len(self.data) > 0 else "Прайс-листы не найдены.")

    def _search_product_price_weight(self, headers):
        '''
        Возвращает номера столбцов для названия продукта, цены и веса.
        '''
        column_map = {
            "product_name": ["товар", "название", "наименование", "продукт"],
            "price": ["цена", "розница"],
            "weight": ["вес", "масса", "фасовка"]
        }

        # Найти индексы для каждого типа столбца
        product_col = next((i for i, h in enumerate(headers) if h.lower() in column_map["product_name"]), None)
        price_col = next((i for i, h in enumerate(headers) if h.lower() in column_map["price"]), None)
        weight_col = next((i for i, h in enumerate(headers) if h.lower() in column_map["weight"]), None)

        return product_col, price_col, weight_col

    def export_to_html(self, fname='output.html', data=None):
        '''
        Экспортирует данные в HTML
        '''
        if data is None:
            data = self.data

        if not data:
            print("No data available to export.")
            return

        result = '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table border="1">
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''
        for i, item in enumerate(data, 1):
            result += f'''
                <tr>
                    <td>{i}</td>
                    <td>{item['product_name']}</td>
                    <td>{item['price']}</td>
                    <td>{item['weight']}</td>
                    <td>{item['file_name']}</td>
                    <td>{item['price_per_kg']:.2f}</td>
                </tr>
            '''
        result += '''
            </table>
        </body>
        </html>
        '''
        with open(fname, "w", encoding="utf-8") as file:
            file.write(result)
        print(f"Data successfully exported to {fname}")


    def find_text(self, text):
        '''
        Поиск текста в названии товара
        '''
        if not self.data:  # Проверка для списков
            print("No data available.")
            return []

        text = text.strip().lower()
        filtered_data = [
            item for item in self.data
            if text in item["product_name"].lower()
        ]
        filtered_data.sort(key=lambda x: x["price_per_kg"])
        return filtered_data


def console_interface():
    pm = PriceMachine()
    folder_path = './'  # путь к папке с прайс-листами. корневая папка по умолчанию
    pm.load_prices(folder_path)

    last_results = None

    while True:
        user_input = input("\nВведите текст для поиска товара (или 'exit' для выхода): ").strip()

        if user_input.lower() == "exit":
            print("Работа завершена.")
            break
        elif user_input.lower() == "export":
            file_name = input("Введите имя файла для экспорта (например, 'output.html'): ").strip()
            if not file_name.endswith(".html"):
                file_name += ".html"
            if last_results:
                pm.export_to_html(file_name, data=last_results)
            else:
                print("Нет результатов поиска. Экспортируется вся база данных.")
                pm.export_to_html(file_name)
        else:
            last_results = pm.find_text(user_input)
            if not last_results:
                print("Товары не найдены.")
            else:
                # Заголовок таблицы
                header = f"{'   Наименование'.ljust(19)} {'Цена'.rjust(12)} {'Вес'.rjust(5)} {'Файл'.ljust(15)} {'Цена за кг.'.rjust(10)}"
                print("\nНайденные товары:")
                print(header)
                print("-" * len(header))  # Разделитель

                # Форматирование строк таблицы
                counter = 1
                for item in last_results:
                    row = (
                        f"{counter}. "
                        f"{item['product_name'][:20].ljust(20)} "
                        f"{str(item['price']).rjust(8)} "
                        f"{str(item['weight']).rjust(5)} "
                        f"{item['file_name'][:15].ljust(15)} "
                        f"{f'{item['price_per_kg']:.2f}'.rjust(10)}"
                    )
                    counter += 1
                    print(row)

                print("\nДля экспорта результатов в HTML введите 'export'.")


if __name__ == "__main__":
    console_interface()
